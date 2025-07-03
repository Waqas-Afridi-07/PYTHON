class Demo:
    a = 4

o = Demo()
print(o.a) # Prints the class attribute
o.a = 0 # Instance attribute is set
print(o.a) # Prints the instance attribute because it is present
print(Demo.a) # prints the class attribute