class Employee:
      def __init__(self,name,role):
       self.name=name
       self.role=role
    
      def display(self):
       print("\nMy name is {} and role is {}".format(self.name,self.role))
     
class Trainer(Employee):
     def __init__(self,name,role,specialization):
      Employee.__init__(self,name,role)
      self.specialization=specialization
    
     def display(self):
        print("\nMy name is {}, my role is {} and my specialization is {}".format(self.name,self.role,self.specialization))
 
class YogaInstructor(Employee):
     def __init__(self,name,role,yoga_style):
      Employee.__init__(self,name,role)
      self.yoga_style=yoga_style
     
     def display(self):
        print("\nMy name is {}, my role is {} and my yoga_style is {}".format(self.name,self.role,self.yoga_style))
        
class MultiTrainer(Trainer,YogaInstructor):
     def __init__(self,name,role,specialization,yoga_style):
      Trainer.__init__(self,name,role,specialization)
      YogaInstructor.__init__(self,name,role,yoga_style)
      
     
     def display(self):
        print("\nMy name is {}, my role is {}, my specialization is {} and my yoga_style is {}".format(self.name,self.role,self.specialization,self.yoga_style))
        
        
e=Employee("Akhil","Staff")
t=Trainer("Poornima","Trainer","Weight Training")
yi=YogaInstructor("Raju","Yoga Instructor","Hatha Yoga")
mt=MultiTrainer("Arun","Trainer","Cardio","Vinyasa Yoga")
e.display()
t.display()
yi.display()
mt.display()
        
         
    
    