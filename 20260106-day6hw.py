blog_views=[150,800,2500,600,1200,450,3000]
i=0
total_views=0
for views in blog_views:
    if views>1000:
        print("Trending")
        i=i+1
    elif (views>=500 and views<=1000):
        print("Average")
    else:
        print("Low Traffic")
    total_views=total_views+views
print("Total number of views is :",total_views)
print("Total number of Trending posts is :",i)


       
        
        
        
        
            