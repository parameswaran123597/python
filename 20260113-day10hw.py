from abc import ABC, abstractmethod
class User(ABC):
    def __init__(self,name,account_year):
        self.name=name
        self.account_year=account_year
        
    def account_age(self):
        return 2025-self.account_year
    @abstractmethod    
    def get_role(self):
        pass
        
            
class Admin(User):
    def __init__(self,name,account_year):
        super().__init__(name,account_year)
    
    def get_role(self):
        return "Admin"     
        
    def __str__(self):
        return f"Admin User: {self.name}, Account Age: {self.account_age()} years"     
class Guest(User):    
    def __init__(self,name,account_year):
        super().__init__(name,account_year)
    
    def get_role(self):
        return "Guest" 
        
    def __str__(self):
        return f"Guest User: {self.name}, Account Age: {self.account_age()} years"    

a=Admin("Paramu",2011)
g=Guest("Rahul",2024)
print(a.get_role())
print(a.account_age())
print(a)
print(g.get_role())    
print(g.account_age())
print(g)
    
    