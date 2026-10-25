# Aufgaben-Manager (Python)

Mein erstes Python-Projekt: ein einfacher Aufgaben-Manager für die Konsole.

Vorher habe ich mit n8n (Low-Code) den Telegram-Bot **BROTÉ Bot** gebaut, der Aufgaben anlegt, anzeigt, erledigt und löscht. Hier habe ich dieselbe Logik in Python nachgebaut, um zu verstehen, was „unter der Haube“ passiert. Entwickelt mit KI-Unterstützung – jede Zeile habe ich nachvollzogen.

## Funktionen
- Aufgabe mit optionaler Frist anlegen (Datum wird geprüft)
- Offene Aufgaben anzeigen, überfällige werden markiert
- Aufgabe per ID als erledigt markieren oder löschen
- Speicherung in einer JSON-Datei – die Daten bleiben nach dem Beenden erhalten

## Starten
Python 3 installieren, dann im Ordner:

```
python aufgaben.py
```

## Was ich dabei gelernt habe
- Funktionen, Schleifen (`while`, `for`) und Bedingungen (`if/elif/else`)
- Listen und Dictionaries
- Dateien lesen und schreiben mit JSON
- Benutzereingaben prüfen und Fehler abfangen (`try/except`)
- Mit Datumswerten arbeiten (`datetime`)

## Nächste Schritte
- Aufgaben nach Frist sortieren
- Tests schreiben
- Den Manager wieder mit Telegram verbinden – diesmal in Python statt n8n
