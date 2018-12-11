import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
result = json.loads(response.text)

with open("file.json", "w") as f:
    json.dump(result, f, indent=2)

sum_unique_users = 0
user_id = 1

try:
    for users in result:
        if users["userId"] == user_id:
            sum_unique_users += 1
            user_id += 1
    print("Количество уникальных пользователей =", sum_unique_users)
    print("----------------------------------------")
except Exception:
    print("Файл пустой или ошибка в содержимом файла")


"""
Словарь {наименование ключа=userId: значение ключа=количество id}
Если ключ есть и id не пустой, то увеличиваем значение ключа на единицу.
Если ключа нет, то при создании новой пары словаря одно id в цикле пропускается.
Поэтому значение нового ключа надо установить равным 1.
"""
dictionary_tasks = {}
for users in result:
    if users["id"] is not None:
        try:
            dictionary_tasks[users["userId"]] += 1
        except Exception:
            dictionary_tasks[users["userId"]] = 1

dictionary_completed = {}
for users in result:
    if users["completed"]:
        try:
            dictionary_completed[users["userId"]] += 1
        except Exception:
            dictionary_completed[users["userId"]] = 1

for i in range(1,sum_unique_users+1):
    print("У пользователя", i,
          "оригинальных задач =", dictionary_tasks.get(i),
          ", из них выполнено =", dictionary_completed.get(i))