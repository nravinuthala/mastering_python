numbers = [3, 7, 8, 9, 23]

def even_finder(num):
    return num % 2 == 0

# print(even_finder(5))
# print(even_finder(6))

even_num_filter = filter(even_finder, numbers)
even_num_list = list(even_num_filter)
print(numbers)
print(even_num_list)
