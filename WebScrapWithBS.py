# Web Scraping with BeautifulSoup
import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extracting and printing page title
title = soup.title.string
print(f"Page Title: {title}")