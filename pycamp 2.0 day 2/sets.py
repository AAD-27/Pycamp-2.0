"""
Sets is an collection of unordered elements
{}
"""
list1 = [2,4,2,3,5]
print("Original list:   ",list1)
set1 = set(list1)
print(set1)
set1 = {2,4,2,3,5}
set2 = {11,3,21,2}
print(set1 | set2)          #Prints the union of two sets
print(set1 & set2)          #Prints the intersection of two sets
print(set1 ^ set2)          #Prints elements which are not common