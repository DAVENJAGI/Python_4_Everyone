import requests
import json

user_name = input("Enter user name: ")
#repository = input("Enter repo name: ")

url = (f'http://api.github.com/users/{user_name}/repos')

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    with open("json_folder/get_request.json", "w") as file:
        json.dump(data,file, indent=2)
    print("Data exported to get_requests.json")
else:
    print("Github user couldn't be found")
