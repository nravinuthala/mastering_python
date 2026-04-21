class Person():
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_person_details(self):
        print(self.name)
        print(self.address)

class BankCustomer(Person):
    def __init__(self, name, age, address, account_type, account_no):
        super().__init__(name, age, address)
        self.account_type = account_type
        self.account_no = account_no

class LoanCustomer(Person):
    def __init__(self, name, age, address, loan_account_type, loan_account_no):
        super().__init__(name, age, address)
        self.loan_account_type = loan_account_type
        self.loan_account_no = loan_account_no

bank_cust1 = BankCustomer("Bob", 45, "Greenwoods", "Savings", 10012341)
bank_cust1.display_person_details()