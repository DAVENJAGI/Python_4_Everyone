#!/usr/bin/python3
import json

with open('states.json') as f:
    data = json.load(f)
print(data)

#for state in data['states']:
#    print(state)
