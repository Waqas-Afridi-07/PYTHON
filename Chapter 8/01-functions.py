# Functions are used to repeat a block of reusable code that performs a specific task
# We don't have to write the same block of code again and again

def avg():
    a = int(input("Enter the number : "))
    b = int(input("Enter the number : "))
    c = int(input("Enter the number : "))

    average = (a+b+c)/3
    print(average)

avg()
avg()
avg()