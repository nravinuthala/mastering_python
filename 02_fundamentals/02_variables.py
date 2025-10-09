# name is a variable
name = "Jill"
age = "30"
profession = "Musician"
# print("Hello " + name)

# this is using string concatenation
# print(name + " is " + age + " years old and is "+ profession + "by profession")

# we can simplify above using format function
# print("{} is {} years old and is {} by profession".format(name, age, profession))

# we can simplify further using formatted string or for short fstring
print(f"{name} is {age} years old and is {profession} by profession")


