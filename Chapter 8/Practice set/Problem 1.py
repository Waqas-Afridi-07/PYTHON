
def greatest():
    n1 = int(input("Enter the number : "))
    n2 = int(input("Enter the number : "))
    n3 = int(input("Enter the number : "))

    if(n1>n2 and n1>n3):
        print("The greatest number is n1 : ", n1)

    elif(n2>n1 and n2>n3):
        print("The greatest number is n2 : ", n2)


    elif(n3>n1 and n3>n2):
        print("The greatest number is n3 : ", n3)

greatest()