"""
Rock paper scissor game using conditional statements
"""
#1. Without using Random function
print("--------------------------------------------------------")
computer = "paper"

 
user = input(" Please your choice ---rock paper scissor:")

print("\n Computer Chose:   ",computer)
print(" User Chose: ",user)

print("\n",computer,"V/s",user)

if computer == user:
    print(" Match Tied 😅")

elif computer == "rock" and user == "paper":
    print("\n You Win😁")
elif computer == "paper" and user == "scissor":
    print("\n You Win😁")
elif computer == "scissor" and user == "rock":
    print("\n You Win😁")

else:
    print("\n\n You lose😭")

print("--------------------------------------------------------")


#2. Using Random function
print("--------------------------------------------------------")
import random
computer = random.choice(['rock','paper','scissor'])

 
user = input(" Please your choice ---rock paper scissor:")

print("\n Computer Chose:   ",computer)
print(" User Chose: ",user)

print("\n",computer,"V/s",user)

if computer == user:
    print(" Match Tied 😅")

elif computer == "rock" and user == "paper":
    print("\n You Win😁")
elif computer == "paper" and user == "scissor":
    print("\n You Win😁")
elif computer == "scissor" and user == "rock":
    print("\n You Win😁")

else:
    print("\n\n You lose😭")

print("--------------------------------------------------------")
