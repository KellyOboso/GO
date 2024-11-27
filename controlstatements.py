temperature = 45

if temperature > 25:
    print("It is too hot")
else:
    print("It is too cold")
if temperature == 25:
    print("Temperature is at normal")

#A python program that checks three numbers and returns the smallest number
num1 = 78
num2 = 15
num3 = 90

if num1 < num2 and num1 < num3:
    print(num1,"is the smallest number")
elif num2<num1 and num2<num3:
    print(num2,"is the smallest number")

else:
    print(num3,"is the smallest number")

#A python program that checks three numbers and returns the largest number
x = 45
y = 21
z = 69

if x > y and x > z:
    print(x, "is the greatest number")
elif y > x and y > z:
    print(y, "is the greatest number")
else:
    print(z, "is the greatest number")
