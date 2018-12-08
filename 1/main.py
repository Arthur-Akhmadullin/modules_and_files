from my_packet.apartment_price.price import apartment_price as AP

print("Введите исходные данные:")
print("------------------------")

square = float(input("Площадь квартиры: "))
price_for_1sqm = int(input("Цена за 1 кв.м: "))
floor = int(input("Этаж: "))
discount = int(input("Скидка: "))

print("Цена квартиры составляет: ",
      AP(square, price_for_1qm, floor, discount))