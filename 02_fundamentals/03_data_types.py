# # variables values wrapped in quotes are called strings, they are used to represent text content
# # name is a string variable or type of the variable name is string or str for short
# name = "Jordan" 
# # age is a number (integer) variable or type of the variable age is integer or int for short
# age = 25
# # height is a number (decimal or floating point) variable or type of the variable height is float
# height = 6.5
# profession = "NBA Player"

# is_he_available = True

# print(type(name))
# print(type(age))
# print(type(height))
# print(type(is_he_available))

# c1 = 3 + 4j
# print(c1)
# print(type(c1))

# c2 = complex(8, 9) # same as 8 + 9j
# print(c2)
# print(type(c2))
# print(c2.real)
# print(c2.imag)

###################################

# if i want to store a list of multiple values together i can use a data type called list

# names = ["John", "Jane", "Jill"]
# print(names)
# print(type(names))

# # there is a special type of list called tuple
# names_tuple = ("John", "Jane", "Jill")
# print(names_tuple)
# print(type(names_tuple))

# # we can also store multipel values as a set 
# names_set = {"John", "Jane", "Jill"}
# print(names_set)
# print(type(names_set))

player_details = ["John", 25, 6.5, "NBA Player"]
print(player_details)

# mapping data type
player_dictionalry = {
    "name": "John",
    "age": 25,
    "height": 6.5,
    "profession": "NBA Player"
}
print(player_dictionalry)
print(type(player_dictionalry))