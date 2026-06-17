class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        else:
            return a / b

calc = Calculator()

n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))

operation = input("Enter the operation: ")

if operation == "+":
    print(calc.add(n1, n2))

elif operation == "-":
    print(calc.subtract(n1, n2))

elif operation == "*":
    print(calc.multiply(n1, n2))

elif operation == "/":
    print(calc.divide(n1, n2))

else:
    print("Invalid operation")