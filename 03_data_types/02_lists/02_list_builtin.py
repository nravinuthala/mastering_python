# print(dir(list))

# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

list_ops1 = ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert'] 
list_ops2 = ['remove', 'reverse', 'sort']

# print(list_ops1)
# list_ops1.append("pop")
# print(list_ops1)

# list_ops1.clear()
# print(list_ops1)

# list1 = [1,2,3,4,1,1,1,2,2,1,1]
# print(list1.count(1))

# list_ops1.extend(list_ops2)
# print(list_ops1)
# print(list_ops2)

# print(list_ops1.index('extend'))
# print(list1.index(2))
# list_ops1.insert(3,"pop")
# print(list_ops1)

# print(list_ops1)

# popped_elemnt = list_ops1.pop()
# print(popped_elemnt)
# print(list_ops1)

# popped_elemnt = list_ops1.pop()
# print(popped_elemnt)
# print(list_ops1)

# popped_elemnt = list_ops1.pop(1)
# print(popped_elemnt)
# print(list_ops1)

# list_ops1.remove("insert")
# print(list_ops1)

# player_details = ["Jordan", 25, 6.2]
# print(player_details)

# # player_details.reverse()
# # print(player_details)

# player_details.sort()
# print(player_details)

# list_ops1.sort(reverse=True)
# print(list_ops1)

# num_list = [34, 78, 23, 67, 9]
# print(num_list)
# num_list.sort(reverse=True)

# print(num_list)

# colors = ["red", "blue", "green"]
# colors_copy = colors.copy()

# print(colors)
# print(colors_copy)

# colors[2] = "pink"

# print(colors)
# print(colors_copy)

student = ["SB", 11, "Pinegrove College", [34, 67, 45]]

# student_copy = student.copy() # shallow copy
# print(student)
# print(student_copy)

# student[3][1] = 100
# # print(student[3][1])
# print(student)
# print(student_copy)

from copy import deepcopy

student_copy_deep = deepcopy(student)

print(student)
print(student_copy_deep)

student[3][1] = 100
# print(student[3][1])
print(student)
print(student_copy_deep)
