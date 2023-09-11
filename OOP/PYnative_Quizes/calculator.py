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
            return self.x / self.y
        else:
            print("Error!!!")
    def subtract(self):
        return self.x - self.y

a = float(input("Enter the values of x: "))
c = input("Enter operation: ")
b = float(input("Enter the value of y: "))

#c = input("Operation: ")

calculator = Calculator(a, b)
if c == str("+"):
    print("The answer = ", calculator.addition())
elif c == str("*"):
    print("The answer = ", calculator.multiply())
elif c == str("/"):
    print("The answer = ", calculator.divide())
elif c == str("-"):
    print("THe answer = ", calculator.subtract())

else:
    raise TypeError("That is a non recognisable operand!!") 


#if c == str(add):
#print("The answer is: ", add)
#elif c == str(mult):
#   print("The answer is: ", mult)
#elif c == str(div):
#    print("The answer is: ", div)
#elif c == str(sub):
#    print("The answer is: ", sub)

