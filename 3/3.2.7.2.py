import random

sum = 0
x = random.randint(1,10)
y = random.randint(1,2)
f1 = str(x) + ".txt"
f2 = str(y) + ".txt"

print("Открываем файлы: ", f1, ", ", f2)

with open(f1, 'rt') as file_1:
    try:
        for s in file_1:
            sum += int(s)
    except Exception:
        print("Ошибка содержимого в файле 1")
file_1.close()

with open(f2, 'rt') as file_2:
    try:
        for s in file_2:
            sum += int(s)
    except Exception:
        print("Ошибка содержимого в файле 2")
file_2.close()

print("Сумма шести чисел = ", sum)
