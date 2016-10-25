import requests

json_result = requests.get("http://localhost:8000/specials/").json()


for item in json_result:
    print(counter)
    print (item["name"])
    print (item["price"])
    print (item["description"])
