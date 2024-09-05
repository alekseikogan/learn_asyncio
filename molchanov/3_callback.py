import socket
import selectors


selector = selectors.DefaultSelector()
to_monitor = []


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("localhost", 5000))
    server_socket.listen()

    selector.register(
        fileobj=server_socket,
        events=selectors.EVENT_READ,
        data=accept_connection)


def accept_connection(server_socket):
    print("Перед подключением!")
    client_socket, addr = server_socket.accept()
    print(f"Подключение из: {addr}")

    selector.register(
        fileobj=client_socket,
        events=selectors.EVENT_READ,
        data=send_message
    )


def send_message(client_socket):
    print("Перед получением сообщения от юзера!")
    request = client_socket.recv(4096)

    if request:
        response = "I am listening you!\n".encode()
        client_socket.send(response)
    else:
        print("Отключаемся")
        client_socket.close()


def event_loop():
    while True:
        # объекты которые готовы для чтения или записи
        events = selector.select()  # (key, events)
        for key, _ in events:
            callback = key.data
            callback(key.fileobj)


if __name__ == "__main__":
    server()
    event_loop()
