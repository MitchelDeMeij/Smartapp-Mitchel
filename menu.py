import opdrachtWeerstation
import smartApp
import meteoAPI

def menu():
    while True:
        print("\n=== Smart App Menu ===")
        print("1. Weerstation")
        print("2. Smart App Controller")
        print("3. Stoppen")

        try:
            keuze = int(input("Maak je keuze: "))
            if keuze == 1:
                opdrachtWeerstation.weerstation()
            elif keuze == 2:
                smartApp.smart_app_controller()
            elif keuze == 3:
                print("Programma afgesloten.")
                break
            else:
                print("Kies 1, 2 of 3.")
        except ValueError:
            print("Voer een geldig getal in.")

if __name__ == "__main__":
    meteoAPI.tempOphalen()
    menu()