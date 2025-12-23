amount = input("what are we exchanging: e.g. TOTAL, AEXCH, BEXCH: ").split()

gel_to_usd = 0.37
usd_to_gel = 2.68 

curr1 = "GEL"
curr2 = "USD"

if len(amount) != 3:
    print("ERROR INPUT MUST BE: Amount, From_Currency, To_Currency")

try:
    value = float(amount[0])
except ValueError:
    print("Amount must be number")
    exit()
    
fr_cur = amount[1].upper()
to_cur = amount[2].upper()

if fr_cur == curr1 and to_cur == curr2:
    print(value * gel_to_usd)
elif fr_cur == curr2 and to_cur == curr1:
    print(value * usd_to_gel)
else:
    print("The currency code is not correct")

