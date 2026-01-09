class Person:
      def __init__(self,name,age):
       self.name=name
       self.age=age
    
      def show_details(self):
       print("\nMy name is {} and age is {}".format(self.name,self.age))
     
class Employee(Person):
     def __init__(self,name,age,employee_id):
      Person.__init__(self,name,age)
      self.employee_id=employee_id
    
     def show_details(self):
        print("\nMy name is",self.name,". I am ",self.age,"years old " ,"and employee id is ",self.employee_id)
 
class PartTime(Person):
     def __init__(self,name,age,working_hours):
      Person.__init__(self,name,age)
      self.working_hours=working_hours
     
     def show_details(self):
        print("\nMy name is",self.name,". I am ",self.age,"years old " ,"and working hours is ",self.working_hours)  
        
class Consultant(Employee,PartTime):
     def __init__(self,name,age,employee_id,working_hours,project_name):
      Employee.__init__(self,name,age,employee_id)
      PartTime.__init__(self,name,age,working_hours)
      self.project_name=project_name
     
     def show_details(self):
        print("\nMy name is",self.name,". I am ",self.age,"years old " ,"and employee id is ",self.employee_id," and working hours is ",self.working_hours,"and  project name is ",self.project_name)
        
        
p=Person("Mahi",28)
e=Employee("Subash",32,"E101")
pt=PartTime("Pooja",23,8.5)
c=Consultant("Paramu",24,"E041",17.2,"Swasthiya Sanjeevani")
p.show_details()
e.show_details()
pt.show_details()
c.show_details()
        
         
    
    