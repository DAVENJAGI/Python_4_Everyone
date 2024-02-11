#!/usr/bin/python3
import requests
import json

identifiers = input("Enter identifier name: ")
#repository = input("Enter repo name: ")

def Stock():
    url = (f'https://api-v2.intrinio.com/stock_exchanges/{identifiers}/prices/reatime')

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        with open("json_folder/intrio.json", "w") as file:
            json.dump(data,file, indent=2)
        print("Data exported to intrio.json")
    else:
        print("Endpoint couldn't be found")


if __name__ == "__main__":
    Stock()
