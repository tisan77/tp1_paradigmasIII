from actors.search_actor import SearchActor
from actors.parse_actor import ParseActor
from actors.compare_actor import CompareActor
from actors.save_actor import SaveActor
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

def scrape_jetsmart(origin, destination, date):
    # Implementa el scraping para JetSmart aquí
    return []

def scrape_aerolineas_argentinas(origin, destination, date):
    # Implementa el scraping para Aerolíneas Argentinas aquí
    return []

# Solicitar datos al usuario
origin = "AEP"  # Buenos Aires, Aeroparque
destination = "BRC"  # Bariloche
date = "2024-10-27"

# Scraping de las tres aerolíneas
flybondi_flights = scrape_flybondi(origin, destination, date)
jetsmart_flights = scrape_jetsmart(origin, destination, date)
aerolineas_flights = scrape_aerolineas_argentinas(origin, destination, date)

# Combinar resultados
all_flights = flybondi_flights + jetsmart_flights + aerolineas_flights

# Procesar y guardar resultados
parse_actor = ParseActor.start().proxy()
compare_actor = CompareActor.start().proxy()
save_actor = SaveActor.start().proxy()

parsed_results = parse_actor.ask({'data': all_flights})
compared_results = compare_actor.ask({'results': parsed_results})
save_actor.ask({'results': compared_results})

parse_actor.stop()
compare_actor.stop()
save_actor.stop()
