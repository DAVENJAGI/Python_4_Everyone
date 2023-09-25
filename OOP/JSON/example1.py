import json

people_string = '''
{
        "people": [
            {
                "name": "Dave Njagi",
                "phone_number": "+254796894542",
                "email": "njagidave@gmail.com",
                "has_license": False
            },
            {
                "name": "Jane Doe",
                "phone_number": "568-555-5153",
                "email": "janedoe@gmail.com",
                "has_license": True
            }
        ]
}
'''
data = json.loads(people_string)
print(data)
