import json
my_data_str = """[
    {
        "id": "10",
        "name": "john",
        "dept": "hr"
    },
    {
        "id": "20",
        "name": "peter",
        "dept": "finance"
    }
]"""

my_data = json.loads(my_data_str)

print(type(my_data))
print(my_data)

for item in my_data:
    print(item)

my_data_new_str = json.dumps(my_data)
print(type(my_data_new_str))