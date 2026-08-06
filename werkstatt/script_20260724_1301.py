def sortiere_und_gib_drei_groesste(zahlenliste):
    """
    Sortiert eine Liste von Zahlen aufsteigend und gibt die drei groessten Elemente zurueck.

    Args:
        zahlenliste: Eine Liste von Zahlen.

    Returns:
        Eine Liste, die die drei groessten Zahlen aus der Eingabeliste enthaelt,
        oder weniger, wenn die Eingabeliste weniger als drei Elemente hat.
    """
    zahlenliste.sort()
    return zahlenliste[-3:]

if __name__ == '__main__':
    test_liste = [5, 2, 8, 1, 9, 4, 7, 3, 6]
    groesste_drei = sortiere_und_gib_drei_groesste(test_liste)
    print(f"Die drei groessten Zahlen sind: {groesste_drei}")

    test_liste_kurz = [10, 20]
    groesste_drei_kurz = sortiere_und_gib_drei_groesste(test_liste_kurz)
    print(f"Die drei groessten Zahlen (kurze Liste) sind: {groesste_drei_kurz}")

    test_liste_leer = []
    groesste_drei_leer = sortiere_und_gib_drei_groesste(test_liste_leer)
    print(f"Die drei groessten Zahlen (leere Liste) sind: {groesste_drei_leer}")