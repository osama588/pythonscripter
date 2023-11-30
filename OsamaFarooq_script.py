import requests
from bs4 import BeautifulSoup
import csv

def scrape_property_info(location):
    url = f'https://www.graana.com/sale/residential-properties-sale-islamabad-1/' 
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
    }  

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            property_listings = []

            
            listings = soup.find_all('div', class_='MuiBox-root mui-style-zf9afz')  
            for listing in listings:
                title = listing.find('h5', class_='MuiTypography-root MuiTypography-subtitle2New mui-style-3bzwbl').text.strip()  
                price = listing.find('div', class_="MuiBox-root mui-style-x1sij0").text.strip() 
                property_listings.append({
                    'Title': title,
                    'Price': price,
                })

            return property_listings
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Request Exception: {e}")
        return None

def save_to_csv(data):
    if data:
        keys = data[0].keys()
        with open('property_listings.csv', 'w', newline='', encoding='utf-8') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)
        print("Data saved to property_listings.csv")
    else:
        print("No data to save")

if __name__ == "__main__":
    location = 'your-designated-location' 
    property_data = scrape_property_info(location)
    save_to_csv(property_data)
