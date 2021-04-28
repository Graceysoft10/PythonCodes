smallest = 0
num1 = 20
num2 = 10
num3 = 30

smallest = num1
if num2 < num1:
    smallest = num2
    if num3 < num2:
        smallest = num3

print(smallest)