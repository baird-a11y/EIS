# Klausur: Einführung in die Softwareentwicklung
**Sommersemester 2025 · 07. August 2025**

---

## Angaben zur Person

**Vorname:** _________________ **Matrikelnummer:** _________________

**Nachname:** _________________

---

## Anleitung

Bitte lesen Sie sich die untenstehenden Hinweise sorgfältig durch, und folgen Sie der Anleitung!

• Sollten Sie sich gesundheitlich nicht in der Lage fühlen, die Prüfung anzutreten, dann melden Sie sich vor Beginn der Bearbeitung bei der Aufsicht.

• Die Klausur besteht aus **7 Aufgaben** auf insgesamt **12 einzelnen Seiten**. Prüfen Sie sofort, ob Sie ein vollständiges Exemplar erhalten haben.

• Beantworten Sie die Fragen direkt auf dem Aufgabenblatt. Falls Sie mehr Platz benötigen, nutzen Sie die Rückseite oder zusätzliche Blätter.

• Sie können maximal **100 Punkte** erreichen. Sie haben ab **50 Punkten** auf jeden Fall bestanden.

• Sie können die Fragen auf **Deutsch oder Englisch** beantworten.

• Sie haben **3 Stunden Zeit** für die Bearbeitung der Klausur.

• Sie dürfen **zwei von Ihnen selbst handbeschriebene DIN A4 Blätter** als Hilfsmittel nutzen.

**Wir wünschen Ihnen viel Erfolg bei der Klausur!**

---

## Aufgabe 1: Grundlagen der Programmierung (12 Punkte)

### a) Datentypen und Variablen (6 Punkte)

Gegeben ist folgender Python-Code:

```python
x = 42
y = "Hello"
z = 3.14
w = True
```

1. Geben Sie für jede Variable den Datentyp an:
   - x: int 
   - y: str
   - z: float 
   - w: bool

1. Was ist der Unterschied zwischen einer Variablen und einer Konstanten?

Der Wert der in einer Variablen gespeichert wird, kann sich während der Laufzeit ändern, sowie der Typ der Variable

### b) Typumwandlung (6 Punkte)

Schreiben Sie eine Python-Funktion `safe_convert`, die einen beliebigen Wert zu einem Integer konvertiert. Falls die Konvertierung nicht möglich ist, soll der Wert 0 zurückgegeben werden.

```python
from typing import Optional


def save_convert(value: Optional) -> int:

    if value is None: # Falls leer/None

        return 0

    elif isinstance(value, str): # Falls es ein String ist und ggf. eine Komma Zahl

        return round(float(value))

    elif isinstance(value, float): # Falls es nur eine Kommazahl ist

        return round(value)

    else:

        return value # Falls es schon ein Int war
```

---

## Aufgabe 2: Kontrollstrukturen (18 Punkte)

### a) Verzweigungen (8 Punkte)

Schreiben Sie ein Python-Programm, das eine Zahl vom Benutzer einliest und ausgibt, ob die Zahl positiv, negativ oder null ist.

```python
number: float = float(input("Gib hier eine Zahl ein")) # Eingabe von User muss konvertiert werden, da sie sonst vom Typ str ist.

if number == 0:
	print("Die Zahl ist 0")
elif number < 0:
	print("Die Zahl ist negativ")
else:
	print("Die Zahl ist postiv")
```

### b) Schleifen (10 Punkte)

Schreiben Sie eine Funktion `print_pattern`, die folgendes Muster ausgibt:

```
*
**
***
****
*****
```

Die Anzahl der Zeilen soll als Parameter übergeben werden.

```python
def print_pattern(n: int) -> None:
    for i in range(1,n+1):
	    for j in range(1,i+1):
		    print("*")
```

---

## Aufgabe 3: Funktionen und Parameter (16 Punkte)

### a) Funktionsdefinition (8 Punkte)

Schreiben Sie eine Funktion `calculate_area`, die die Fläche eines Rechtecks berechnet. Die Funktion soll zwei Parameter haben: `length` und `width`.

```python
def calculate_area(self, length: float, width: float) -> float:
    return self.length * self.width

```

### b) Default-Parameter (8 Punkte)

Erweitern Sie die Funktion `greet_user`, sodass sie einen optionalen Parameter `greeting` hat. Wenn kein Greeting übergeben wird, soll "Hello" verwendet werden.

```python
def greet_user(name: str, greeting = Optional) -> str: # Vervollständigen Sie die Signatur

    if greeting is None:

        print("Hello", name)

    else:

        print(greeting, name)
```

---

## Aufgabe 4: Listen und Datenstrukturen (20 Punkte)

### a) Listen-Operationen (10 Punkte)

Gegeben ist folgende Liste:
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

Schreiben Sie Code, der:
1. Alle geraden Zahlen aus der Liste extrahiert
2. Die Summe aller Zahlen berechnet
3. Das Maximum der Liste findet

