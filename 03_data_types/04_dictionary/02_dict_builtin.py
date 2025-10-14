# print(dir(dict))

# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

player_dictionalry = {
    "name": "John",
    "age": 25,
    "height": 6.5
}

player_sub_details = {
    "profession": "NBA Player", 
    "clubs": ["AR", "BC", "UN"]
}

# print(player_dictionalry)
# player_dictionalry.clear()
# print(player_dictionalry)

# print(player_dictionalry)
# player_dictionalry_copy = player_dictionalry.copy()
# print(player_dictionalry_copy)

# print(player_dictionalry["profession1"])
# print(player_dictionalry.get("profession1"))

# player_details_list = list(player_dictionalry.items())
# print(player_details_list)
# print(player_details_list[0][0])

# player_attributes = list(player_dictionalry.keys())
# print(player_attributes)

# player_values = list(player_dictionalry.values())
# print(player_values)

# print(player_dictionalry)
# popped_item = player_dictionalry.popitem()
# print(popped_item)
# print(player_dictionalry)

# print(player_dictionalry)
# popped = player_dictionalry.pop("age")
# print(popped)
# print(player_dictionalry)

# print(player_dictionalry)
# print(player_sub_details)

# player_dictionalry.update(player_sub_details)

# print(player_dictionalry)

# print(player_dictionalry)
# player_dictionalry["age"] = 30
# print(player_dictionalry)

new_keys = ["key1", "key2"]
new_dict = dict.fromkeys(new_keys)
print(new_dict)

new_dict.setdefault("key1", 30)
print(new_dict)

# player_dictionalry["age"] = 35
# # print(player_dictionalry)
# # print(player_dictionalry_copy)
# player_dictionalry["clubs"][1] = "DA"
# print(player_dictionalry)
# print(player_dictionalry_copy)

# dummy_keys = ["first", "second", "third"]
# test1 = dict.fromkeys(dummy_keys, "hi")
# print(test1)

# print(player_dictionalry["city"])
# print(player_dictionalry.get("city"))