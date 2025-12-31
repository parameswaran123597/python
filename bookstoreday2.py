head="""Hi,
Welcome to Book Store Day! 
We are excited to have you join us for a day filled with great books and special events.\n"""
print(head.upper())
Book_title1="Python Basics"
Book_title1_price=450
Book_title2="Data Science Intro"
Book_title2_price=600
format_op="The price for the book1 '{}' is {} INR and book2 '{}' is {} INR.\n"
print(format_op.format(Book_title1,Book_title1_price,Book_title2,Book_title2_price).upper())
total_price=Book_title1_price+Book_title2_price
print(("Total price for both books is "+str(total_price)).upper())
str1="\nthank-you\t"
str2="Visit Again!"
print((str1+" "+str2).upper())