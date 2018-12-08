import random

sum = 0
x = random.randint(1,10)
y = random.randint(1,10)
f1 = str(x) + ".txt"
f2 = str(y) + ".txt"

print("Открываем файлы: ", f1, ", ", f2)

file_1 = open(f1, 'rt')
for s in file_1:
    sum += int(s)
file_1.close()

file_2 = open(f2, 'rt')
for s in file_2:
    sum += int(s)
file_2.close()

print("Сумма шести чисел = ", sum)
