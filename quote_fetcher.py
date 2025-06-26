import waveassist
import requests

waveassist.init()

response = requests.get('https://zenquotes.io/api/random')
response.raise_for_status()

quote_data = response.json()
print("Fetched Quote Data:", quote_data)
waveassist.store_data('quote_data', quote_data)
