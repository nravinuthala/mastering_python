from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def sum_the_nums(num1, num2):
    return num1 + num2

# print(sum_the_nums(34, 56))

result = reduce(sum_the_nums, numbers)
print(result)