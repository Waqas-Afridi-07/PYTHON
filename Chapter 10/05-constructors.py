class Employee:
    salary = 1200000
    language = "Python"

    def __init__(self, name, salary, language): # dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        
        print("I am creating an object")


    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary} ")

    @staticmethod
    def greet():
        print("Good morning ")

waqas = Employee("Waqas", 1300000, "JavaScript")
# waqas.name = "Waqas"
print(waqas.name, waqas.salary, waqas.language)

# rehan = Employee()