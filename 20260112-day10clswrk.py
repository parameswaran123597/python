from abc import ABC, abstractmethod
class User(ABC):
    def __init__(self,name,join_year):
        self.name=name
        self.join_year=join_year
        
    def calculate_year(self):
        return 2025-self.join_year
    @abstractmethod    
    def get_role(self):
        pass
        
    def display(self):
        print("Name is", self.name,",joining year is", self.join_year,"and I am working here for", self.calculate_year())
      
            
class Customer(User):
    def __init__(self,name,join_year):
        super().__init__(name,join_year)
    
    def get_role(self):
        return "Customer"     
class Vendor(User):    
    def __init__(self,name,join_year):
        super().__init__(name,join_year)
    
    def get_role(self):
        return "Vendor" 

c=Customer("Pooja",2015)
v=Vendor("Erica",2018)
c.display()
v.display() 
    
    
    