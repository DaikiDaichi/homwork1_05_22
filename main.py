# Unterprogramme
def zahlen_eingeben():
    zahl1 = input("Zahl 1: ")
    zahl2 = input("Zahl 2: ")
    return (zahl1, zahl2)


def zahlen_tauschen(zahlen):
    zahl1, zahl2 = zahlen
    hilf = zahl1
    zahl1 = zahl2
    zahl2 = hilf
    return (zahl1, zahl2)


def zahlen_ausgeben(zahl):
    zahl1, zahl2 = zahl
    print("Zahl 1: ", zahl1)
    print("Zahl 2: ", zahl2)


# Hauptprogramm
zahlen_ausgeben(zahlen_tauschen(zahlen_eingeben()))

# ======================================================================================================================

def zahlen_ein():
    zahl3 = input("Zahl 1: ")
    zahl4 = input("Zahl 2: ")
    return (zahl4, zahl3)

def zahlen_aus(zahl):
    zahl1, zahl2 = zahl
    print("Zahl 1: ", zahl1)
    print("Zahl 2: ", zahl2)

zahlen_aus(zahlen_ein())