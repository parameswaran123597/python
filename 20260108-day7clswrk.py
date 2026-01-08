items=["milk","bread","eggs"]
def add_item(item):
    items.append(item)
    print (items)
    
def remove_last_item():
   print(items.pop())
   print(items)
   
lfunc=lambda item:print("items:", item)

def count_characters(items):
    if not items:
        return 0
    return len(items[0])+count_characters(items[1:])
   
   
add_item("biscuit")        
remove_last_item()       
for item in items:
   lfunc(item) 
print("Total characters =", count_characters(items))    
            