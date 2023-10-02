import sqlite3

def create_connection():
    conn = sqlite3.connect('camp_resident_manager.db')
    return conn

def initialize_database():
    conn = create_connection()
    cursor = conn.cursor()
    
    # Erstellen Sie hier die Tabellen basierend auf den Modellen
    # Beispiel:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS campbewohner (
            id INTEGER PRIMARY KEY,
            vorname TEXT,
            nachname TEXT,
            geburtsdatum DATE,
            punkte INTEGER
        )
    """)
    
    # ... (weitere Tabellen erstellen)
    
    conn.commit()
    conn.close()
