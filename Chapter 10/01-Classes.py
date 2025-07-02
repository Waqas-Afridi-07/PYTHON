class Employee:
    salary = 1200000 # class attributes
    language = "Python"

waqas = Employee()
waqas.name = "Waqas" # object or (instance) attribute 
print(waqas.name, waqas.salary, waqas.language)

rohan = Employee() # Creating a new Employee
rohan.name = "Rohan" # Giving name to employees
print(rohan.name, rohan.salary, rohan.language)