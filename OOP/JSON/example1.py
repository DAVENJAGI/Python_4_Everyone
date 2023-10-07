import json

with open("states.json") as f:
    data =  json.load(f)
#print(data)

#for state in data['states']:
#    print(state)

for state in data['states']:
    del state['area_codes']
#    print(data)

with open('new_states.json', 'w') as j:
          json.dump(data, j, indent=2)
#    print(state['name'], ':', state['abbreviation'])

