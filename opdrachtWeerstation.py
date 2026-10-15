def fahrenheit(temp_celcius):
    return 32 + 1.8 * temp_celcius


def gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid):
    return temp_celcius - (luchtvochtigheid / 100) * windsnelheid


def weerrapport(temp_celcius, windsnelheid, luchtvochtigheid):
    gevoel = gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid)

    if gevoel < 0 and windsnelheid > 10:
        return "Het is heel koud en het stormt! Verwarming helemaal aan!"
    elif gevoel < 0 and windsnelheid <= 10:
        return "Het is behoorlijk koud! Verwarming aan op de benedenverdieping!"
    elif 0 <= gevoel < 10 and windsnelheid > 12:
        return "Het is best koud en het waait; verwarming aan en roosters dicht!"
    elif 0 <= gevoel < 10 and windsnelheid <= 12:
        return "Het is een beetje koud, elektrische kachel op de benedenverdieping aan!"
    elif 10 <= gevoel < 22:
        return "Heerlijk weer, niet te koud of te warm."
    else:
        return "Warm! Airco aan!"
    
def weerstation():
    dagen = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]
    tempDagen = []
    windDagen = []
    vochtDagen = []

    for i in range(len(dagen)):
        temperatuur = input(f"Hoeveel graden celsius is het op {dagen[i]}?: ")
        while temperatuur.strip() != "" and not temperatuur.replace(".", "", 1).lstrip("-").isdigit():
            print("Ongeldige invoer, probeer opnieuw.")
            temperatuur = input(f"Hoeveel graden celsius is het op {dagen[i]}?: ")
        if temperatuur.strip() == "":
            break

        windSnelheid = input(f"Wat is de windsnelheid op {dagen[i]} in meters per seconde?: ")
        while windSnelheid.strip() != "" and not windSnelheid.replace(".", "", 1).isdigit():
            print("Ongeldige invoer, probeer opnieuw.")
            windSnelheid = input(f"Wat is de windsnelheid op {dagen[i]} in meters per seconde?: ")
        if windSnelheid.strip() == "":
            break

        luchtVochtigheid = input(f"Wat is de luchtvochtigheid op {dagen[i]} (0-100)?: ")
        while luchtVochtigheid.strip() != "" and not luchtVochtigheid.isdigit():
            print("Voer een geheel percentage van 0 tot 100 in.")
            luchtVochtigheid = input(f"Wat is de luchtvochtigheid op {dagen[i]} (0-100)?: ")
        if luchtVochtigheid.strip() == "":
            break

        while luchtVochtigheid.strip() != "" and (not luchtVochtigheid.isdigit() or not 0 <= int(luchtVochtigheid) <= 100):
            print("Voer een geheel percentage van 0 tot 100 in.")
            luchtVochtigheid = input(f"Wat is de luchtvochtigheid op {dagen[i]} (0-100)?: ")

        if luchtVochtigheid.strip() == "":
            break

        tempDagen.append(float(temperatuur))
        windDagen.append(float(windSnelheid))
        vochtDagen.append(int(luchtVochtigheid))

        gradenF = fahrenheit(tempDagen[i])      
        rapport = weerrapport(tempDagen[i], windDagen[i], vochtDagen[i])
        gemiddelde = sum(tempDagen) / len(tempDagen)

        print(f"Het is {tempDagen[i]:.1f} graden celcius, en {gradenF:.1f} graden fahrenheit")
        print(rapport)
        print(f"Gemiddelde temperatuur tot nu toe is {gemiddelde:.1f} graden celsius")
        print("------------------------------")

if __name__ == "__main__":
    weerstation()