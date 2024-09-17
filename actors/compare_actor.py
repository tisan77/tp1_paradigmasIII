import pykka

class CompareActor(pykka.ThreadingActor):
    def on_receive(self, message):
        results = message.get('results')
        sorted_results = sorted(results, key=lambda x: x['price'])
        return sorted_results
