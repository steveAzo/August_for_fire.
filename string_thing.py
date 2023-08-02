def thing(n):
    result = ""
    for i in range(n):
        result += '1' if i % 2 == 0 else '0'
    return result

n = int(input("What number do you wanna generate the altenating 0s and 1s ?"))
print(thing(n))