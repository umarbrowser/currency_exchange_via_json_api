import requests
import json

url = "http://api.fixer.io/latest?base=USD"

response = requests.get(url)
data = response.text
parsed = json.loads(data)
date = parsed["date"]
print("Date:", date, "\n")

rates = parsed["rates"]

for currency, rate in rates.items():
    print(currency, "= USD", rate)