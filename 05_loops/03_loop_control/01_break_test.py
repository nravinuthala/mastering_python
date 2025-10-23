numbers = [11,33,55,38,55,75,37,21,23,22,41,13]

# for num in numbers:
#     if num % 2 == 0:
#         print(f"{num} is an even number")
#     print(f"{num} is an odd number")
# else:
#     print("Completed going through the list")

for num in numbers:
    if num % 2 == 0:
        print("found even number, hence exiting the loop")
        break
    print(f"{num} is an odd number")
else:
    print("Completed going through the list")