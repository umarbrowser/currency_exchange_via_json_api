import requests
import json


bases = ["USD", "RON", "EUR"]
string_for_each_header_currency = ""
string_for_each_currency = ""
text_file = open("mailText.txt", "w")

for base in bases:
    url = "http://api.fixer.io/latest?base=" + base
    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)
    rates = parsed["rates"]

    text_file.write("\n--------------- Rates in " + base + "---------------\n")
    text_file.write(string_for_each_header_currency)
    for currency, rate in rates.items():
        text_file.write(currency + " = " + base + " " + str(rate) + ", ")




#totalString = string_for_each_header_currency + string_for_each_currency

text_file.close()