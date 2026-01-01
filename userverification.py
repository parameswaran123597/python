has_account=True
email_verified=False
can_login=has_account and email_verified
print("User can log in?", can_login)
email="paramu2001@gmail.com"
is_email_valid=('@' in email)
print("Is email valid?", is_email_valid)
user_age=17
is_age_valid=(user_age>=18)
print("Is user can login based on age?", is_age_valid)
can_login_final=has_account and email_verified and is_email_valid and is_age_valid
print("Final login status:", can_login_final)
result=True
print("Result is =",has_account is result)