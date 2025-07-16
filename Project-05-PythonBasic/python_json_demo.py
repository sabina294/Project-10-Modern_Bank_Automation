import json

# some JSON:
user_details =  '{"name":"John", "age":30, "city":"New York"}'

# parse x:
user_details_load = json.loads(user_details)

# the result is a Python dictionary:
print(user_details_load["age"])

# a Python object (dict):
user_info = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(user_info)

# the result is a JSON string:
print(y)