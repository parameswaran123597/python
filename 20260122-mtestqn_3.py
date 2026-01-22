arr=[{"id":1,"name":"rajesh"},{"id":2,"name":"rahul"},{"id":3,"name":"sruthi"}]
user_input=int(input("Enter the id"))
for x in arr:
    if user_input==x["id"]:
        print(x["name"])
        break
else:
    print("Student not found")