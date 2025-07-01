def find_sum():
    n = int(input("Enter the number : "))
    total = 0
    i = 1
    while(i<=n):
        total += i
        i += 1
    print("The sum is : ", total)

find_sum()