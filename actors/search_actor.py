import pykka
import requests
from bs4 import BeautifulSoup

class SearchActor(pykka.ThreadingActor):
    def on_receive(self, message):
        origin = message.get('origin')
        destination = message.get('destination')
        date = message.get('date')
        
        results = []
        results.extend(self.search_flybondi(origin, destination, date))
        results.extend(self.search_jetsmart(origin, destination, date))
        results.extend(self.search_aerolineas(origin, destination, date))
        
        return results

    def search_flybondi(self, origin, destination, date):
        url = f"https://www.flybondi.com/search?origin={origin}&destination={destination}&date={date}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extraer datos relevantes de Flybondi
        flights = []
        import requests
from bs4 import BeautifulSoup

def scrape_flybondi(origin, destination, date):
    url = f"https://flybondi.com/search?origin={origin}&destination={destination}&date={date}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    flights = []
    for flight in soup.find_all('div', class_='flight-info'):
        airline = 'Flybondi'
        price = flight.find('span', class_='price').text
        departure_time = flight.find('span', class_='departure-time').text
        arrival_time = flight.find('span', class_='arrival-time').text
        stops = flight.find('span', class_='stops').text
        
        flights.append({
            'airline': airline,
            'price': price,
            'departure_time': departure_time,
            'arrival_time': arrival_time,
            'stops': stops
        })

        return flights

    def search_jetsmart(self, origin, destination, date):
        url = f"https://jetsmart.com/ar/es/search?origin={origin}&destination={destination}&date={date}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extraer datos relevantes de Jetsmart
        flights = []
        import requests
from bs4 import BeautifulSoup

def scrape_jetsmart(origin, destination, date):
    url = f"https://jetsmart.com/ar/es/search?origin={origin}&destination={destination}&date={date}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    flights = []
    for flight in soup.find_all('div', class_='flight-info'):
        airline = 'JetSMART'
        price = flight.find('span', class_='price').text
        departure_time = flight.find('span', class_='departure-time').text
        arrival_time = flight.find('span', class_='arrival-time').text
        stops = flight.find('span', class_='stops').text
        
        flights.append({
            'airline': airline,
            'price': price,
            'departure_time': departure_time,
            'arrival_time': arrival_time,
            'stops': stops
        })

        return flights

    def search_aerolineas(self, origin, destination, date):
        url = f"https://www.aerolineas.com.ar/search?origin={origin}&destination={destination}&date={date}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extraer datos relevantes de Aerolíneas Argentinas
        flights = []
        import requests
from bs4 import BeautifulSoup

def scrape_aerolineas_argentinas(origin, destination, date):
    url = f"https://aerolineas.com.ar/search?origin={origin}&destination={destination}&date={date}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    flights = []
    for flight in soup.find_all('div', class_='flight-info'):
        airline = 'Aerolíneas Argentinas'
        price = flight.find('span', class_='price').text
        departure_time = flight.find('span', class_='departure-time').text
        arrival_time = flight.find('span', class_='arrival-time').text
        stops = flight.find('span', class_='stops').text
        
        flights.append({
            'airline': airline,
            'price': price,
            'departure_time': departure_time,
            'arrival_time': arrival_time,
            'stops': stops
        })

        return flights
