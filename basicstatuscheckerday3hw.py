is_logged_in=True
print("Is user logged in?", is_logged_in)
is_subscribed=False
print("Is user subscribed?", is_subscribed)
user_credits=100
max_credits=200
min_credits=50
credits_valid=(user_credits>=min_credits) and (user_credits<=max_credits) and (user_credits!=min_credits)
print("Are user credits valid?", credits_valid)
bonus_eligible=(is_subscribed or (user_credits>min_credits))
print("Is user eligible for bonus?", bonus_eligible)
user_credits+=50
print("User credits after addition:", user_credits)
user_credits-=20
print("User credits after deduction:", user_credits)
user_credits*=2
print("User credits after multiplication:", user_credits)
user_credits%=150
print("User credits after modulus operation:", user_credits)
power_result=user_credits**2
print("User credits raised to power 2:", power_result)
full_access=is_logged_in and is_subscribed
print("Does user have full access?", full_access)
result=True
is_true_login=(is_logged_in is result)
print("Result is =",is_true_login)
access_result = is_logged_in or is_subscribed and False
print("Access result is =", access_result)