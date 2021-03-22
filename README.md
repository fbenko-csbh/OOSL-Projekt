# Finanzplanungs-Programm

![Screenshot der Anwendung](/images/screenshot.png)

## Beschreibung
Ein Anwender soll die Möglichkeit haben, bestehende private Ein- und Ausgaben in
einer Datenmaske erfassen zu können. Diese Informationen können in einer SQLite Datenbank
persistiert werden. Die Informationen sollen darüber hinaus in einer einfachen Analyse bewertet
und das Ergebnis grafisch dargestellt werden können.


## Technologie
* Python
* Tkinter
* SQLite3


## Requirements
ID | Beschreibung | Kategorie | Priorität | Abnahmekriterium 
---|--------------|-----------|-----------|-----------------
10 | Das Programm-Fenster soll in der Größe veränderbar sein | Gebrauchstauglichkeit | A - sehr hoch | Fenstergröße ändern muss möglich sein
20 | Die Eingabe der mtl. Einnahmen und Ausgaben muss möglich sein | Funktionale Anforderung | A - sehr hoch | Eingabe-Felder müssen dargestellt werden
30 | grafische Darstellung der gewichteten Ausgaben-Positionen  | Funktionale Anforderung | A- sehr hoch | Kuchendiagramm muss dargestellt werden
40 | grafische Darstellung des Verhältnisses Einnahmen/Ausgaben | Funktionale Anforderung | A- sehr hoch | Balken muss dargestellt werden
50 | Alle eingegebenen Positionen soll in einer Übersicht dargestellt werden | Funktionale Anforderung | A - sehr hoch | Tabellenübersicht muss dargestellt sein
60 | Daten sollen gespeichert werden | Funktionale Anforderung | A - sehr hoch | Daten müssen in Datenbank persistiert werden
70 | Die Bedienung soll intuitiv möglich sein | Gebrauchstauglichkeit | A - sehr hoch | Positiver User-Test
80 | Daten, Darstellung und Logik sollen getrennt bearbeitbar sein | Skalierbarkeit | B - hoch | Anwendung des MVC Pattern 

## Darstellung
![Screenshot der Anwendung](/images/screenshot2.png)
![Screenshot der Anwendung](/images/screenshot3.png)
