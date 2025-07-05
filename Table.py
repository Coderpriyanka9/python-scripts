x = input("Please enter a number: ")
x = int(x)
i = 1
for i in range(11):
    if i == 0:
        continue
    print(x * i)