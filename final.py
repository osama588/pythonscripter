import requests
from bs4 import BeautifulSoup
import csv
import json
import time
from random import randint


def scrape_real_estate_data(location):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
        # Add any other necessary headers to mimic a browser request
    }

    base_url = f'https://www.zameen.com/Homes/Karachi-2-1.html' 

    try:
        response = requests.get(base_url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find elements containing property information
            property_listings = soup.find_all('div', class_='_6ccdaada')  # Update this according to the website structure

            # Store data in a list of dictionaries
            data = []
            for listing in property_listings:
                # property_title = listing.find('h2', class_='').text.strip()  # Update according to website structure
                property_price = listing.find('span', class_='c4fc20ba').text.strip()  # Update according to website structure
                # property_url = listing.find('a')['href']  # Update according to website structure

                property_data = {
                    # 'Title': property_title,
                    'Price': property_price,
                    # 'URL': property_url
                }
                data.append(property_data)

            return data

        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None

    except Exception as e:
        print(f"Error: {str(e)}")
        return None

# Function to save data to a CSV file
def save_to_csv(data):
    filename = 'real_estate_data.csv'
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Title', 'Price', 'URL']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

# Function to save data to a JSON file
def save_to_json(data):
    filename = 'real_estate_data.json'
    with open(filename, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4)

# Main function
def main():
    location = 'your-location'  # Replace with the desired location or zip code
    real_estate_data = scrape_real_estate_data(location)

    if real_estate_data:
        save_to_csv(real_estate_data)
        save_to_json(real_estate_data)
        print("Data scraped and saved successfully!")
    else:
        print("Failed to scrape data.")

if __name__ == "__main__":
    main()
