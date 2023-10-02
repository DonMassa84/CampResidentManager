from database import initialize_database, add_campbewohner, get_campbewohner_by_id, update_campbewohner, delete_campbewohner, add_raumreservierung, get_raumreservierungen_by_date, add_punkte, subtract_punkte, check_alter

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
            # Logik zur Raumreservierung
            pass
        elif auswahl == "3":
            # Logik zum Hinzufügen/Abziehen von Punkten
            pass
        elif auswahl == "4":
            break

if __name__ == "__main__":
    main_menu()

