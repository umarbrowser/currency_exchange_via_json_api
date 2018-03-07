import requests
import json


bases = ["USD", "RON", "EUR"]
string_for_each_header_currency = ""
string_for_each_currency = ""
for base in bases:
    url = "http://api.fixer.io/latest?base=" + base
    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)
    rates = parsed["rates"]

    string_for_each_header_currency += "--------------- Rates in" +  base + "---------------"
    for currency, rate in rates.items():
        s = str("=")
        string_for_each_currency += currency + s + base + str(rate)

