class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addition(self):
        return self.x + self.y
    def multiply(self):
        return self.x * self.y
    def divide(self):
        if self.y != 0:
            return("Value cannot be divided by zero!!")
        else:
            return self.x / self.y
    def subtract(self):
        return self.x - self.y

a = float(input("Enter the values of x: "))
b = float(input("Enter the value of y: "))

c = input("Operation: ")

calculator = Calculator(a, b)

add = calculator.addition()
mult = calculator.multiply()
div = calculator.divide()
sub = calculator.subtract()

#c = input("Operation: ")
if (c == add):
    print("The answer is: ", add)
elif (c == mult):
    print("The answer is: ", mult)
elif (c == div):
    print("The answer is: ", div)
elif (c == sub):
    print("The answer is: ", sub)

