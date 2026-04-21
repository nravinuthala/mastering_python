# from datetime import date1
# x = 3
# y = 'hi'
# a = 0
# try:
#     # print(int(y))
#     colors = ['r', 'g', 'b']
#     # print(colors[3])
#     emp = {"name": "Pete"}
#     print(emp["age"])
#     print(z)
#     print(x/a)
# except ValueError as e:
#     print("Please check if you are trying to convert a string into an int.")
# except IndexError as e:
#     print("Please check to ensure you are not trying to extract outside the list index.")
# except KeyError as e:
#     print("Please check your key.")
# except Exception as e:
#     print(e)

# # try:
# #     print(x/y)
# # except Exception as error:
# #     print(error)
# # else:
# #     print("Your division is fine")

class MyException(Exception):
    def __init__(self, msg):
        self.msg = msg

amt = int(input("Enter the amount you wish to withdraw."))

try:
    if amt < 100:
        raise MyException("Minimum amount to withdraw is 100.")
except MyException as me:
    print(me)
