# Primzahltest Rekursiv
# Keine Schleifen, sondern Rekursion

# Variablen
n = 10007 * 100003 # Zahl, die getestet werden soll
i = 2 # Startwert für den Divisor, muss 2 sein, da 1 immer teilt und 2 die kleinste Primzahl ist

# Funktion, die prüft, ob n eine Primzahl ist
def is_prime(n, i=2):
    # Basisfall: Wenn n kleiner als 2 ist, ist es keine Primzahl
    if n < 2:
        return False
    # Wenn i*i größer als n, dann ist n eine Primzahl
    if i * i > n:
        return True
    # Wenn n durch i teilbar ist, dann ist es keine Primzahl
    if n % i == 0:
        return False
    # Rekursiver Aufruf mit dem nächsten Divisor
    return is_prime(n, i + 1)
# Test der Funktion
print(f"Zahl: {n}")
print(f"Ist Primzahl: {is_prime(n)}")
