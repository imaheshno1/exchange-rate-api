import requests

api_key = "fe0d14f72ba89c5ae3cd2279"

# Where USD is the base currency you want to use
url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/USD'

# Making our request
response = requests.get(url)
data = response.json()

# Your JSON object
print(data)
# return the desired country value
inr_rate = data['conversion_rates']['INR']
print("Indian exchange value against USD⇒", inr_rate)

with open('exchange_rate.json', 'w') as file:
    file.write(f"USD to INR exchange rate: {data}")
print("INR exchange rate saved to exchange_rate.json")
