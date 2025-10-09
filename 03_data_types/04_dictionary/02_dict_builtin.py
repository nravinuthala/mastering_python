# print(dir(dict))

# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

player_dictionalry = {
    "name": "John",
    "age": 25,
    "height": 6.5,
    "profession": "NBA Player", 
    "clubs": ["AR", "BC", "UN"]
}

# print(player_dictionalry)
# player_dictionalry.clear()
# print(player_dictionalry)

# print(player_dictionalry)
# player_dictionalry_copy = player_dictionalry.copy()
# print(player_dictionalry_copy)

# player_dictionalry["age"] = 35
# # print(player_dictionalry)
# # print(player_dictionalry_copy)
# player_dictionalry["clubs"][1] = "DA"
# print(player_dictionalry)
# print(player_dictionalry_copy)

dummy_keys = ["first", "second", "third"]
test1 = dict.fromkeys(dummy_keys, "hi")
print(test1)