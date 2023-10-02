import sqlite3
from datetime import datetime

DATABASE_NAME = 'camp_resident_manager.db'

def create_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def initialize_database():
    conn = create_connection()
    cursor = conn.cursor()
    
    # Tabelle für CampBewohner
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS campbewohner (
            id INTEGER PRIMARY KEY,
            vorname TEXT,
            nachname TEXT,
            geburtsdatum DATE,
            punkte INTEGER
        )
    """)
    
    # Tabelle für RaumReservierung
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS raumreservierung (
            reservierungs_id INTEGER PRIMARY KEY,
            camp_bewohner_id INTEGER,
            raum_typ TEXT,
            startzeit DATETIME,
            endzeit DATETIME,
            anzahl_gaeste INTEGER,
            zweck TEXT,
            FOREIGN KEY (camp_bewohner_id) REFERENCES campbewohner(id)
        )
    """)
    
    # ... (weitere Tabellen erstellen)
    
    conn.commit()
    conn.close()

def add_campbewohner(vorname, nachname, geburtsdatum):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO campbewohner (vorname, nachname, geburtsdatum, punkte) VALUES (?, ?, ?, ?)", (vorname, nachname, geburtsdatum, 100))
    conn.commit()
    conn.close()

def get_campbewohner_by_id(id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM campbewohner WHERE id=?", (id,))
    result = cursor.fetchone()
    conn.close()
    return result

def update_campbewohner(id, vorname, nachname, geburtsdatum):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE campbewohner SET vorname=?, nachname=?, geburtsdatum=? WHERE id=?", (vorname, nachname, geburtsdatum, id))
    conn.commit()
    conn.close()

def delete_campbewohner(id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM campbewohner WHERE id=?", (id,))
    conn.commit()
    conn.close()

# Ähnliche Funktionen für andere Tabellen und Operationen können hier hinzugefügt werden.


