rice_price=45
sugar_price=40
oil_price=130

rice_qn=3
sugar_qn=2.5
oil_qn=1.8

total_cost_sugar=sugar_price*sugar_qn
total_cost_rice=rice_price*rice_qn
total_cost_oil=oil_price*oil_qn
print("Total cost of sugar is ",total_cost_sugar)
print("Total cost of rice is ",total_cost_rice)
print("Total cost of oil is ",total_cost_oil)

total_bill=total_cost_sugar+total_cost_rice+total_cost_oil
print("Total grocery bill is ",total_bill)

print("Total grocery bill after converting to integer is ",int(total_bill))
print("Total grocery bill after converting to string is ",str(total_bill))
import random
print(random.randrange(5,10)+total_bill)