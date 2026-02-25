a = float(input("Please type number a: "))
action = input("Please type action symbol: ")
b = float(input("Please type number b: "))

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

if action == "+":
    print(add(a,b))
elif action == "-":
    print(subtract(a,b))
elif action == "*":
    print(multiply(a,b))
elif action == "/":
    if b == 0:
        print("Can't divide by zero")
    else:
        print(divide(a,b))
else:
    print("Wrong action symbol")