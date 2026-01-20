import random
import math
customer=input("Names of customers are:")
names_list = [name.strip() for name in customer.split(",")]
unique_names = list(set(names_list))
rand=random.shuffle(unique_names)
winners = random.sample(unique_names, 2)
reversed_winners = [winner[::-1] for winner in winners]
print("\n🎉 Lucky Draw Winners (Reversed Names):")
for winner in reversed_winners:
    print(winner)
count=len(unique_names)
print("Total number of participants=: ", count)
print(round(math.sqrt(count)))
    