from abc import ABC, abstractmethod

class Account(ABC):
    @abstractmethod
    def calculate_interest():
        pass

class CCAccount(Account):
    
    def calculate_interest(self):
        pass
    
    def generate_statement(self):
        pass

ccact1 = CCAccount()
ccact1.calculate_interest()