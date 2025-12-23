import requests

amount = input("what are we exchanging: e.g. TOTAL, AEXCH, BEXCH: ").split()

access_key = "445d3b0b9e44659a9d07b2eea208b4cb"
value = amount[0]
from_cur = amount[1].upper()
to_cur = amount[2].upper()

url = f"http://api.currencylayer.com/convert?access_key={access_key}&from={from_cur}&to={to_cur}&amount={value}"
response = requests.get(url).json()

if response["success"]:
    converted = response["result"]
    print(f"{value} {from_cur} = {converted:.2f} {to_cur}")
else:
    print("Error fetching conversion rate")