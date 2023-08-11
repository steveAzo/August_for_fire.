def triangular(n):
    if n <= 0:
        return 0
    else:
        return n * (n + 1) // 2
n = int(input("Enter a number to be return it's triangular number or not."))
print(triangular(n))