import requests
import json

url_for_usd_to_ron = "http://api.fixer.io/latest?symbols=USD,RON"
response = requests.get(url_for_usd_to_ron)
data = response.text
parsed = json.loads(data)
date = parsed["date"]
usd_rate = parsed["rates"]["USD"]
ron_rate = parsed["rates"]["RON"]
print("On " + date + " RON equals " + str(ron_rate) + " RON")
print("On " + date + " USD equals " + str(usd_rate) + " USD")
