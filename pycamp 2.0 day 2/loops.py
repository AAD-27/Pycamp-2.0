"""
In python we have two types loop -- for loop and while loop 
"""

l1 = [1,2,3,4,5]                                 #a random list
a = 0
for a in l1:
    print("Elemnts in list are: ",a)

for i in range(4):
    print("Hello World")
    print(i)

count = 0
while count < 3:
    print("Hello World")
    count = count + 1
    print(count)
print("While loop completed")

i = 1
while i < 6:
    print(i)
    if (i == 3):
        break
    i += 1                  #i = i + 1