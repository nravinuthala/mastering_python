# define or create fucntion
def greet():
    print("Hello")

# invoke or call the funciton to execute it
# greet()

# greet()

# greet()

# greet()

# greet()

    
def collect_student_details():
    name = input("Enter your name:")
    age = input("Enter your age:")
    email = input("Enter your email:")
    mobile = input("Enter your mobile:")
    first_name = name.split()[0] # Nagaraj Ravinuthala
    last_name = name.split()[1]
    print(first_name)
    print(last_name)

# collect_student_details()
# a function with mandatory parameters
# function with optional parameters
def display_details(name, age, email="Unavailable", mobile="Unavailable"):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Email: {email}")
    print(f"Mobile: {mobile}")

name1 = "Nagaraj"
age1 = 48
email1 = "nrav@email.com"
mobile1 = "12345678"

name2 = "Sreekar"
age2 = 16
email2 = "snrav@email.com"
mobile2 = "012345678"

# display_details(name1, age1) # arguments
# display_details(name1, age1, email1) # arguments
# display_details(name1, age1, email1, mobile1) # arguments
# display_details(name2)
# positional arguments
# def details(age, name):
#     print(f"Name: {name}, Age:{age}")

# details(48, "Nagaraj")

# def details(name, age):
#     print(f"Name: {name}, Age:{age}")

# details(48, "Nagaraj")
# details(age=48, name="Nagaraj")


#functions that return a single value
# def calculate_average(marks):
#     total = sum(marks)
#     average = total/ len(marks)
#     return average

# marks = [30, 40, 50, 60, 70]
# avg = calculate_average(marks)
# print(f"Agerage marks of the student is: {avg}")


#functions that return multiple values
def calculate_average(marks):
    total = sum(marks)
    average = total/ len(marks)
    return total, average

marks = [30, 40, 50, 60, 70]
# total, avg = calculate_average(marks)
# print(f"Agerage marks of the student is: {avg} and total is {total}")

ret_vals = calculate_average(marks)
print(ret_vals)

# functions with dynamic number of arguments




