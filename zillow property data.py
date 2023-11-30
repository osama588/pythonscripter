import requests
from bs4 import BeautifulSoup
import csv
import json

def scrape_zameen(location):
    # Define the URL with the specified location
    base_url = f"https://www.zameen.com/{location}"

    # Set up the User-Agent string
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
    }

    # Print the headers for verification
    print("Headers:", headers)

    # Send a GET request to the URL with the specified User-Agent header
    response = requests.get(base_url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using Beautiful Soup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find elements containing property information
        property_listings = soup.find_all('div', class_='_126656cb')  # Update class name as per Zameen's structure

        # Create lists to store extracted data
        # titles = []
        prices = []
        # urls = []

        # Extract required information for each property listing
        for listing in property_listings:
            # Extract property title
            # title = listing.find('h2', class_='title').text.strip()  # Update class name as per Zameen's structure
            # titles.append(title)

    
            price = listing.find('span', class_='price').text.strip()  # Update class name as per Zameen's structure
            prices.append(price)

            # Extract property URL
            # property_url = listing.find('a', class_='link-block')['href']  # Update class name as per Zameen's structure
            # urls.append(property_url)

        # Store the extracted data in a JSON file
        # with open('zameen_properties.json', 'w', encoding='utf-8') as jsonfile:
        #     data = []
        #     for i in range(len(titles)):
        #         data.append({
        #             'Title': titles[i],
        #             'Price': prices[i],
        #             'URL': urls[i]
        #         })
        #     json.dump(data, jsonfile, indent=4)

    else:
        print("Failed to retrieve the page")

# Call the function with your desired location (e.g., city or zip code)
scrape_zameen('karachi')  # Replace 'karachi' with your desired location
