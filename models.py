from datetime import datetime

class CampBewohner:
    def __init__(self, id, vorname, nachname, geburtsdatum, punkte=100):
        self.id = id
        self.vorname = vorname
        self.nachname = nachname
        self.geburtsdatum = geburtsdatum
        self.punkte = punkte

    @property
    def alter(self):
        today = datetime.today()
        return today.year - self.geburtsdatum.year - ((today.month, today.day) < (self.geburtsdatum.month, self.geburtsdatum.day))

class RaumReservierung:
    def __init__(self, reservierungs_id, camp_bewohner, raum_typ, startzeit, endzeit, anzahl_gaeste, zweck):
        self.reservierungs_id = reservierungs_id
        self.camp_bewohner = camp_bewohner
        self.raum_typ = raum_typ
        self.startzeit = startzeit
        self.endzeit = endzeit
        self.anzahl_gaeste = anzahl_gaeste
        self.zweck = zweck

class Spiel:
    def __init__(self, spiel_id, name, fsk_altersfreigabe):
        self.spiel_id = spiel_id
        self.name = name
        self.fsk_altersfreigabe = fsk_altersfreigabe

class Film:
    def __init__(self, film_id, titel, fsk_altersfreigabe):
        self.film_id = film_id
        self.titel = titel
        self.fsk_altersfreigabe = fsk_altersfreigabe

class PunkteTransaktion:
    def __init__(self, transaktions_id, camp_bewohner, datum, punkte, grund):
        self.transaktions_id = transaktions_id
        self.camp_bewohner = camp_bewohner
        self.datum = datum
        self.punkte = punkte
        self.grund = grund

class Feedback:
    def __init__(self, feedback_id, camp_bewohner, datum, kommentar, bewertung):
        self.feedback_id = feedback_id
        self.camp_bewohner = camp_bewohner
        self.datum = datum
        self.kommentar = kommentar
        self.bewertung = bewertung
