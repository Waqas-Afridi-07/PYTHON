# Single Inheritance: When child class inherits only a single parent class
class Employee:
    company = "ITC"
    name = "Default name"

    def show(self):
        print(f"The name is {self.name} and the language is not defined here.")


class Coder:
    language = "Python"

    def printLanguages(self):
        print(f"Out of all the languages, here is your language: {self.language}")


# Multiple Inheritance: When a child class inherits from more than one parent class


class Programmer(Employee, Coder):
    company = "ITC Infotech"

    def show(self):
        print(f"The company is {self.company} and the language is {self.language}")


# Multilevel Inheritance: When a child class becomes a parent for another child class


class SeniorProgrammer(Programmer):
    def codeReview(self):
        print(f"{self.name} is reviewing code written in {self.language}")


a = Employee()
b = Programmer()
c = SeniorProgrammer()

print("\nProgrammer object:")
b.show()             
b.printLanguages()    

print("\nSeniorProgrammer object:")
c.name = "Zia"
c.show()            
c.printLanguages()    
c.codeReview()        
