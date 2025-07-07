numbers = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8, 9 , 10]
even = []
odd = []
for num in numbers:
    if num % 2 == 0:
        even.append(num)
print(even)
for num in numbers:
    if num % 2 == 1:
        odd.append(num)
print(odd)