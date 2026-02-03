class Student():
    def __init__(self, aadharid):
        self.__aadharid = aadharid

    def get_aadhar(self):
        return self.__aadharid
    
    def set_aadhar(self, new_aadhar_id):
        self.__aadharid = new_aadhar_id


st1 = Student(1234)

# print(st1.__aadharid)
# st1.__aadharid = 5678
# print(st1.aadharid)

print(st1.get_aadhar())
st1.set_aadhar(5678)
print(st1.get_aadhar())