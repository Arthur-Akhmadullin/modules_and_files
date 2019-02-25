import time
from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread

# Данные сервера. Для передачи данных "по адресу"
server = ("127.0.0.1", 50000)

s = socket(AF_INET, SOCK_DGRAM)
s.connect(("127.0.0.1", 50000))
s.setblocking(0)

# stop - флаг присутсвия участника в чате. Если True, то запрещаем передачу сообщений
# connection - флаг. Есть соединение с чатом или нет.
stop = False
connection = False
name_of_participant = input("Имя нового участника чата: ")
quit_message = False

def receving (name, sock):
    while stop == False:
        try:
            while True:
                data, address = sock.recvfrom(1024)
                print(data.decode("utf-8"))
        except:
            pass
socket_thread = Thread(target=receving, args=("Thread", s))
socket_thread.start()

while stop == False:
    if connection == False:
        s.sendto((name_of_participant + " присоединяется к чату").encode("utf-8"), server)
        connection = True
    else:
        try:
            message = input("")
            if message != "":
                s.sendto((name_of_participant + " пишет: " + message).encode("utf-8"), server)
        except:
            quit_message = True
            s.sendto((name_of_participant + " покидает нас").encode("utf-8"), server)
            stop = True

socket_thread.join()
s.close()