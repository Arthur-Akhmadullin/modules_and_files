from socket import *
from threading import Thread

#Функция получения сообщений
def receive_message():
    while True:
        input_message = client_socket.recv(1024).decode("utf8")
        if input_message == "ВЫХОД":
            client_socket.close()
            break
        if not input_message:
            break
        # Показываем сообщения от сервера
        print(input_message)

#Функция отправки сообщений
def send_message():
    while True:
        output_message = input(":: ")
        client_socket.send(bytes(output_message, "utf8"))
        if output_message == "ВЫХОД":
            break


client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(('127.0.0.1', 50000))

receive_thread = Thread(target=receive_message)
send_thread = Thread(target=send_message)
receive_thread.start()
send_thread.start()
receive_thread.join()
send_thread.join()