from database import initialize_database, add_campbewohner, get_campbewohner_by_id, update_campbewohner, delete_campbewohner, add_raumreservierung, get_raumreservierungen_by_date, add_punkte, subtract_punkte, check_alter

def reserviere_raum():
    camp_bewohner_id = int(input("Geben Sie die ID des CampBewohners ein: "))
    raum_typ = input("Welchen Raumtyp möchten Sie reservieren (Wohnzimmer/Nebenraum)? ")
    startzeit = input("Geben Sie die Startzeit im Format YYYY-MM-DD HH:MM:SS ein: ")
    endzeit = input("Geben Sie die Endzeit im Format YYYY-MM-DD HH:MM:SS ein: ")
    anzahl_gaeste = int(input("Wie viele Gäste werden teilnehmen? "))
    zweck = input("Geben Sie den Zweck der Reservierung an (z.B. Geburtstagsfeier, Klausurvorbereitung): ")

    # Überprüfen Sie die Verfügbarkeit des Raums
    vorhandene_reservierungen = get_raumreservierungen_by_date(startzeit.split(" ")[0])
    for reservierung in vorhandene_reservierungen:
        if (startzeit < reservierung[4] and endzeit > reservierung[3]) and raum_typ == reservierung[2]:
            print("Der Raum ist zu dieser Zeit bereits reserviert.")
            return

    # Überprüfen Sie die Punkte des Benutzers
    bewohner = get_campbewohner_by_id(camp_bewohner_id)
    if bewohner[4] < 10:
        print("Sie haben nicht genügend Punkte, um den Raum zu reservieren.")
        return

    # Raum reservieren und Punkte abziehen
    add_raumreservierung(camp_bewohner_id, raum_typ, startzeit, endzeit, anzahl_gaeste, zweck)
    subtract_punkte(camp_bewohner_id, 10)
    print("Raum erfolgreich reserviert!")

def manage_punkte():
    camp_bewohner_id = int(input("Geben Sie die ID des CampBewohners ein: "))
    aktion = input("Möchten Sie Punkte hinzufügen oder abziehen (hinzufügen/abziehen)? ")
    punkte_menge = int(input("Wie viele Punkte möchten Sie hinzufügen/abziehen? "))

    if aktion == "hinzufügen":
        add_punkte(camp_bewohner_id, punkte_menge)
        print(f"{punkte_menge} Punkte wurden hinzugefügt.")
    elif aktion == "abziehen":
        subtract_punkte(camp_bewohner_id, punkte_menge)
        print(f"{punkte_menge} Punkte wurden abgezogen.")

def main_menu():
    initialize_database()
    while True:
        print("1. Neuen CampBewohner hinzufügen")
        print("2. Raumreservierung vornehmen")
        print("3. Punkte hinzufügen/abziehen")
        print("4. Beenden")
        auswahl = input("Wählen Sie eine Option: ")
        if auswahl == "1":
            # Logik zum Hinzufügen eines CampBewohners
            pass
        elif auswahl == "2":
            reserviere_raum()
        elif auswahl == "3":
            manage_punkte()
        elif auswahl == "4":
            break

if __name__ == "__main__":
    main_menu()
