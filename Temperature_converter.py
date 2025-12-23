amount = input("Please, Enter temperature and unit: ").split()

if len(amount) != 2:
    print("Input is lacking the component")
    exit()

try:
    value = float(amount[0])
except ValueError:
    print("Amount should be number")
    exit()

unit = amount[1].upper()

if unit == "C":
    f = (value * 9 / 5) + 32
    print(f"{value} {unit} = {f:.2f} F")
elif unit == "F":
    c = (value - 32) * 5/9
    print(f"{value} {unit} = {c:.2f} C")
else:
    print("Unknown variable")
