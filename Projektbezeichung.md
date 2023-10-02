1. Projektbezeichung.
Campbewohner(innen) – Verwaltungsanwendung.

2. Zielsetzung Soll-Konzept
Bei meiner Tätigkeit als Praktikant bei der Firma Grassau GmbH, 
wurde mir der Auftrag erteilt eine Lösung zu konzipieren. 
Anhand folgender  Aufgabenstellung (siehe Ist-Analyse)

verwende Ich eine  SQL Datenbank, um sämtliche Informationen wie Name, Vorname, Geburtsdatum und Alter für FSK abfragen abzuspeichern.
2.2 Ist-Analyse
Es gibt 1200 Camp-Bewohner, jeder von Ihnen hat einen Tisch einen Stuhl und ein Bett,
Jeder möchte das Wohnzimmer nutzen, Wohnzimmer vermietet das Unternehmen Grassau GmbH so zusagen Kostenfrei.
Für jeweils 1,5 Stunden, oder auch für 3 Stunden also 2 mal 1,5 Stunden.
Jetzt ist die Frage wer möchte es mieten für was und zu welchem Zeitraum?
Es kann ja sein jemand hat Geburtstag. 
Somit ist es eine Person, und möchte das Objekt mieten mit 5 bis 8 anderen Personen. 

D.h nur nutzen für Geburtstagsfeier. Im Objekt kann man Playstation spielen.
jetzt gibt es die Frage wie alt sind die Personen?
Die Personen unter 10 Jahren können nur Spiele spielen die gemäss FSK die ihrem Alter entsprechen.
Deshalb wird diese Altersabfrage implementieren. 
Dann können sich z.B 9 Personen anmelden und Playstation spielen.
Alle paar Minuten wechselt der Spielen und jeder darf mal spielen.


Dann können Camp - Bewohner gemeinsam einen Filmabend verbringen, je nach dem kann ein Film angeschaut werden.
Von jeder Altersgruppe sind von 1200 Menschen so viele da, 
das es kein Problem darstellt, weil der Raum eine Kapazität von 20 bis 30 Personen hat.
Deshalb müssen die Altersgruppen heraus gefunden werden.
Der Raum hat auch noch einen Nebenraum. Wenn jemand eine Klausur schreibt, soll er diesen Raum mieten und sich dort hinsetzen und für die Klausur lernen.
Oder wenn jemand etwas scannen möchte oder etwas drucken möchte für das JobCenter, kann er diesen zusätzlichen Raum nutzen, muss man also reservieren können, Sonderfall. Im extra Raum den man zusätzlich mieten kann. Sozusagen.
Jeder aus dem Camp bekommt 100 Punkte.
Und eine Buchung kostet 10 Punkte.
Die frage ist wie kann Ich sicherstellen, das jeder alles richtig macht und Dass jeder Gleichberechtigt ist.
Es gibt auch Menschen, die mithelfen diese sollen die Möglichkeit bekommen 10 Punkte extra zu verdienen.(aufgeräumt, Kehrwoche, positiv Aufgefallen etc.)
Das Gegenteil, es wurde etwas schlecht gemacht und es werden 10 Punkte abgezogen.
Bei normalen Verhalten, einfach nur seine Raumkapazität gemacht. Normal gebraucht.
Sicherstellen das jeder auf gleiche Fairness den Raum nutzt.
Angenommen jemand nutzt den Raum jeden Tag und hat seine Punkte aufgebraucht, dann kann jemand anderes diesen Raum mit seinen nutzen.
Irgendwie müssen wir fair einen Raum den jeder nutzen will auf viele Leute aufteilen.

2.3 Was soll am Ende des Projektes erreicht sein?
Ziel ist es eine Anwendung zu entwickeln die sicherstellt das alle unter 10 jährigen und die  restlichen jugendlichen bis 18 Jahren, die Räumlichkeiten fair nutzen können. 
zusammenfassen:

 Create: Anweisung, um einen neuen Datensatz zu erstellen
 Read oder Retrieve: Liest Datensätze aus einer Datenbanktabelle basierend
