# # define or create fucntion with an input parameter
# def greet(name):
#     print(f"Hello {name}.")

# # Calling function with argument
# greet("Nagaraj")

# greet("Eshaan")

# greet("Sreekar")

# defining a function with multiple input parameters
# def greet(name, age, profession):
#     print(f"{name} is {age} years old and is {profession} by profession.")

# greet("Sreekar", 16)

# name = input("Enter your name:")
# yob = int(input("Enter your year of birth:"))

# def calc_age(n, y):
#     age = 2025 - y
#     print(f"Hello {n}. You are {age} years old.")

# calc_age(name, yob)

# function with positional arguments
# def display_details(name, age):
#     print(f"{name} is {age} years old.")

# # display_details(50, "John")
# display_details(age=50, name="John")

# function with default argument
# def new_emp(name="Candidate", dept="Admin", position="Associate"):
#     print(f"{name} has joined {dept} department as a {position}")


# new_emp("Nagaraj", "Training", "Head")
# new_emp("Sreekar", "Training")
# new_emp("John")
# new_emp()

# functions with keyword arguments
# def new_emp(name, dept, position):
#     print(f"{name} has joined {dept} department as a {position}")

# # new_emp("HR", "Associate", "Arthur")
# # function call with keyword arguements
# new_emp(dept="HR", position="Associate", name="Arthur")
# new_emp(position="Associate", name="Arthur", dept="HR")

# full time emps - salary, bonus, pf, insurance, leave encashment
# contract emps - salary, bonus

# functions with variable number of arguments
# def emp_separation(*args):
#     # print(args)
#     # print(type(args))
#     for arg in args:
#         print(arg)

# emp_separation("salary", "bonus", "pf", "insurance", "leave_encashment")
# # emp_separation("salary", "bonus")
# # emp_separation("leave_encashment")

# def calculate_average_marks(math_marks, lang_marks, comp_marks, science_marks):
#     sum_marks = math_marks + lang_marks + comp_marks + science_marks
#     average = sum_marks // 4
#     print(average)

# def calculate_average_marks(*marks):
#     sum_marks = sum(marks)
#     average = sum_marks // len(marks)
#     print(average)

# calculate_average_marks(90, 87, 60, 56)
# calculate_average_marks(90, 87, 56)
# calculate_average_marks(90, 87)

# def calculate_circumference(side1, side2, side3):
#     circ = side1 + side2 + side3
#     print(circ)

# def calculate_circumference(*sides):
#     circ = sum(sides)
#     print(circ)

# calculate_circumference(45, 67, 34)

# calculate_circumference(45, 67, 34, 45)

# print("hi")
print("hi","hello", sep="/", end=" | ")
print(1 , end=" | ")
print(2)