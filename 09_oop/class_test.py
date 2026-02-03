class Student():
    def __init__(self, name, age, city, courses, marks):
        self.name = name
        self.age = age
        self.city = city
        self.courses = courses
        self.marks = marks
    
    def claculate_average(self):
        total = sum(self.marks)
        avg = total / len(self.marks)
        print(avg)
    
st1 = Student("Nag", 15, "Hyderabad", "MPC", [67, 68, 89])
print(st1.name)
print(st1.age)
st1.claculate_average()

# st1, st2, st3
