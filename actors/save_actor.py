import pykka

class SaveActor(pykka.ThreadingActor):
    def on_receive(self, message):
        results = message.get('results')
        with open('results.txt', 'w') as f:
            for result in results:
                f.write(f"Aerolinea: {result['airline']}\n")
                f.write(f"Precio: {result['price']}\n")
                f.write(f"Hora de salida: {result['departure_time']}\n")
                f.write(f"Hora de llegada: {result['arrival_time']}\n")
                f.write(f"Escalas: {result['stops']}\n")
                f.write("\n")
        return "Results saved"
