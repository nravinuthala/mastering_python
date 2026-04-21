class Account():
    def calculate_interest():
        pass

class CCAccount(Account):
    def calculate_interest(self):
        #Credit card interest calculation details here
        pass

class LoanAccount(Account):
    def calculate_interest(self):
        #Loan account interest calculation
        pass

ccact1 = CCAccount()
lnacct1 = LoanAccount()

ccact1.calculate_interest()
lnacct1.calculate_interest()
