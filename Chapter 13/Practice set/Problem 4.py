def divisible5(n):
    if (n%5 == 0):
        return True
    return False

a = [1,5,65,70,7574,75,883747348]

f = list(filter(divisible5, a))
print(f)