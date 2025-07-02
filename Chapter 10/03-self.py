class Employee:
    salary = 1200000
    language = "Python"

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary} ")

    def greet(self):
        print("Good morning ")

waqas = Employee()
# waqas.language = "JavaScript"  
waqas.getInfo()
waqas.greet()
# Employee.getInfo(harry)