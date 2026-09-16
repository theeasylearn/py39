import requests

url = "https://www.swamigurukul.com/"

response = requests.get(url)

print(response)
print(response.status_code)
print(response.text)