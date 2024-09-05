import socket
import time

# опишем сервер
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# привяжем домен и порт
server_socket.bind(('localhost', 5000))
server_socket.listen()

while True:
    print('Перед подключением!')
    # метод принимает входящие подключения
    client_socket, addr = server_socket.accept()
    print(f'Подключение из: {addr}')

    # после подключение пользователя ждем реакции
    while True:
        print("Перед получением сообщения от юзера!")
        # типа сообщение
        request = client_socket.recv(4096)

        if not request:
            print("Отключаемся")
            time.sleep(1)
            break
        else:
            # закодироватьстроку в byte
            response = "I am listening you!\n".encode()
            client_socket.send(response)
        print('Outside inner While')
        client_socket.close()
