# num = 1234
# first = int(x) for x in str(num)
# print(first)
# num / 1000
# num2 = first % 1000
# second = num2 / 100
# print(first, second)
# f
userInput = 3456
firstDigit = userInput / 1000
userInput2 = userInput % 1000
secondDigit = userInput2 / 100
userInput3 = userInput2 % 100
thirdDigit = userInput3 / 10

userInput4 = userInput3 % 10
fourthDigit = userInput4 / 1

print(firstDigit, " ", secondDigit, " ", thirdDigit, " ", fourthDigit)
