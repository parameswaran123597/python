Python={"aryan","arunima","rajesh"}
print(Python)
Data_Science={"poornima","anoop","saroj","aryan"}
print(Data_Science)
Python.add("Sam")
print(Python)
Data_Science.remove("anoop")
print(Data_Science)
print(Python & Data_Science)
print(Python - Data_Science)
print(Python | Data_Science)
course={
    "Python":len(Python),
    "Data_Science":len(Data_Science)
}
print(course)
for x, y in course.items():
  print("course:",x,"No_Students:", y)
  new_dict={course:student*2 for course, student in course.items()}
print(new_dict)


    