import pykka
import requests
from bs4 import BeautifulSoup
from config import FLYBONDI_URL, JETSMART_URL, AEROLINEAS_ARGENTINAS_URL

class SearchActor(pykka.ThreadingActor):
    
    def on_receive(self, message):
        origin = message.get('origin')
        destination = message.get('destination')
        date = message.get('date')
        
        # Realiza scraping en las aerolíneas
        flybondi_flights = self.scrape_flybondi(origin, destination, date)
        jetsmart_flights = self.scrape_jetsmart(origin, destination, date)
        aerolineas_flights = self.scrape_aerolineas_argentinas(origin, destination, date)
        
        # Devuelve una lista combinada de resultados
        all_flights = flybondi_flights + jetsmart_flights + aerolineas_flights
        return all_flights

    def scrape_flybondi(self, origin, destination, date):
        url = FLYBONDI_URL.format(origin=origin, destination=destination, date=date)
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

    def scrape_jetsmart(self, origin, destination, date):
        url = JETSMART_URL.format(origin=origin, destination=destination, date=date)
        # Implementar el scraping de JetSmart aquí
        return []

    def scrape_aerolineas_argentinas(self, origin, destination, date):
        url = AEROLINEAS_ARGENTINAS_URL.format(origin=origin, destination=destination, date=date)
        # Implementar el scraping de Aerolíneas Argentinas aquí
        return []
