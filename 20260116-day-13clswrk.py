item = input("Enter the name of the new item: ")
f = open("items.txt", "a")
f.write(item + "\n")
f.close()
f = open("items.txt", "r")
print("List of items:")
print(f.read())

    