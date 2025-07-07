def isPrime(x):
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i = i + 1
    return True

x = int(input("Please enter a number: "))
if x <= 1:
    print("Not a prime number")
elif(x == 2):
    print("Not a prime number")

else:
    if isPrime(x):
       print(x, "is prime")
    else:
        print(x, "is not  a prime")
