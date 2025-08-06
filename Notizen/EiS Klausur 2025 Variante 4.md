# Klausur: Einführung in die Softwareentwicklung

**Sommersemester 2025 · 07. August 2025 (Variante D)**

---

## Angaben zur Person

**Vorname:** _________________ **Matrikelnummer:** _________________

**Nachname:** _________________

---

## Anleitung

• Die Klausur besteht aus **7 Aufgaben** auf insgesamt **11 einzelnen Seiten**.

• Sie können maximal **100 Punkte** erreichen. Sie haben ab **50 Punkten** auf jeden Fall bestanden.

• **Programmiersprachen:** Python mit Type-Annotations

• **Pseudocode erlaubt:** Falls Sie Syntax vergessen haben, können Sie Pseudocode verwenden

• Sie haben **3 Stunden Zeit** für die Bearbeitung.

**Wir wünschen Ihnen viel Erfolg!**

---

## Teil A: Programmieraufgaben (70 Punkte)

## Aufgabe 1: Strings und Listen (15 Punkte)

### a) String-Verarbeitung (8 Punkte)

Schreiben Sie eine Funktion `count_vowels`, die zählt, wie viele Vokale (a, e, i, o, u) in einem String vorkommen. Groß- und Kleinschreibung soll ignoriert werden.

```python
def count_vowels(text: str) -> int:
    vowels: dict[str] = ["a","e","i","o","u"]
    counter: int = 0
    for i in range(len(text)):

        for j in range(len(vowels)):

            if text[i] == vowels[j]:

                counter +=1

    return counter
```

**Test:** `count_vowels("Hallo Welt")` soll `3` zurückgeben (a, o, e)

### b) Listen-Manipulation (7 Punkte)

Schreiben Sie eine Funktion `remove_duplicates`, die Duplikate aus einer Liste entfernt und die ursprüngliche Reihenfolge beibehält.

```python
def remove_duplicates(items: list) -> list:




```

**Test:** `[1, 2, 2, 3, 1, 4]` wird zu `[1, 2, 3, 4]`

---

## Aufgabe 2: Einfache Klassen und Objekte (18 Punkte)

### a) Bankonto-Klasse (12 Punkte)

Implementieren Sie eine `BankAccount` Klasse mit folgenden Eigenschaften:

- Attribut `balance` (Kontostand)
- Methode `deposit(amount)` - Geld einzahlen
- Methode `withdraw(amount)` - Geld abheben (nur wenn genug da ist)
- Methode `get_balance()` - Kontostand abfragen

```python
class BankAccount:
    def __init__(self, initial_balance: float = 0):
		self.initial_balance = initial_balance
		self.balance = balance + self.initial_balance



    def deposit(self, amount: float) -> float:
		return self.balance + amount



    def withdraw(self, amount: float) -> bool:
        # Rückgabe: True wenn erfolgreich, False wenn nicht genug Geld
			if amount > self.balance:
				return False
			else:
				return True



    def get_balance(self) -> float:
		return self.balance



```

### b) Objektverwendung (6 Punkte)

Erstellen Sie ein Bankonto mit 100€ Startguthaben. Zahlen Sie 50€ ein und versuchen Sie 200€ abzuheben. Was passiert?

```python
# Konto erstellen:
kunde: BankAccount = BankAccount(100)
# 50€ einzahlen:
kunde.deposit(50)
# 200€ abheben versuchen:
kunde.withdraw(200)
# Erwartetes Ergebnis:
False
```

---

## Aufgabe 3: Kontrollstrukturen und Funktionen (20 Punkte)

### a) Verschachtelte Schleifen (8 Punkte)

Schreiben Sie eine Funktion `multiplication_table`, die das kleine Einmaleins (1x1 bis 10x10) ausgibt:

```python
def multiplication_table():

    for i in range(1,11):

        for j in range(1,11):# Ausgabe-Format: "3 x 4 = 12"

              print(i, "x", j, "=" ,i*j)



```

### b) Rekursion (12 Punkte)

Implementieren Sie eine rekursive Funktion `sum_digits`, die die Quersumme einer Zahl berechnet:

```python
def sum_digits(n: int) -> int:


    if n % 10 == 0:

        return n/10

    else:

        return sum_digits(n//10)



```

**Hinweis:** Verwenden Sie `n % 10` für die letzte Ziffer und `n // 10` für den Rest.

---

## Aufgabe 4: File-Verarbeitung und Exception Handling (17 Punkte)

### a) Sicheres Datei-Lesen (10 Punkte)

Schreiben Sie eine Funktion `safe_read_file`, die eine Datei liest und bei Fehlern eine leere Liste zurückgibt:

```python
def safe_read_file(filename: str) -> list[str]:
    # Liest Datei zeilenweise, fängt Fehler ab




```

### b) Eingabe-Validierung (7 Punkte)

Schreiben Sie eine Funktion `get_positive_number`, die so lange nach einer positiven Zahl fragt, bis eine gültige Eingabe gemacht wird:

```python
def get_positive_number() -> float:
    # Fragt User nach positiver Zahl, wiederholt bei Fehlern




```

---

## Teil B: Theoretische Fragen (30 Punkte)

## Aufgabe 5: Objektorientierte Programmierung (12 Punkte)

### a) Vererbung (6 Punkte)

