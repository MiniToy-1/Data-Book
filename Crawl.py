import csv
from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# Define the URL you want to scrape
URL = 'https://www.fahasa.com/sach-trong-nuoc.html'

# Send an HTTP GET request to the URL
response = requests.get(URL, headers=headers)
if response.status_code == 200:
    Source = BeautifulSoup(response.content, 'html.parser')
print(Source)