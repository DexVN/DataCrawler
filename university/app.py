import requests
from bs4 import BeautifulSoup

# URL of the page you want to scrape
url = 'https://example.com'

# Define the cookie
cookies = {
    'cookie_name': 'MOODLEID1_=%257BN%251A%25F5%25DB%2503%25CA%2B; Path=/; Secure;'  # Replace with actual cookie name and value
}

# Make the request with cookies
response = requests.get(url, cookies=cookies)

# Check the status code of the response
if response.status_code == 200:
    print("Request successful")
else:
    print(f"Failed to retrieve page: {response.status_code}")

# Parse the page with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Example of scraping some data
data = soup.find_all('div', class_='example-class')  # Change to the actual HTML structure
for item in data:
    print(item.get_text(strip=True))
