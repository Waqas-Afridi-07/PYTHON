# Arithmetic operators: They are +, -, /, * etc. Perform mathematical calculations
a = 34
b = 58
print(a+b)
print(a-b)
print(a*b)
print(a/b)

# Assignment operators: Used to assign values. They are =, +=, -=, *=, /= etc.
a = 21-5 # = means assign a to 17.
b = 6
b +=3 # means add or increment 3 to the value of b.
print(a)
print(b)

b = 6
b -=3 # means subtract or decrement to the value of b.
print(b)

b = 6
b *=3 # means multiply 3 with the value of b.
print(b)

b = 6
b /=3 # means divide 3 with the value of b.
print(b)

# Comparison operators: They are used to compare two values and their return value is always boolean 
                        # They are equal to (==), not equal to (!=), greater (>), greater and equal to (>=),
                        # less than (<), less than and equal to (<=) etc.
# For example:- 
5 == 5 # equal to
5 != 4 # not equal to 
5 > 2 # greater than
5 >= 5 # greater than and equal to
5 < 8 #  less than
5 <= 5 # less than and equal to 

# Logical operators: They are used for combining conditions. They're "and" (returns true if both are true)
                                                                # "or" (returns true if at least one is true) 
                                                                #  "not" (it reverse the condition

# Truth table of "and" 
print("True and False is", True and False)
print("True and True is", True and True)
print("False and True is", False and True)
print("False and False is", False and False) 

# Truth table of "or" 
print("True or False is", True or False)
print("True or True is", True or True)
print("False or True is", False or True)
print("False or False is", False or False) 

# Truth table of "not" 
print(not(False))
print(not(True))