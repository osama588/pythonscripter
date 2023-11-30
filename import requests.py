import requests

def check_robots_txt(url):
    robots_url = url + "/robots.txt"
    response = requests.get(robots_url)
    
    if response.status_code == 200:
        print("Robots.txt content:")
        print(response.text)
    else:
        print(f"Failed to retrieve robots.txt. Status code: {response.status_code}")

# Example usage for Zillow
check_robots_txt("https://www.zillow.com")
