import json

with open('states.json') as f:
    data = json.load(f)

for state in data['states']:
    print(state)
if __name__ == "__main__":
    json_file_name = "states.json"
    run_json_file(states.json)
