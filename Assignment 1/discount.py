"""
Write a program to take input from user for shopping amount. For amount, greater than
1000 shopkeeper gives 10 percent discount and for amount below 1000 he gives 5 percent
discount. Write a program to display percent of discount and amount of discount applicable.
"""
 
n = int(input("Please enter the total amount: "))
if n> 1000:
    print("\n\nCongratulations you got 10% Discount")
    discount = 0.1 * n
    total = n - discount

else:
    print("\n\nCongratulations you got 5% Discount")
    discount = 0.05 * n
    total = n - discount

print("\nYour Final price after discount is ",total)
