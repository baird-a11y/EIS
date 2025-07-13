from math import sqrt

def ist_primzahl(zahl: int) -> bool:
    """
    Prüft effizient, ob eine Zahl eine Primzahl ist.
    
    Args:
        zahl: Die zu prüfende Zahl
        
    Returns:
        True wenn Primzahl, False sonst
    """
    # Spezialfälle
    if zahl < 2:
        return False
    if zahl == 2:
        return True
    if zahl % 2 == 0:  # Alle geraden Zahlen > 2 sind keine Primzahlen
        return False
    
    # Nur ungerade Zahlen von 3 bis sqrt(zahl) prüfen
    for i in range(3, int(sqrt(zahl)) + 1, 2):
        if zahl % i == 0:
            return False
    
    return True

# Test
zahl = 10003
if ist_primzahl(zahl):
    print(f"{zahl} ist eine Primzahl.")
else:
    print(f"{zahl} ist keine Primzahl.")