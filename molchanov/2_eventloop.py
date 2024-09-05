import socket
from select import select
# файловый дескриптор это номер файла
# .fileno()
# функция select мониторит изменение файлов, которые мы ей передали
# она получает на вход списки [для чтения], [для записи], [ошибки]
# и возвращает эти объекты после их освобождения (доступности)

to_monitor = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("localhost", 5000))
server_socket.listen()


def accept_connection(server_socket):
    print("Перед подключением!")
    client_socket, addr = server_socket.accept()
    print(f"Подключение из: {addr}")
    to_monitor.append(client_socket)


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
        ready_to_read, _, _ = select(to_monitor, [], [])
        for sock in ready_to_read:
            if sock is server_socket:
                accept_connection(sock)
            else:
                send_message(sock)


if __name__ == '__main__':
    to_monitor.append(server_socket)
    event_loop()
