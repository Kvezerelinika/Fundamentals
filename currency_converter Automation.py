amount = input("what are we exchanging: e.g. TOTAL, AEXCH, BEXCH: ").split()

currencies = {
    "USD": 1.0,        # US Dollar
    "EUR": 0.92,       # Euro
    "GBP": 0.78,       # British Pound
    "JPY": 156.2,      # Japanese Yen
    "AUD": 1.62,       # Australian Dollar
    "CAD": 1.35,       # Canadian Dollar
    "CHF": 0.91,       # Swiss Franc
    "CNY": 6.95,       # Chinese Yuan
    "GEL": 2.68,       # Georgian Lari
    "TRY": 32.4,       # Turkish Lira
    "INR": 83.7,       # Indian Rupee
    "NZD": 1.72,       # New Zealand Dollar
    "SEK": 11.1,       # Swedish Krona
    "NOK": 11.7,       # Norwegian Krone
    "DKK": 6.9,        # Danish Krone
    "RUB": 108.2,      # Russian Ruble
    "SGD": 1.36,       # Singapore Dollar
    "HKD": 7.82,       # Hong Kong Dollar
    "MXN": 17.1,       # Mexican Peso
    "BRL": 5.0         # Brazilian Real
    }

if len(amount) != 3:
    print("ERROR INPUT MUST BE: Amount, From_Currency, To_Currency")

try:
    value = float(amount[0])
except ValueError:
    print("Amount must be number")
    exit()
    
fr_cur = amount[1].upper()
to_cur = amount[2].upper()

if fr_cur not in currencies or to_cur not in currencies:
    print("UNSUPPORTED CURRENCY CODE")
    exit()

usd_value = value / currencies[fr_cur]
converted = usd_value * currencies[to_cur]

print(f"{value} {fr_cur} = {converted:2.2f} {to_cur}")

