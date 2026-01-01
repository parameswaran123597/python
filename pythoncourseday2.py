python=""" Hii all python learners!,
Welcome to Python course
We are excited to have you join us for a day filled with learning and fun activities\n"""
print(python.lower())
print(len(python))
print((python[0]).lower())
print(python[-2])
print((python[0:51]).lower())
print(python.replace("Python","PYTHON"))
print(python.strip())
print(python.split(" "))
bool="course" in python
print(bool,"\nyes, 'course' is present in the string")
final_msg="The course description is {} characters long and has {} words."
print(final_msg.format(len(python),len(python.split())))