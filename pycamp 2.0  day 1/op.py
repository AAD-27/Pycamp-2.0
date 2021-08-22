"""
In python we 7 different types of operator 
1. Arithmetic Operators
2. Comparison (Relational) Operators
3. Assignment Operators
4. Logical Operators
5. Bitwise Operators
6. Membership Operators
7. Identity Operators

https://www.geeksforgeeks.org/python-operators/
"""

print("7+9 = ",7+9)     #Addition
print("7-9 = ",7-9)     #Substraction
print("7*9 = ",7*9)     #Multiplication
print("7/9 = ",7/9)     #Division
print("17//9 = ",17//9) #Quotient alaways a integer
print("7**2 = ",7**2)   #Power
print("17%9 = ",17%9)   #Remainder alaways a integer

#Comparison (Relational) Operators

#There are 6 types of comparison operators < > == != >= <=
#Returns True or False as their output

i = 10
j = 15
print(i == j)
print(i<j)
print(i<=j)

#Logical operators are covered under Boolean section

#Assisgnment Operator
x = 10
print(x)

x += 5                  #x = x + 5
print(x) 

x -= 5                  #x = x - 5
print(x) 

x *= 5                  #x = x * 5
print(x) 

x %= 5                  #x = x % 5
print(x) 
#There are 11 types of assignment operators: = += -= *= /= //= **= &= != ^= >>= <<= 

#Membership operator
#in not in

list1 = [1,2,3,4]
print(1 in list1)
print(10 in list1)

#Identity
a = 100
b = 50
print(a is not b)
print(a is b)