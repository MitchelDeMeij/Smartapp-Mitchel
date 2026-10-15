
def aantal_dagen(inputFile):
    with open(inputFile, "r") as bestand:
        regels = bestand.readlines()
    dagen = 0

    for regel in regels[1:]:
        if regel.strip() != "":
            dagen += 1
    return dagen

def auto_bereken(inputFile, outputFile):
    with open(inputFile, "r") as bestand:
        regels = bestand.readlines()

    with open(outputFile, "w") as bestand:
        for regel in regels[1:]:
            if regel.strip() == "":
                continue

            gegevens = regel.split()
            datum = gegevens[0]
            personen = int(gegevens[1])
            setpoint = float(gegevens[2])
            buiten = float(gegevens[3])
            neerslag = float(gegevens[4])
            verschil = setpoint - buiten

            if verschil >= 20:
                cv_ketel = 100
            elif verschil >= 10:
                cv_ketel = 50
            else:
                cv_ketel = 0

            ventilatie = min(personen + 1, 4)
            bewatering = neerslag < 3
            bestand.write(f"{datum};{cv_ketel};{ventilatie};{bewatering}\n")

    print("Alle actuatoren zijn berekend en opgeslagen.")

def overwrite_settings(outputFile):
    try:
        with open(outputFile, "r") as bestand:
            regels = bestand.readlines()
    except FileNotFoundError:
        print("Fout: output bestand niet gevonden")
        return -3

    datum = input("Welke datum wil je aanpassen?: ")

    datum_gevonden = False

    for regel in regels:
        gegevens = regel.strip().split(";")

        if gegevens[0] == datum:
            datum_gevonden = True
            break

    if not datum_gevonden:
        print("Fout: datum niet gevonden.")
        return -1

    print("Welk systeem wil je aanpassen?")
    print("1. CV-ketel")
    print("2. Ventilatie")
    print("3. Bewatering")

    systeem = input("Maak je keuze (1, 2 of 3): ")

    if systeem not in ["1", "2", "3"]:
        print("Fout: ongeldig systeem gekozen.")
        return -3

    waarde = input("Welke nieuwe waarde wil je instellen? ")

    try:
        nieuwe_waarde = int(waarde)
    except ValueError:
        print("Fout: voer een geheel getal in.")
        return -3

    if systeem == "1":
        if nieuwe_waarde < 0 or nieuwe_waarde > 100:
            print("Fout: de CV-ketel moet tussen 0 en 100 liggen.")
            return -3
        kolom = 1

    elif systeem == "2":
        if nieuwe_waarde < 0 or nieuwe_waarde > 4:
            print("Fout: ventilatie moet tussen 0 en 4 liggen.")
            return -3
        kolom = 2

    else:
        if nieuwe_waarde not in [0, 1]:
            print("Fout: bewatering moet 0 of 1 zijn.")
            return -3

        if nieuwe_waarde == 0:
            nieuwe_waarde = "False"
        else:
            nieuwe_waarde = "True"

        kolom = 3

    for i in range(len(regels)):
        gegevens = regels[i].strip().split(";")
        if gegevens[0] == datum:
            gegevens[kolom] = str(nieuwe_waarde)
            regels[i] = ";".join(gegevens) + "\n"
            break

    with open(outputFile, "w") as bestand:
        bestand.writelines(regels)
    print("De waarde is succesvol aangepast.")
    return 0

def smart_app_controller():
    inputFile = "input.txt"
    outputFile = "output.txt"

    while True:
        print("\n=== Smart App Controller ===")
        print("1. Hoeveel dagen zijn aanwezig?")
        print("2. Bereken alle actuatoren")
        print("3. Overschrijf een waarde")
        print("4. Stoppen")

        keuze = input("Maak je keuze (1-4): ")

        if keuze == "1":
            try:
                dagen = aantal_dagen(inputFile)
                print("Aantal dagen:", dagen)
            except FileNotFoundError:
                print("Fout: input.txt is niet gevonden.")
        elif keuze == "2":
            try:
                auto_bereken(inputFile, outputFile)
            except (FileNotFoundError, ValueError, IndexError):
                print("Fout: het invoerbestand ontbreekt of bevat ongeldige gegevens.")
        elif keuze == "3":
            resultaat = overwrite_settings(outputFile)
            if resultaat == -1:
                print("Controleer de ingevoerde datum.")
            elif resultaat == -3:
                print("De waarde is niet aangepast.")
        elif keuze == "4":
            print("Het programma wordt afgesloten.")
            break
        else:
            print("Ongeldige keuze. Kies 1, 2, 3 of 4.")

if __name__ == "__main__":
    smart_app_controller()