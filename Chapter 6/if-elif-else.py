# They are multiway decision taken by our program due to certain conditions in our code.

a = int(input("Enter your age : "))

if(a>=18):
    print("You are above the age of consent")

elif(a<0):
    print("You are entering an invalid age")

elif(a==0):
    print("You are entering an invalid age")    

else:
    print("You are below the age of consent")


print("End")    