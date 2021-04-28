class numbers:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.smallest = 0

    def Sum(self):
        return self.num1 + self.num2 + self.num3

    def Average(self):
        return self.Sum() / 3

    def Product(self):
        return self.num1 * self.num2 * self.num3

    def Smallest(self):
        self.smallest = self.num1
        if self.num2 < self.num1:
            self.smallest = self.num2
            if self.num3 < self.num2:
                self.smallest = self.num3


d1 = numbers(20, 10, 15)

print(d1.Sum())
print(d1.Product())
print(d1.Average())
print(d1.Smallest())
