class Employee:
    salary = 1200000
    language = "Python"

waqas = Employee()
waqas.language = "JavaScript" # object or (instance) attributes takes preference over class attributes. 
print(waqas.language, waqas.salary)