```python
# 1. Gerade Zahlen:
even_numbers: list[int] = list(filter(lambda x: x%2==0, numbers))
# 2. Summe:
summe: int = reduce(lambda x,y: x+y, numbers)
# 3. Maximum:
max_number: int = reduce(filter(lambda x,y: x<y, numbers))
```

### b) Dictionary-Operationen (10 Punkte)

Erstellen Sie ein Dictionary `student`, das folgende Informationen speichert:
- Name: "Max Mustermann"
- Matrikelnummer: 12345
- Fächer: ["Mathematik", "Informatik", "Physik"]

Schreiben Sie dann Code, der ein neues Fach "Chemie" zur Fächerliste hinzufügt.

```python
# Dictionary erstellen:
student: dict[str,int, list[str]] = {

    "Name": "Max Mustermann",

    "Martikelnummer": 12345,

    "Fächer": ["Mathe","Informatik","Physik"]

}
student["Fächer"].append("Chemie")


```

---

## Aufgabe 5: Objektorientierte Programmierung (20 Punkte)

### a) Klassendefinition (12 Punkte)

Definieren Sie eine Klasse `Car` mit folgenden Eigenschaften:
- Attribute: `brand`, `model`, `year`
- Methode `get_info()`, die eine formatierte Beschreibung des Autos zurückgibt

```python
class Car:

    def __init__(self, brand: str, model: str, year: int) -> None:

        self.brand = brand

        self.model = model

        self.year = year

    def get_info(self) -> None:

        print("Bei dem Auto handelt es sich im ein", self.brand, ",Model", self.model, "aus dem Jahre", self.year)
```

### b) Objekterstellung und -verwendung (8 Punkte)

Erstellen Sie ein Objekt der Klasse `Car` und rufen Sie die `get_info()`-Methode auf.

```python
auto: Car = Car("Ford","Mustang",1970)
Car.get_info(auto)
```

---

## Aufgabe 6: Fehlerbehandlung und Debugging (10 Punkte)

### a) Exception Handling (10 Punkte)

Schreiben Sie eine Funktion `safe_division`, die zwei Zahlen dividiert. Die Funktion soll eine Division durch Null abfangen und in diesem Fall `None` zurückgeben.

```python
def safe_division(a: int, b: int) -> float:
	if b == 0:
		return None
	else:
		return a:b
    
```

---

## Aufgabe 7: Theoretische Fragen (4 Punkte)

### a) Software-Entwicklung (2 Punkte)

Was versteht man unter dem Begriff "Debugging" und nennen Sie zwei wichtige Strategien beim Debugging.

Das suchen und auffinden von Fehlern im Code, wie falsche oder fehlende Rückgabe von Werte.

Entweder man nutzt dafür spezielle Datensätze bei denen man den Ausgang kennt oder man baut bestimmte print() Statements ein, die den aktuellen zustand ausgeben.

### b) Code-Qualität (2 Punkte)

Warum ist es wichtig, Code zu kommentieren? Nennen Sie zwei Vorteile.

Verständlichkeit bei komplexeren Funktionen
Dokumentation für späteres Erweitern oder Weiterarbeiten

---

**Ende der Klausur**

**Punkteverteilung:**
- Aufgabe 1: 12 Punkte
- Aufgabe 2: 18 Punkte  
- Aufgabe 3: 16 Punkte
- Aufgabe 4: 20 Punkte
- Aufgabe 5: 20 Punkte
- Aufgabe 6: 10 Punkte
- Aufgabe 7: 4 Punkte

**Gesamt: 100 Punkte**


# Klausurbewertung: Einführung in die Softwareentwicklung

## Gesamtergebnis: 71/100 Punkte ✅ **BESTANDEN**

---

## Aufgabe 1: Grundlagen der Programmierung (9/12 Punkte)

### a) Datentypen und Variablen (6/6 Punkte) ✅

- **Datentypen:** Alle korrekt! (int, str, float, bool)
- **Variable vs. Konstante:** ✅ Richtige Erklärung - Variablen können sich ändern, inklusive des Typs

### b) Typumwandlung (3/6 Punkte) ⚠️

**Fehler:**

- Funktionsname: `save_convert` statt `safe_convert` (-0,5 Punkte)
- `Optional` ohne Import verwendet (-0,5 Punkte)
- Exception Handling fehlt für ungültige String-Konvertierungen (-2 Punkte)

**Korrigierte Version:**

```python
def safe_convert(value) -> int:
    try:
        if value is None:
            return 0
        return int(float(value))  # Wandelt auch Strings um
    except (ValueError, TypeError):
        return 0
```

---

## Aufgabe 2: Kontrollstrukturen (14/18 Punkte)

### a) Verzweigungen (8/8 Punkte) ✅

- Perfekte Lösung! Korrekte Eingabe, Typkonvertierung und Verzweigungslogik
- Guter Kommentar zur String-Konvertierung

### b) Schleifen (6/10 Punkte) ⚠️

**Fehler:**

