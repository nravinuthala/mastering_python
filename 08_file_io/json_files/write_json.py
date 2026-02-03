import json

# my_data = [
#     {
#         "id": "10",
#         "name": "john",
#         "dept": "hr"
#     },
#     {
#         "id": "20",
#         "name": "peter",
#         "dept": "finance"
#     }
# ]

# print(type(my_data))

with open("my_data.json") as in_file:
    data = json.load(in_file)

with open("new_data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)
