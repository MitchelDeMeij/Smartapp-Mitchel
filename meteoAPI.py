import json
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

def tempOphalen():
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=52.09&longitude=5.12"
        "&current=temperature_2m"
    )

    try:
        with urlopen(url, timeout=10) as antwoord:
            gegevens = json.loads(antwoord.read().decode("utf-8"))
        temperatuur = gegevens["current"]["temperature_2m"]
        print(f"Goedemiddag, het is momenteel {temperatuur} graden in Utrecht.")
    except (HTTPError, URLError, TimeoutError):
        print("Het weer kon niet worden opgehaald. Controleer je internet?")
    except (KeyError, ValueError):
        print("De ontvangen weergegevens zijn niet geldig.")

if __name__ == "__main__":
    tempOphalen()