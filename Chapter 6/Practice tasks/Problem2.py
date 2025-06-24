marks1 = float(input("Enter marks of first subject : "))
marks2 = float(input("Enter marks of second subject : "))
marks3 = float(input("Enter marks of third subject : "))

total_percentage = (100*(marks1 + marks2 + marks3))/300

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("Congrats, You are passed")
    print("Percentage :", total_percentage)

else:
    print("oh, You failed, better luck next time") 
    print(total_percentage)   
