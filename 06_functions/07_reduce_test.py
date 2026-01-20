from functools import reduce

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# def sum_the_nums(num1, num2):
#     return num1 + num2

# # print(sum_the_nums(34, 56))

# result = reduce(sum_the_nums, numbers)
# print(result)

# reduce takes a function and a list and condenses the list into a single value using the function

# you have a list - you want to sum up the elements of the list, or find greatest number of the list

# so the function which will be passed to reduce fuinction will accept 2 values and returns a single value

# sum - takes 2 values and returns their sum

# max - takes 2 values returns the bigger of the two

# min - takes 2 values and returns smaller of the two

def find_min(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2
    
def find_max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# [1, 3, 4, 5, 6, 7, 8, 9]

# [1, 4, 5, 6, 7, 8, 9]

# print(reduce(find_min, numbers))
# print(reduce(find_max, numbers))

print(reduce(lambda num1, num2: num1 + num2, numbers))