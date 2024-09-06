import socket
import time


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("localhost", 5000))
    server_socket.listen()

    while True:
        yield server_socket
        print("Перед подключением!")
        client_socket, addr = server_socket.accept()  # ждем ввода 
        print(f"Подключение из: {addr}")
        client(client_socket)


def client(client_socket):
    while True:
        yield client_socket
        print("Перед получением сообщения от юзера!")
        request = client_socket.recv(4096)  # ждем ввода

        if not request:
            print("Отключаемся")
            time.sleep(1)
            break
        else:
            response = "I am listening you!\n".encode()
            yield client_socket
            client_socket.send(response)  # ждем ввода

    client_socket.close()


server()