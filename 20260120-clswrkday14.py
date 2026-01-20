import random
import math
guest=input("Names of invited guests are:")
names_list = [name.strip() for name in guest.split(",")]
unique_names = list(set(names_list))
print("Unique names:", unique_names)
rand=random.choice(unique_names)
print("Random element from list:", rand)
reversed_name=rand[::-1]
print("Reversed name is: ", reversed_name)
count=len(unique_names)
print("Total number of unique names =: ", count)
print(round(math.sqrt(count)))
    