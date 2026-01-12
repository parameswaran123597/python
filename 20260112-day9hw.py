class Account:
    def __init__(self,_name,_balance):
        self._name=_name
        self._balance=_balance
    def __add__(self, other):
        return self._balance + other._balance    
    
class SavingsAccount(Account):
    def __init__(self,_name,_balance):
        super().__init__(_name,_balance)
        
    def calculate_interest(self):
        return self._balance*0.05
        
class CurrentAccount(Account):
    def __init__(self,_name,_balance):
        super().__init__(_name,_balance)
        
    def calculate_interest(self):
        return self._balance*0.02   
        

sa=SavingsAccount("Ravi",10000)
ca=CurrentAccount("Anjali",15000)
print("Savings Account")
print("Name:", sa._name)
print("Balance:", sa._balance)
print("Interest:", sa.calculate_interest())

print("\nCurrent Account")
print("Name:", ca._name)
print("Balance:", ca._balance)
print("Interest:", ca.calculate_interest())

print("\nTotal Balance:", sa + ca)
    
    