auf den Eingabeparametern
 Update: Führt eine Aktualisierung bestehender Datenbankobjekte durch
 Delete oder Destroy: Löscht eine definierte Zeile aus einer Datenbanktabelle.

Mit diesen vier Funktionen lassen sich Daten in Systemen also anlegen und in jeder
Form verwalten.

2.4 Welche Anforderungen müssen erfüllt sein?
1. Einfache Bedienung über Intuitive Führung
2. Daten hinzufügen (Create)
3. Daten anzeigen (Read)
4. Daten verändern (Update)
5. Daten löschen (Delete)

2.5 Welche Einschränkungen müssen berücksichtigt werden?
Der Auftraggeber will mit allen Mitteln das Projekt entwickeln lassen somit spielt es keine Rolle welche Programmiersprache verwendet werden.

2.6 Was ist zur Erfüllung der Zielsetzung notwendig?

Um die Zielsetzung des Projekts zu erfüllen, sind folgende Schritte und Ressourcen notwendig:

1. **Datenbankentwurf**: 
   - Entwerfen einer relationalen Datenbankstruktur, die alle benötigten Informationen wie Name, Vorname, Geburtsdatum, Alter, Punktestand und Buchungshistorie speichert.
   - Einrichten von Tabellen für Camp-Bewohner, Raumreservierungen, Punkteverlauf und Altersgruppen.

2. **Benutzeroberfläche**:
   - Entwicklung einer intuitiven Benutzeroberfläche, die es den Benutzern ermöglicht, ihre Daten einzugeben, Raumreservierungen vorzunehmen und ihren Punktestand einzusehen.
   - Implementierung der CRUD-Funktionalität (Create, Read, Update, Delete) in der Benutzeroberfläche.

3. **Altersverifikation**:
   - Ein System, das das Alter der Benutzer überprüft und sicherstellt, dass sie nur auf Inhalte zugreifen können, die ihrem Alter entsprechen (z.B. FSK-geprüfte Spiele).

4. **Punktesystem**:
   - Ein System, das den Punktestand jedes Camp-Bewohners verfolgt und aktualisiert, basierend auf ihren Aktionen (z.B. Raumreservierung, Mithilfe bei der Reinigung, Regelverstöße).

5. **Reservierungssystem**:
   - Ein System, das es den Benutzern ermöglicht, Räume zu reservieren, basierend auf Verfügbarkeit und ihrem Punktestand.
   - Ein Kalendersystem, das zeigt, wann Räume verfügbar sind und wann sie bereits reserviert sind.

6. **Berichterstattung und Analyse**:
   - Tools, die es den Administratoren ermöglichen, die Nutzung der Räumlichkeiten zu überwachen und zu analysieren, um sicherzustellen, dass sie fair genutzt werden.

7. **Sicherheit**:
   - Implementierung von Sicherheitsmaßnahmen, um sicherzustellen, dass die Daten der Benutzer geschützt sind und nur autorisierte Personen Zugriff auf die Verwaltungsanwendung haben.

8. **Schulung und Dokumentation**:
   - Bereitstellung von Schulungsmaterialien und Handbüchern für die Benutzer und Administratoren der Anwendung.
   - Durchführung von Schulungssitzungen, um sicherzustellen, dass alle Beteiligten wissen, wie sie die Anwendung effektiv nutzen können.

9. **Feedback-Mechanismus**:
   - Ein System, das es den Benutzern ermöglicht, Feedback zur Anwendung zu geben, um kontinuierliche Verbesserungen zu ermöglichen.

10. **Technische Anforderungen**:
   - Auswahl der geeigneten Technologien und Programmiersprachen, die den Anforderungen des Projekts entsprechen und vom Auftraggeber akzeptiert werden.
   - Sicherstellung, dass die Anwendung auf den Geräten und Plattformen funktioniert, die von den Camp-Bewohnern verwendet werden.

Durch die Umsetzung dieser Schritte und die Bereitstellung der notwendigen Ressourcen kann sichergestellt werden, dass die Zielsetzung des Projekts erreicht wird und eine effektive und faire Nutzung der Räumlichkeiten durch die Camp-Bewohner ermöglicht wird.
