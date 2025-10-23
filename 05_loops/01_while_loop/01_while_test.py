num = int(input("Enter a number: "))

# print(num)

while num > 0:
    if num % 2 == 0:
        print(num)
    num -= 1
else:
    print("Please check your input and try again.")