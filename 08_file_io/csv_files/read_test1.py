import csv
# csv_file = open("my_data.csv")
# csv_data = csv.DictReader(csv_file)
# csv_lines = list(csv_data)
# # print(csv_lines)
# for line in csv_lines:
#     print(line)

# print(csv_file.closed)

# csv_file = open("my_data.csv")
with open("my_data.csv") as csv_file:
    csv_data = csv.DictReader(csv_file)
    csv_lines = list(csv_data)
    for line in csv_lines:
        print(line)
    print("inside", csv_file.closed)
print("outside", csv_file.closed)