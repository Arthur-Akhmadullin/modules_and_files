import random
from threading import Thread

# Функция подсчета суммы в части массива
def sum_part_array(part_array, part_sum):
    part_sum.append(round(sum(elem for elem in part_array), 2))

# Функция, которая делит массив на части и запускает потоки
def sum_random_numbers(arr, nt):
    # Объявим массив для хранения результатов суммы на каждой итерации
    iteration_sum = []

    # На каждой итерации выделяем часть массива для вычисления части суммы
    for i in range(nt):
        d, m = divmod(len(arr), nt)
        part_arr = arr[i * d + min(i, m):(i + 1) * d + min(i + 1, m)]

        # Объявляем поток. Результат его работы - добавление части суммы в массив
        # А также выведем результат работы каждого потока
        Thread(target=sum_part_array, name="Thread #%s" % (i+1), args=(part_arr, iteration_sum)).start()
        print("Thread #%s" % (i+1), iteration_sum)

    print("Сумма =", round(sum(iteration_sum), 2))
    return(iteration_sum)


array = []
number_elements_of_array = int(input("Укажите количество чисел в массиве: "))

for i in range(0, number_elements_of_array):
    array.append(round(random.uniform(1, 10), 2))

number_threads = int(input("Укажите количество потоков: "))

print(sum_random_numbers(array, number_threads))

# Проверим через обычный цикл
sum_common_cycle = 0
for i in array:
    sum_common_cycle += i
print("Сумма через обычный цикл = ", round(sum_common_cycle, 2))
