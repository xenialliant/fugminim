import requests

url = 'https://example.com/api'
data = {'key': 'value'}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    print(response.json())
else:
    print(response.text)
