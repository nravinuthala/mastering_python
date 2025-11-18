# we have a list of numbers
# we want get a list with each number squared
numbers = [1, 2, 3, 4, 5]

# sq_number_list = []
# for num in numbers:
#     sq_num = num ** 2
#     sq_number_list.append(sq_num)

# print(squared_numbers)

def square_the_number(num):
    return num ** 2

print(square_the_number(5))

# for i in numbers:
#     squared_numbers.append(square_number(i))

squared_numbers_map = map(square_the_number, numbers)
squared_numbers_list = list(squared_numbers_map)

print(squared_numbers_list)
