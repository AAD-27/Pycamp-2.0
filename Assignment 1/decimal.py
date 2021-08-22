"""
 Write a program to count the number of digits before and after decimal point in the entered floating point number. 
 Take atleast 4 decimal point floating number as input from user.
"""

num = input('Enter a Floating-point number: ')
str = num.split('.')
print('Number of digits before decimal point:', len(str[0]))
print('Number of digits after decimal point:', len(str[1]))