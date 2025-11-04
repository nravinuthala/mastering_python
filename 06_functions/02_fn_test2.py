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
def new_emp(name="Candidate", dept="Admin", position="Associate"):
    print(f"{name} has joined {dept} department as a {position}")


new_emp("Nagaraj", "Training", "Head")
new_emp("Sreekar", "Training")
new_emp("John")
new_emp()


