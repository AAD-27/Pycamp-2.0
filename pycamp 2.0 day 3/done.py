"""
Write a program that repeatedly reads numbers until the user enters “done”. Once “done” is
entered, print out the total, count, average of numbers and minimum & maximum. If the user enters
anything other than a number, detect their mistake using try and except and print an error message
and skip to the next numbers?
"""

count = 0
total = 0.0
largest = None
smallest = None

while True:
    number = input("Enter a no: ")
    if number == 'done':
        break
    try:
        no = float(number)
    except:
        print("Invalid Number")
        continue
    count = count + 1
    total = total + no 

    if largest is None:
        largest = no
        smallest = no

    if no>largest: 
        largest=no
    if no<smallest: 
        smallest=no

print ("Task Completed Successfully ")
print("\nTotal is ",total)
print("Count is ",count)
print("Average is: ",total/count)
print("Maximum & minimum nos are",largest," & ",smallest) 
