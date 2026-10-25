import json
import os
from datetime import date, datetime

DATEI = "aufgaben.json"
DATUMSFORMAT = "%d.%m.%Y"  


def laden():
    """Liest alle Aufgaben aus der JSON-Datei. Gibt es die Datei noch nicht, kommt eine leere Liste zurück."""
    if not os.path.exists(DATEI):
        return []
    with open(DATEI, "r", encoding="utf-8") as f:
        return json.load(f)


def speichern(aufgaben):
    """Schreibt die Liste der Aufgaben in die JSON-Datei."""
    with open(DATEI, "w", encoding="utf-8") as f:
        json.dump(aufgaben, f, ensure_ascii=False, indent=2)


def neue_id(aufgaben):
    """Nimmt die höchste vorhandene ID und zählt 1 dazu."""
    hoechste = 0
    for a in aufgaben:
        if a["id"] > hoechste:
            hoechste = a["id"]
    return hoechste + 1


def datum_gueltig(text):
    """Prüft, ob der Text ein echtes Datum im Format TT.MM.JJJJ ist."""
    try:
        datetime.strptime(text, DATUMSFORMAT)
        return True
    except ValueError:
        return False


def hinzufuegen(aufgaben):
    titel = input("Aufgabe: ").strip()
    if titel == "":
        print("Die Aufgabe darf nicht leer sein.")
        return

    while True:
        frist = input("Frist (TT.MM.JJJJ, leer = keine Frist): ").strip()
        if frist == "" or datum_gueltig(frist):
            break
        print("Ungültiges Datum. Beispiel: 31.10.2026")

    aufgaben.append({
        "id": neue_id(aufgaben),
        "titel": titel,
        "frist": frist,
        "erledigt": False,
    })
    speichern(aufgaben)
    print("Aufgabe gespeichert.")


def anzeigen(aufgaben):
    heute = date.today()
    anzahl = 0
    for a in aufgaben:
        if a["erledigt"]:
            continue
        zeile = f"[{a['id']}] {a['titel']}"
        if a["frist"] != "":
            zeile += f" – bis {a['frist']}"
            if datetime.strptime(a["frist"], DATUMSFORMAT).date() < heute:
                zeile += "  (ÜBERFÄLLIG)"
        print(zeile)
        anzahl += 1
    if anzahl == 0:
        print("Keine offenen Aufgaben.")


def finden(aufgaben):
    """Fragt nach einer ID und gibt die passende Aufgabe zurück (oder None)."""
    eingabe = input("ID der Aufgabe: ").strip()
    if not eingabe.isdigit():
        print("Bitte eine Zahl eingeben.")
        return None
    for a in aufgaben:
        if a["id"] == int(eingabe):
            return a
    print("Keine Aufgabe mit dieser ID gefunden.")
    return None


def erledigen(aufgaben):
    a = finden(aufgaben)
    if a is not None:
        a["erledigt"] = True
        speichern(aufgaben)
        print(f"Erledigt: {a['titel']}")


def loeschen(aufgaben):
    a = finden(aufgaben)
    if a is not None:
        aufgaben.remove(a)
        speichern(aufgaben)
        print(f"Gelöscht: {a['titel']}")


def main():
    aufgaben = laden()
    while True:
        print("\n1 = Neue Aufgabe   2 = Offene Aufgaben   3 = Erledigt   4 = Löschen   0 = Beenden")
        wahl = input("Auswahl: ").strip()
        if wahl == "1":
            hinzufuegen(aufgaben)
        elif wahl == "2":
            anzeigen(aufgaben)
        elif wahl == "3":
            erledigen(aufgaben)
        elif wahl == "4":
            loeschen(aufgaben)
        elif wahl == "0":
            print("Tschüss!")
            break
        else:
            print("Bitte 0, 1, 2, 3 oder 4 eingeben.")


main()
