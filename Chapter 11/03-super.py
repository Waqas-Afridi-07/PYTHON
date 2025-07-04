class Employee:
    def __init__(self):
        print("Constructor of the employee")
    a = 1


class Programmer(Employee):
    def __init__(self):
        print("Constructor of the programmer")
    b = 2


class Manager(Programmer):
    def __init__(self):
        super().__init__() # used to call a method from the parent class (also called the base class)
        print("Constructor of the manager")
    c = 3

# o = Employee()
# print(o.a) # prints the a attribute

# o = Programmer()
# print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)