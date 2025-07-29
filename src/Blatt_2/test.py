limit = 10

# Schritt 1: Alle Zahlen sammeln
is_prime = list(range(2, limit+1))
print(f"Start: {is_prime}")

# Schritt 2: Vielfache entfernen
for i in range(2, int(limit**0.5) + 1):  # nur bis √10 = 3.16, also bis 3
    if i in is_prime:  # Falls i noch nicht gestrichen wurde
        print(f"\nEntferne Vielfache von {i}:")
        
        # Sammle alle Vielfachen von i (außer i selbst)
        to_remove = []
        for j in range(i*i, limit+1, i):  # ab i² 
            if j in is_prime:
                to_remove.append(j)
        
        # Entferne sie
        for num in to_remove:
            is_prime.remove(num)
            print(f"  Entfernt: {num}")
        
        print(f"  Liste nach {i}: {is_prime}")

print(f"\nEndergebnis: {is_prime}")