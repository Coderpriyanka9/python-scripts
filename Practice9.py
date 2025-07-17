first_num = int(input("Enter first number: "))
second_num = int(input("Enter second  number: "))
operator = input("Enter operator: ")
if operator == '+':
    print(first_num + second_num)
elif operator == '-':
    print(first_num - second_num)
elif operator == '*':
    print(first_num * second_num)
elif operator == '/':
    print(first_num / second_num)
elif operator == '%':
    print(first_num % second_num)
else:
    print("Invalid try")

