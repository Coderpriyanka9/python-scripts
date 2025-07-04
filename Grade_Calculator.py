x = input("enter your marks: ")
x = float(x)
if x > 90:
    print("Excellent you got grade A++")
elif x > 80 :
    print("Very good you got grade A+")
elif x > 70:
    print("Good you got grade A")
elif x > 60:
    print("You got grade B+")
elif x > 50:
    print("You got grade B")
elif x > 40:
    print("You got grade C")
elif x > 35:
    print("You got grade D")
else:
    print("You Failed!")
