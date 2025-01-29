import requests
from bs4 import BeautifulSoup

def scrape_air_quality_data():
    url = "https://air-quality.com/place/india/gurugram/d2853e61?lang=en&standard=aqi_us"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    pollutants = {}
    
    # Find all pollutant items
    pollutant_items = soup.find_all('div', {'class': 'pollutant-item'})
    
    for item in pollutant_items:
        name = item.find('div', {'class': 'name'}).text.strip()
        value = item.find('div', {'class': 'value'}).text.strip()
        pollutants[name] = value
    
    return pollutants

# Example usage
if __name__ == "__main__":
    data = scrape_air_quality_data()
    print(data)