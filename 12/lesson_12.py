import random

def long_process(id, n):
    sum = 0
    for x in range(n):
        sum += x
        print(id, sum)
        if x < n-1:
            yield
        else:
            yield sum


number_of_processes = int(input("Укажите количество одновременных генераторов: "))

#Рандомно формируем список чисел, представляющих собой второй параметр генератора
array_second_parameter = []
for parameter in range(number_of_processes):
    array_second_parameter.append(random.randint(4, 10))
print("Список вторых параметров: ", array_second_parameter)

#Словарь, содержащий ссылки на объект-генератор
dict_gen = {}
for i in range(number_of_processes):
    dict_gen["id"+str(i+1)] = long_process("id"+str(i+1), array_second_parameter[i])
print("Словарь, содержащий ссылки на объект-генератор: ", dict_gen)

#Словарь, возвращающий результаты вычислений
dict_res = {}
for i in range(number_of_processes):
    dict_res["id" + str(i + 1)] = None
print("Словарь, возвращающий результаты вычислений: ", dict_res)

#Количество итерация - это максимальный элемент в массиве параметров
max_value_of_parametres = max(array_second_parameter)
print("Количество итераций = ", max_value_of_parametres)


for i in range(max_value_of_parametres):
    for j in range(number_of_processes):
        if dict_res['id'+str(j+1)] is None:
            dict_res['id'+str(j+1)] = next(dict_gen['id'+str(j+1)])
    print("-----------------------------")

print("РЕЗУЛЬТАТ: ", dict_res)



