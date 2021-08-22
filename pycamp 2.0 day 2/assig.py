a=input("Enter a number: ")
b=[]
while a!="done":
    try:
        b.append(int(a))
    except:
        print("error occured .../nplease enter a valid number")    
    a=input("Enter a number: ")
print("Total: ",sum(b))
print("Count: ",len(b))    
print("Maximum: ",max(b))
print("Minimum: ",min(b))

 