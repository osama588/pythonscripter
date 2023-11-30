import requests
from bs4 import BeautifulSoup
import csv
import json

base_url = 'https://www.zameen.com/Homes/Karachi-2-1.html'  # Replace with the website URL you want to scrape
response = requests.get(base_url)
response = response.content
soup = BeautifulSoup(response, 'html.parser')
