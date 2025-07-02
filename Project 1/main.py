import random 
"""
-1 for water
0 for gun
1 for snake 

"""

computer = random.choice([-1,0,1])
youstr = input("Enter your choice : ")
youDict = {"s": 1, "w": -1, "g": 0} 
reverseDict = {1: "Snake", 0: "Gun", -1: "Water"}

you = youDict[youstr]
# By now we have two numbers, "you and computer"

print(f"You chose {reverseDict[you]}\n Computer chose {reverseDict[computer]}")

if(computer == you):
    print("It's a draw")

else:
    if(computer == -1 and you == 1):
            print("You Win!")

    elif(computer == -1 and you == 0):
         print("You Loose!")

    elif(computer == 1 and you == -1):
         print("You Loose!")  

    elif(computer == 1 and you == 0):
         print("You Win!")  

    elif(computer == 0 and you == -1):
         print("You Win!") 

    elif(computer == 0 and you == 1):
         print("You Loose!")      

    else:
         print("Something went wrong!")     
