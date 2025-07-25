class Employee:
    a = 1

    @classmethod # Bound to the class not the object
    def show(cls):
        print(f"The class attribute of a is {cls.a}")


    @property
    def name(self):
     return f"{self.fname} {self.lname}"

    @name.setter
    def name(self, value):
       self.fname = value.split(" ")[0]
       self.lname = value.split(" ")[1]


e = Employee()
e.a = 45

e.name = "Harry khan"
print(e.fname, e.lname)

e.show()