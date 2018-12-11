import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
result = json.loads(response.text)

with open("file.json", "w") as f:
    json.dump(result, f, indent=2)

user_id = 1
dictionary_users = {}

for users in result:
    if users["userId"] == user_id:
        dictionary_users[users["userId"]] = {"tasks": 0, "completed": 0}
        user_id += 1
    if users["id"]:
        dictionary_users[users["userId"]]["tasks"] += 1
    if users["completed"]:
        dictionary_users[users["userId"]]["completed"] += 1
print("Количество уникальных пользователей =", len(dictionary_users))
print("-------------------------------------")

for i in range(1, len(dictionary_users)+1):
    print("У пользователя", i,
          "оригинальных задач =", dictionary_users[i]["tasks"],
          ", из них выполнено =", dictionary_users[i]["completed"])