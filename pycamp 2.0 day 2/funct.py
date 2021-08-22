"""
Defining a function, calling a function 
"""

# def function1(a,b,c):             #Defining a function
#     return a,b,c

# print(function1(1,2,3))

"""
Define a function which passes multiple arguments as an input and returns multiple values as result

"""

m = int(input("Enter length:     "))
n = int(input("Enter breadth:    "))

def rect(l,b):
    area = l * b
    return area

#print(rect(m,n))
print("Area of rectangle is:    ",rect(m,n))

"""
3.4 Define a function which passes list as an input

"""
 

def job_details(list_1):                              #defining the function with list_1 as parameter
  print("My details are:  \n")

  for x in list_1:                                #for loop for printing every element
    print(x, end= " " )                           #end is used here to combine the elements in same line 
list_1 = [ 'Ameya','Dikshit', 'LFC', 2.0 ]        #Entering details of students

job_details(list_1)                                   #calling the function

