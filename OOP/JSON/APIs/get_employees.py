import requests
import json

employee_ID = input("Enter employee ID: ")

url = (f'https://jsonplaceholder.typicode.com/users/{employee_ID}')

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    with open("json_folder/get_employee.json", "w") as file:
        json.dump(data,file, indent=4)
    print("Data exported to get_employee.json")
else:
    print("Error: Couldn't import data")
