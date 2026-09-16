import requests

url = "https://www.swamigurukul.com/"

response = requests.get(url)

from bs4 import BeautifulSoup

# Create BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser")
print(soup.title.text)
print(soup.h2.text)