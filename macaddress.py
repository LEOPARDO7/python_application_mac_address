
import requests

value = [] 
n = int(input('Enter how many MAC address you want to query\n'))
print('Enter your MAC Address')

for i in range(0, n):
  b = input()
  value.append(b)

MAC_URL = 'https://api.macaddress.io/v1?apiKey=API_TOKEN&output=json&search=%s'
for i in range(0, n):
  try:
    r = requests.get(MAC_URL % value[i])
    a = r.json()
    print('Company Name:', a['vendorDetails']['companyName'], value[i])
  except KeyError as e:
    print('Check you MAC address properly', value[i])

