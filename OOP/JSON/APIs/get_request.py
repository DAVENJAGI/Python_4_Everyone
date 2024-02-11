import requests
import json

user_name = input("Enter user name: ")
#repository = input("Enter repo name: ")

url = (f'http://api.github.com/users/{user_name}/repos')

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    repositories = []
    for repository in data:
        repositories.append(repository["name"])
    number_of_repos = len(repositories)
    print("Number of repositories is: ", number_of_repos)
    print(repositories)
else:
    print("Github user couldn't be found")

repository_name = input("Enter repository name: ")
url2 = (f'http://api.github.com/users/{user_name}/{repository_name}/tree/DAVE/')
