var1 = "Hello"
var2 = "Ameya"
print(var1,var2)        #To print 2 or more variables together type comma after the end of each variable
print(var1+var2)        #+ concatenates(merge) the 2 variables so they together form a single word
var3 = 27
var4 = 2.0

print(type(var1))
print(type(var3))
print(type(var4))

c = 1 + 2j
print(type(c))

#---------------------------------
# Boolean values are True and False
value1 = True
value2 = False
print(value1, value2)

# Logical NOT
print("Logical NOT")            #NOT: complements the value
print("===========")
print(not value1)
print(not value2)


# Logical AND
print("Logical AND")            #AND returns True if both values are True
print("===========")
print(value1 and value1)
print(value1 and value2)
print(value2 and value2)

# Logical OR
print("Logical OR")             #OR reuturns True if any of the value is True
print("==========")
print(value1 or value1)
print(value1 or value2)
print(value2 or value2)
