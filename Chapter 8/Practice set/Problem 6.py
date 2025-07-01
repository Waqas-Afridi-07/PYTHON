def pattern (n):
    if(n==0):
        return 
    print("*" * n)
    pattern(n-1)

p = int(input("Enter number for pattern : "))
pattern(p)