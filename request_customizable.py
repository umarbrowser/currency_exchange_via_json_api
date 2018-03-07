import requests
import json

bases = ["USD", "RON", "EUR"]

for base in bases:
    url = "http://api.fixer.io/latest?base=" + base

    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)

    rates = parsed["rates"]

    print("--------------- Rates in", base, "---------------")
    for currency, rate in rates.items():
        print(currency, "=", base, rate)