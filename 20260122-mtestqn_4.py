class Calculator:
    def add(self,x,y):
        return x+y
    def sub(self,x,y):
        return x-y
    def mul(self,x,y):
        return x*y
    def div(self,x,y):
        return x/y 
x=int(input("Enter the first number"))
y=int(input("Enter the second number"))        
calc=Calculator()        
print("Addition:",calc.add(x,y))
print("Subtraction:",calc.sub(x,y))
print("Multiplication:",calc.mul(x,y))
print("Division:",calc.div(x,y))