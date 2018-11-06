def is_prime(x):
    prime = False
    for a in range(x):
        test = a+1
        if test == 1:
            continue
        if test == x:
            continue
        if x % test == 0:
            prime = False
            break
        else:
            prime = True
    return prime

print (is_prime(int(input("Enter a number: "))))