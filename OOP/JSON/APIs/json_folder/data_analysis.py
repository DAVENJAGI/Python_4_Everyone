import matplotlib
from matplotlib import pyplot
import json

with open("get_request.json", "r") as file:
    data = json.load(file)
    repository_size = []
    repository_number = []
    repository_name = []

    for repository in data:
        repository_size.append(repository["size"])

    for repository in data:
        repository_number.append(repository['name'])

    for repository in data:
        repository_name.append(repository['name'])

    print("no of repos: ", (len(repository_number)))
    print("size of repos: ", repository_size)
    print("repo names: ", repository_name)

    count = len(repository_number)
    number_list = list(range(1, count + 1))
     
    x_values = number_list
    y_values = repository_size 

    pyplot.plot(x_values, y_values, color="red")
    pyplot.title("Plot for repo sizes in github")
    pyplot.xlabel("number of repositories")
    pyplot.ylabel("size of repository in kilobytes")
    pyplot.show()
