from socket import socket, AF_INET, SOCK_DGRAM

# Для взаимодействия с клиетами через сокеты
s = socket(AF_INET, SOCK_DGRAM)
s.bind(("127.0.0.1", 50000))

# Список для хранения адресов клиентов
clients_address = []

# Флаг для остановки сервера
stop = False

print("Запускаем сервер")

# Получаем через сокет адрес клиента. Если клиент новый, добавляем его в список
# для последующей рассылки сообщений.
while not stop:
    try:
        data, client_address = s.recvfrom(1024)
        if client_address not in clients_address:
            clients_address.append(client_address)

        print(client_address[0] + " / " + str(client_address[1]) + ":  ", end="")
        # Из байтового представления декодируем сообщение в формат utf-8
        print(data.decode("utf-8"))
        mes = "покидает нас"
        if mes in data.decode("utf-8"):
            clients_address.remove(client_address)

        for client in clients_address:
            try:
                if client_address != client:
                    s.sendto(data, client)
                print(clients_address)
            except:
                print("Ууууупс!")

    # Если что-то пошло не так, выводим сообщение об остановке сервера,
    # "взводим" флаг и завершаем цикл
    except:
        print("Останавливаем сервер")
        print(clients_address)
        stop = True

s.close()