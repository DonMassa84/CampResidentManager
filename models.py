from datetime import datetime

class CampBewohner:
    def __init__(self, id, vorname, nachname, geburtsdatum, punkte):
        self.id = id
        self.vorname = vorname
        self.nachname = nachname
        self.geburtsdatum = geburtsdatum
        self.punkte = punkte

class RaumReservierung:
    def __init__(self, reservierungs_id, camp_bewohner_id, raum_typ, startzeit, endzeit, anzahl_gaeste, zweck):
        self.reservierungs_id = reservierungs_id
        self.camp_bewohner_id = camp_bewohner_id
        self.raum_typ = raum_typ
        self.startzeit = startzeit
        self.endzeit = endzeit
        self.anzahl_gaeste = anzahl_gaeste
        self.zweck = zweck

