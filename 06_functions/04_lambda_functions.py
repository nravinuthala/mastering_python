# circ = 56
# circ = lambda side1, side2, side3: side1 + side2 + side3


# print(circ(34, 45, 67))

# def circ(side1, side2, side3):
#     return side1 + side2 + side3

# circ = lambda side1, side2, side3: side1 + side2 + side3

# print((lambda side1, side2, side3: side1 + side2 + side3)(34, 45, 67))


# higher order functions

# map function

# map is a function - which takes another function and applies it to each element of a list

# you have a list and you have a function 

# function takes a number and returns its square - 2 -> 4, 3 -> 9

mylist = [2, 3, 4]

# map - its take a function, takes a list, applies the function to each element of the list

def myfn(num):
    return num ** 2

my_squared_list = list(map(lambda num: num ** 2, mylist))

# my_squared_list = list(map(myfn, mylist))
print(my_squared_list)

# lambda expression or a lambda function is a way to define an anonymous function

# it starts with a keyword called lambda followed by function arguments : function expression.

# it can accept any number of arguments, but can have only one expression or statement