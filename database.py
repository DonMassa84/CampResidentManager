import sqlite3

DATABASE_NAME = 'camp_resident_manager.db'

def create_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def initialize_database():
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS campbewohner (
            id INTEGER PRIMARY KEY,
            vorname TEXT,
            nachname TEXT,
            geburtsdatum DATE,
            punkte INTEGER
        )
    """)
    
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

def add_raumreservierung(camp_bewohner_id, raum_typ, startzeit, endzeit, anzahl_gaeste, zweck):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO raumreservierung (camp_bewohner_id, raum_typ, startzeit, endzeit, anzahl_gaeste, zweck) VALUES (?, ?, ?, ?, ?, ?)", (camp_bewohner_id, raum_typ, startzeit, endzeit, anzahl_gaeste, zweck))
    conn.commit()
    conn.close()

def get_raumreservierungen_by_date(date):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM raumreservierung WHERE DATE(startzeit) = ?", (date,))
    result = cursor.fetchall()
    conn.close()
    return result

def add_punkte(camp_bewohner_id, punkte):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE campbewohner SET punkte = punkte + ? WHERE id=?", (punkte, camp_bewohner_id))
    conn.commit()
    conn.close()

def subtract_punkte(camp_bewohner_id, punkte):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE campbewohner SET punkte = punkte - ? WHERE id=?", (punkte, camp_bewohner_id))
    conn.commit()
    conn.close()

def check_alter(camp_bewohner_id):
    bewohner = get_campbewohner_by_id(camp_bewohner_id)
    geburtsdatum = datetime.strptime(bewohner[3], '%Y-%m-%d').date()
    heute = datetime.today().date()
    alter = heute.year - geburtsdatum.year - ((heute.month, heute.day) < (geburtsdatum.month, geburtsdatum.day))
    return alter