- `print("*")` gibt jedes `*` in neue Zeile aus (-2 Punkte)
- Verschachtelte Schleifen unnötig kompliziert (-2 Punkte)

**Korrigierte Version:**

```python
def print_pattern(n: int) -> None:
    for i in range(1, n+1):
        print("*" * i)  # Einfacher und korrekter
```

---

## Aufgabe 3: Funktionen und Parameter (6/16 Punkte)

### a) Funktionsdefinition (2/8 Punkte) ❌

**Schwere Fehler:**

- `self` Parameter bei normaler Funktion (-3 Punkte)
- `self.length` und `self.width` existieren nicht (-3 Punkte)

**Korrigierte Version:**

```python
def calculate_area(length: float, width: float) -> float:
    return length * width
```

### b) Default-Parameter (4/8 Punkte) ⚠️

**Fehler:**

- Syntax `greeting = Optional` ist falsch (-2 Punkte)
- Funktion gibt nichts zurück, obwohl Return-Typ angegeben (-2 Punkte)

**Korrigierte Version:**

```python
def greet_user(name: str, greeting: str = "Hello") -> None:
    print(greeting, name)
```

---

## Aufgabe 4: Listen und Datenstrukturen (18/20 Punkte)

### a) Listen-Operationen (8/10 Punkte) ✅

**Gut gelöst:**

- Gerade Zahlen: ✅ Korrekt mit `filter` und Lambda
- Summe: ✅ `reduce` ist korrekt (Import wird als gegeben angenommen)
- Maximum: ❌ Falsche `reduce`-Verwendung - sollte `max()` oder `reduce(lambda x,y: x if x>y else y, numbers)` sein (-2 Punkte)

**Korrigierte Version:**

```python
# 1. Gerade Zahlen: ✅ Richtig
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# 2. Summe:
summe = sum(numbers)  # Oder: from functools import reduce

# 3. Maximum:
max_number = max(numbers)  # Oder: reduce(lambda x,y: x if x>y else y, numbers)
```

### b) Dictionary-Operationen (10/10 Punkte) ✅

- Dictionary-Erstellung: ✅ Korrekt (trotz kleinem Tippfehler "Martikelnummer")
- Fach hinzufügen: ✅ Perfekt mit `append()`

---

## Aufgabe 5: Objektorientierte Programmierung (16/20 Punkte)

### a) Klassendefinition (10/12 Punkte) ✅

- `__init__` Methode: ✅ Korrekt
- Attribute: ✅ Richtig zugewiesen
- `get_info()`: ⚠️ Funktioniert, aber könnte eleganter sein (-2 Punkte)

**Verbesserung:**

```python
def get_info(self) -> str:
    return f"Auto: {self.brand} {self.model} ({self.year})"
```

### b) Objekterstellung (6/8 Punkte) ✅

- Objekt erstellt: ✅ Korrekt
- Methodenaufruf: ⚠️ `Car.get_info(auto)` funktioniert, aber `auto.get_info()` wäre üblicher (-2 Punkte)

---

## Aufgabe 6: Fehlerbehandlung (6/10 Punkte)

### Exception Handling (6/10 Punkte) ⚠️

**Fehler:**

- Syntax-Fehler: `a:b` statt `a/b` (-2 Punkte)
- Kein `try-except` für robuste Fehlerbehandlung (-2 Punkte)

**Korrigierte Version:**

```python
def safe_division(a: int, b: int) -> float:
    try:
        if b == 0:
            return None
        return a / b  # Nicht a:b
    except:
        return None
```

---

## Aufgabe 7: Theoretische Fragen (2/4 Punkte)

### a) Software-Entwicklung (2/2 Punkte) ✅

- Definition von Debugging: ✅ Korrekt
- Strategien: ✅ Testdaten und Print-Statements sind gute Beispiele

### b) Code-Qualität (0/2 Punkte) ⚠️

- Nur ein Vorteil genannt statt zwei (-2 Punkte)
- "Verständlichkeit" und "Dokumentation" sind im Grunde dasselbe

**Bessere Antwort:** Verständlichkeit für andere Entwickler + Wartbarkeit/Debugging-Unterstützung

---

## Zusammenfassung der Hauptfehler:

1. **Syntax-Fehler:** `a:b` statt `a/b`, falsche Default-Parameter-Syntax
2. **Konzeptfehler:** `self` bei normalen Funktionen verwenden
3. **Fehlende Imports:** ~~`reduce` ohne `functools` Import~~ (Imports als gegeben angenommen)
4. **Print vs. Return:** Funktionen die etwas ausgeben vs. zurückgeben

## Positive Aspekte:

- Gute Verwendung von Type Hints
- Verständnis von Listen-Operationen und Lambda-Funktionen
- Solide Kenntnisse in OOP-Grundlagen
- Korrekte Kontrollstrukturen

**Note: 2,3 (71/100 Punkte)**

Mit etwas mehr Übung bei Syntax-Details und Exception Handling können Sie leicht eine bessere Note erreichen!