"""
Lists are Mutuable
List = []
"""

shopping_list = ["Mobile","Jeans","Grocery","Food from dominos"]
print(shopping_list) 

mixed_list = ["Hello","World",True,2.0]
print(mixed_list[2])                    #First position is always in all programming languages

#Nested list                            #List inside list
nlist = [[ True , [16] ] , 27 , ['Ameya'  , 9.82]]
print(nlist)

# retrieve value from list 
print(nlist[0][1]) 
print(nlist[2][1])
print(nlist[1])

numbers = [2,1,3,23,1]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

numbers.append(15)              #Adds value in the end
print(numbers)
print(numbers[-2])              #Negative indexing last element of the list
print(numbers[1:4])             #Slicing of list

mixed_list = ["Hello","World",15,True,2.0]
mixed_list[1] = "Python"        #To replace item 
print(mixed_list)
print(mixed_list[:2])
mixed_list.insert(2,15)         #2 indicates index position and 15 is the value
print(mixed_list)

del mixed_list[2]
print(mixed_list)

 