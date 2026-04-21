class Person():
	def __init__(self, name, age, address):
			self.name = name
			self.age = age
			self.address = address
	
	def display_details(self):
		print(self.name)
		print(self.age)
		print(self.address)
		
p1 = Person("Choco", 25, "Bangalore")
p1.display_details()

class Patient(Person):
	def __init__(self, name, age, address, medical_history, cons_doc, regid):
		super().__init__(name, age, address)
		self.regid = regid
		self.medical_history = medical_history
		self.cons_doc = cons_doc
	
	def display_details(self):
		print(self.name)
		print(self.age)
		print(self.regid)
		print(self.medical_history)
		print(self.cons_doc)
		
pt1 = Patient('Agnes', 30, "Boston", ["diabetic"], "Dr. James", 100346)

pt1.display_details()

