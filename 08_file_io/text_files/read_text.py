file_handle = open("myfile.txt")
# file_data = file_handle.read()
# print(file_data)

# file_handle.seek(0)

# line1 = file_handle.readline()
# print(line1)
# line2 = file_handle.readline()
# print(line2)
# line3 = file_handle.readline()
# print(line3)

lines = file_handle.readlines()
print(lines)

print(file_handle.closed)

file_handle.close()

print(file_handle.closed)

file_handle.seek(0)