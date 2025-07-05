try:
    a = int(input("Hey, Enter a number : "))
    print(a)

except Exception as e:
    print(e)

else:
    print("I am inside else") # It will only enter else when "try" executes successfully
                                # otherwise it will show error