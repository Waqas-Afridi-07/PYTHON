class Programmer:
    company = "Microsoft"
    def __init__(self, name, age, salary, pin):
        self.name = name
        self.age = age
        self.salary = salary
        self.pin = pin

s = Programmer("Shehzad", 40, 100000, 249001)
print(s.name, s.age, s.salary, s.pin, s.company)

r = Programmer("Rehan", 40, 200000, 245001)
print(r.name, r.age, r.salary, r.pin, r.company)

a = Programmer("Asim", 40, 300000, 243001)
print(a.name, a.age, a.salary, a.pin, a.company)