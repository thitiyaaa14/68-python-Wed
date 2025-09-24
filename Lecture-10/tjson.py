import json
data = {'name': 'Alice', 'age': 30, 'city': 'New York'}
json_string = json.dump(data)
print(f'JSON string: {json_string}')

parsed_data = json.loads(json_string)
print(f'Parsed data: {parsed_data}')
print(f'Name: {parsed_data["name"]}')
print(f'Age: {parsed_data["age"]}')
