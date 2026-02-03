import csv
new_data1 = {"id": 30, "name": "Harvey", "dept": "IT"}
new_data2 = {"id": 40, "name": "Jane", "dept": "IT"}
new_data3 = {"id": 50, "name": "Paul", "dept": "IT"}

# csv_file = open("my_data_new.csv", "w")
# # fields = ["id", "name", "dept"]
# fields = list(new_data1.keys())
# writer = csv.DictWriter(csv_file, fieldnames=fields, lineterminator="\n")

# writer.writeheader()
# writer.writerow(new_data1)
# writer.writerow(new_data2)
# writer.writerow(new_data3)

csv_file = open("my_data.csv", "a")
fields = list(new_data1.keys())
writer = csv.DictWriter(csv_file, fieldnames=fields, lineterminator="\n")
writer.writerow(new_data2)
writer.writerow(new_data3)