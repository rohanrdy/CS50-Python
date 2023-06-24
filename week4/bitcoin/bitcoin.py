import json
import requests
import sys

if len(sys.argv) == 2:
    try:
        n = float(sys.argv[1]) # n number of bitcons
    except ValueError:
        sys.exit("Command-line argument is not a number")
else:
    sys.exit("Missing command-line argument")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    sys.exit("There was an exception while handling the api request")

response_json = response.json()

a = response_json["bpi"]
b = a["USD"]
c = b["rate_float"]

print(f"${c*n:,.4f}") # to print with commas at thousands and upto 4 decimal places