Was ist Vererbung in der objektorientierten Programmierung? Geben Sie ein praktisches Beispiel mit einer Basisklasse und einer abgeleiteten Klasse.

### b) Kapselung (6 Punkte)

Warum sollte man Attribute einer Klasse "privat" machen? Wie macht man in Python ein Attribut privat?

---

## Aufgabe 6: Python-Spezifika (10 Punkte)

### a) List Comprehensions (5 Punkte)

Schreiben Sie eine List Comprehension, die alle geraden Quadratzahlen von 1 bis 20 erstellt:

```python
even_squares = # Ihre List Comprehension hier
```

### b) Lambda-Funktionen (5 Punkte)

Was ist eine Lambda-Funktion? Schreiben Sie eine Lambda-Funktion, die prüft, ob eine Zahl durch 3 teilbar ist.

---

## Aufgabe 7: Debugging und Code-Qualität (8 Punkte)

### a) Fehlersuche (4 Punkte)

Finden Sie die Fehler in folgendem Code:

```python
def calculate_average(numbers):
    total = 0
    for number in numbers:
        total += number
    average = total / len(numbers)
    return average

result = calculate_average([])
print(result)
```

**Fehler:** _________________

**Lösung:** _________________

### b) Code-Verbesserung (4 Punkte)

Wie könnte man folgenden Code lesbarer machen?

```python
def f(x):
    if x > 0:
        return x * 2
    else:
        return x * -1
```

**Verbesserter Code:**

---

**Ende der Klausur**

**Punkteverteilung:**

- Teil A (Programmierung): 70 Punkte
    - Aufgabe 1: 15 Punkte
    - Aufgabe 2: 18 Punkte
    - Aufgabe 3: 20 Punkte
    - Aufgabe 4: 17 Punkte
- Teil B (Theorie): 30 Punkte
    - Aufgabe 5: 12 Punkte
    - Aufgabe 6: 10 Punkte
    - Aufgabe 7: 8 Punkte

**Gesamt: 100 Punkte**


# Klausur Variante D - Komplette Lösungen


# Aufgabe 1: Strings und Listen (15 Punkte)

# a) String-Verarbeitung (8 Punkte)
def count_vowels(text: str) -> int:
    vowels = "aeiou"
    counter = 0
    for char in text.lower():
        if char in vowels:
            counter += 1
    return counter

# b) Listen-Manipulation (7 Punkte)
def remove_duplicates(items: list) -> list:
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result


# Aufgabe 2: Einfache Klassen und Objekte (18 Punkte)


# a) Bankonto-Klasse (12 Punkte)
class BankAccount:
    def __init__(self, initial_balance: float = 0):
        self.balance = initial_balance

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def withdraw(self, amount: float) -> bool:
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        return self.balance

# b) Objektverwendung (6 Punkte)
# Konto erstellen:
kunde = BankAccount(100)
# 50€ einzahlen:
kunde.deposit(50)  # Balance ist jetzt 150€
# 200€ abheben versuchen:
result = kunde.withdraw(200)  # False, weil nur 150€ da sind
# Erwartetes Ergebnis: False

# 
# Aufgabe 3: Kontrollstrukturen und Funktionen (20 Punkte)
# 

# a) Verschachtelte Schleifen (8 Punkte)
def multiplication_table():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")

# b) Rekursion (12 Punkte)
def sum_digits(n: int) -> int:
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_digits(n // 10)


# Aufgabe 4: File-Verarbeitung und Exception Handling (17 Punkte)


# a) Sicheres Datei-Lesen (10 Punkte)
def safe_read_file(filename: str) -> list[str]:
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except (FileNotFoundError, IOError):
        return []

# b) Eingabe-Validierung (7 Punkte)
def get_positive_number() -> float:
    while True:
        try:
            number = float(input("Geben Sie eine positive Zahl ein: "))
            if number > 0:
                return number
            else:
                print("Bitte geben Sie eine positive Zahl ein!")
        except ValueError:
            print("Ungültige Eingabe! Bitte geben Sie eine Zahl ein.")

# Theoretische Antworten


"""
Aufgabe 5a) Vererbung:
Vererbung ermöglicht es, neue Klassen basierend auf bestehenden Klassen zu erstellen.
Die neue Klasse (Kindklasse) erbt Attribute und Methoden der Basisklasse (Elternklasse).

Beispiel:
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def start(self):
        print("Fahrzeug startet")

class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors

Aufgabe 5b) Kapselung:
Private Attribute schützen interne Daten vor direktem Zugriff von außen.
In Python: Attribut mit einem Unterstrich beginnen (_private) oder zwei (__very_private)

Aufgabe 6a) List Comprehensions:
even_squares = [x**2 for x in range(1, 21) if x**2 % 2 == 0]

Aufgabe 6b) Lambda-Funktionen:
Lambda-Funktionen sind anonyme Funktionen für einfache Operationen.
divisible_by_3 = lambda x: x % 3 == 0

Aufgabe 7a) Fehlersuche:
Fehler: Division durch Null bei leerer Liste
Lösung: 
if len(numbers) == 0:
    return 0
average = total / len(numbers)

Aufgabe 7b) Code-Verbesserung:
def absolute_value_or_double(x):
    '''Returns double if positive, absolute value if negative'''
    if x > 0:
        return x * 2
    else:
        return abs(x)
"""