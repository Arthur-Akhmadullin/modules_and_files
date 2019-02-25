from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

#Функция для установки соединения с клиентом
def connect_with_client():
    while True:
        client, client_address = server.accept()
        print("УСТАНОВЛЕНО СОЕДИНЕНИЕ С %s:%s" % client_address)
        client.send(bytes("Ваш ник? Введите и нажмите ENTER", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()

#Функция отправки сообщений
def handle_client(client):
    #Перехватываем первое сообщение после вопроса - это клиент ввел свой ник
    #Сохраняем его в переменную и словарь и приветствуем
    nick = client.recv(1024).decode("utf8")
    server_message = "К нам присоединяется %s" % nick
    send_to_all_clients(bytes(server_message, "utf8"))
    clients[client] = nick

    #Пока клиент не введет слово "ВЫХОД", будем принимать сообщения и рассылать его
    #Иначе закроем соединение, удалим клиента из словаря и всем сообщим, что он вышел
    while True:
        server_message = client.recv(1024)
        if server_message != bytes("ВЫХОД", "utf8"):
            send_to_all_clients(server_message, nick + ": ")
        else:
            client.send(bytes("ВЫХОД", "utf8"))
            client.close()
            del clients[client]
            send_to_all_clients(bytes("%s выходит из чата" % nick, "utf8"))
            break

#Функция рассылки сообщений всем участникам чата
def send_to_all_clients(message, prefix=""):
    for sock in clients:
        sock.send(bytes(prefix, "utf8") + message)

#Клиентов и их адреса будем хранить в словарях
#Если клиент вышел из чата, удаляем его из словаря
clients = {}
addresses = {}
server = socket(AF_INET, SOCK_STREAM)
server.bind(('127.0.0.1', 50000))

if __name__ == "__main__":
    #число установленных соединений, которые могут быть обработаны в любой момент времени = 5
    server.listen(5)
    print("[СЕРВЕР ЗАПУЩЕН...]")
    ACCEPT_THREAD = Thread(target=connect_with_client)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    server.close()