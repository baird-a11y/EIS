# Klausur: Einführung in die Softwareentwicklung
**Sommersemester 2025 · 07. August 2025 (Variante B)**

---

## Angaben zur Person

**Vorname:** _________________ **Matrikelnummer:** _________________

**Nachname:** _________________

---

## Anleitung

Bitte lesen Sie sich die untenstehenden Hinweise sorgfältig durch, und folgen Sie der Anleitung!

• Die Klausur besteht aus **7 Aufgaben** auf insgesamt **11 einzelnen Seiten**.

• Sie können maximal **100 Punkte** erreichen. Sie haben ab **50 Punkten** auf jeden Fall bestanden.

• **Programmiersprachen:** Alle Programmieraufgaben können wahlweise in **Python oder Scala** gelöst werden (außer wenn anders angegeben).

• **Imports:** Alle Inhalte der Python-Standardmodule, dataclasses, abc, typing und math können ohne expliziten import genutzt werden.

• Sie haben **3 Stunden Zeit** für die Bearbeitung der Klausur.

• Sie dürfen **zwei von Ihnen selbst handbeschriebene DIN A4 Blätter** als Hilfsmittel nutzen.

**Wir wünschen Ihnen viel Erfolg bei der Klausur!**

---

## Teil A: Programmieraufgaben (70 Punkte)

## Aufgabe 1: Arrays und Strings (12 Punkte)

### a) String-Filterung (8 Punkte)

Schreiben Sie eine Funktion `print_words_starting_with`, die ein Array von Strings als Eingabe bekommt und alle Einträge auf der Konsole ausgibt, die mit einem bestimmten Buchstaben beginnen. Leere Strings sollen ignoriert werden.

**Beispiel:** `print_words_starting_with(["apple", "banana", "", "avocado", "cherry"], "a")` 
soll ausgeben:
```
apple
avocado
```

**Python:**
```python
def print_words_starting_with(words: list[str], letter: str) -> None:

    starting_words: list[str] = [] #Leere Liste

    for i in range(len(words)):

        starting_letter = words[i][0]

        if starting_letter == letter:

            starting_words.append(words[i])

            return starting_words
```

**Scala:**
```scala
def printWordsStartingWith(words: Array[String], letter: String): Unit = {
    // Ihre Lösung hier
}
```

### b) Array-Manipulation (4 Punkte)

Was gibt folgender Python-Code aus? Begründen Sie Ihre Antwort.

```python
numbers = [1, 2, 3, 4, 5]
numbers[1:3] = [10, 20, 30]
print(numbers)
```

**Ausgabe:** [1, 10, 20, 30, 4, 5]

**Begründung:**  Ich überschreibe die Einträge mit den Index zwischen 1 und 3 mit den neuen Werten. Der Reist bleibt gleich. Heißt die 2 fällt weg

---

## Aufgabe 2: Objektorientiertes Design (18 Punkte)

### a) Klassen und Vererbung (12 Punkte)

Implementieren Sie eine Basisklasse `Vehicle` und eine abgeleitete Klasse `Car`:

- `Vehicle` soll Attribute `brand` und `year` haben
- `Vehicle` soll eine Methode `get_age()` haben, die das Alter berechnet (2025 - year)
- `Car` soll zusätzlich das Attribut `doors` haben
- `Car` soll die Methode `get_info()` haben, die alle Informationen formatiert zurückgibt

**Python:**
```python
class Vehicle:
    def __init__(self, brand: str, year: int) -> None:
	    self.brand = brand
	    self.year = year

	def get_age(self) -> None:
		print(2025 - self.year)

class Car(Vehicle):
    def super().__init__(self, brand, year, door: int) -> None:
	    self.door = door

	def get_info(self) -> None:
		return f"Auto: {self.brand} {get_age(self.year)} {self.door}"
	
```

### b) Objektverwendung (6 Punkte)

Erstellen Sie ein `Car`-Objekt mit den Werten: brand="BMW", year=2020, doors=4
Rufen Sie dann beide Methoden auf und geben Sie das erwartete Ergebnis an.

```python
# Objekterstellung:
auto: Car = Vehicle("B;W", 2020, 4)
auto.get_age()
auto.get_info()

# Methodenaufrufe und erwartete Ausgaben:
5
"Auto: BMW 5 4"
```

---

## Aufgabe 3: Funktionale Programmierung (20 Punkte)

### a) Lambda-Funktionen und Higher-Order Functions (12 Punkte)

Gegeben ist folgende Liste von Studierenden:
```python
students = [
    {"name": "Anna", "grade": 1.7, "credits": 120},
    {"name": "Bob", "grade": 2.3, "credits": 90},
    {"name": "Clara", "grade": 1.2, "credits": 150},
    {"name": "David", "grade": 3.1, "credits": 60}
]
```

Schreiben Sie Code, der:
1. Alle Studierenden mit Note besser als 2.0 filtert
2. Die Namen dieser Studierenden extrahiert
3. Die Gesamtzahl der Credits aller gefilterten Studierenden berechnet

Verwenden Sie `filter()`, `map()` und `reduce()` bzw. entsprechende Lambda-Funktionen.

```python
# 1. Filtern:
students: list[str] = list(filter(lambda x: x["grade"]<2.0, students))
# 2. Namen extrahieren:
student_names: list[str] = reduce(lambda x: x["name"], students)
# 3. Credits summieren:
credit_sum: int = reduce(lambda x,y,z: x+y, students["credits"])

```

### b) Rekursion (8 Punkte)

Implementieren Sie eine rekursive Funktion `fibonacci(n)`, die die n-te Fibonacci-Zahl berechnet.

```python
def fibonacci(n: int) -> int:
    if n == 0:
	    return 0
	elif n == 1:
		return 1
	else
		return fibonacci(n-2) + fibonacci(n-1)
```

---

## Aufgabe 4: GUI-Programmierung (20 Punkte)

### a) Event-Handler Design (12 Punkte)

Entwerfen Sie die Struktur einer einfachen Taschenrechner-GUI mit folgenden Komponenten:
- Eingabefeld für Zahlen
- Buttons für +, -, *, /
- Ergebnis-Anzeige

Implementieren Sie einen Event-Handler für den Plus-Button (Pseudocode ist erlaubt, wenn Sie die genaue Syntax vergessen haben).

```python
class MyWindow(QMainWindow):
	def __init__(self, parent: QWidget):
		super().__init()__(parent)
		self.setWindowTitel("Taschenrechner")
		self.setMinimumSize(400,600)
		self.my_frame = QFrame(self)
		self.setCentralWidget(self.my_frame)
		self.my_layout = QVBoxLayout(self.my_frame)
		self.my_frame.setLayout(self.my_layout)
	
```

### b) Event-orientierte Programmierung Konzepte (8 Punkte)

Erklären Sie den Unterschied zwischen:
1. **Ereignisgesteuerter** und **sequenzieller** Programmierung

Bei ersterem wird der Code nur ausgeführt, wenn z.B die Taste gedrückt wird oder das Feld aufgerufen wird. 


2. **Callback-Funktionen** und **normale Funktionen**



**Antwort:**

---

## Teil B: Theoretische Fragen (30 Punkte)

## Aufgabe 5: Programmiersprachen-Vergleich (12 Punkte)

### a) Typsysteme (6 Punkte)

Vergleichen Sie die Typsysteme von Python und C++. Welche Vor- und Nachteile hat statische vs. dynamische Typisierung?

dynamische hat den Vorteil, dass ich Funktionen zum Beispiel für unterschiedliche Typen nutzen kann auf kosten von Performance
statische hat den Vorteil, dass ich weniger Fehler mache und es leichter zu debuggen ist

### b) Speicherverwaltung (6 Punkte)

Warum sind C++ Pointer "gefährlicher" als Python Referenzen? Nennen Sie zwei konkrete Gefahren.

Ich kann entweder den Pointer nicht bewegt haben oder diese zeigt auf einen alten oder leeren Speicher

---

## Aufgabe 6: Software-Engineering Konzepte (10 Punkte)

### a) Code-Qualität (5 Punkte)

Was versteht man unter "Clean Code"? Nennen Sie drei Prinzipien für sauberen Code.

Clean Code bedeutet der Code hält sich an bestimmte Vorgaben, was Lesbarkeit, Verständlichkeit und Wartbarkeit betrifft.

So sollen Funktionen und Variablen immer so benannt werden das sie selbst erklärend sind was sie speichern oder tun

### b) Testing (5 Punkte)

Was ist der Unterschied zwischen Unit-Tests und Integrationstests? Wann würden Sie welchen Ansatz wählen?

Unit Test bedeutet ich habe vorgegeben Fälle und prüfe ob meine Ausgabe diesem entspricht
Integrationstest prüfen ob der Code abschnitt zum rest passt und einbettbar ist

---

## Aufgabe 7: Datenstrukturen und Algorithmen (8 Punkte)

### a) Komplexitätsanalyse (4 Punkte)

Bestimmen Sie die Zeitkomplexität (Big-O) folgender Operationen:
- Suchen in einer unsortierten Liste: O(n^2)
- Einfügen in eine sortierte Liste: O(n)

### b) Datenstruktur-Wahl (4 Punkte)

Sie müssen häufig prüfen, ob ein Element in einer Sammlung enthalten ist. Welche Datenstruktur würden Sie wählen und warum?

Dictonary, weil ich die Elemente dann Gruppieren kann und schneller innerhalb der Gruppe das finde

---

**Ende der Klausur**

**Punkteverteilung:**
- Teil A (Programmierung): 70 Punkte
  - Aufgabe 1: 12 Punkte
  - Aufgabe 2: 18 Punkte  
  - Aufgabe 3: 20 Punkte
  - Aufgabe 4: 20 Punkte
- Teil B (Theorie): 30 Punkte
  - Aufgabe 5: 12 Punkte
  - Aufgabe 6: 10 Punkte
  - Aufgabe 7: 8 Punkte

**Gesamt: 100 Punkte**


# Klausurbewertung: Einführung in die Softwareentwicklung (Variante B)

## Gesamtergebnis: 56/100 Punkte ✅ **BESTANDEN**

---

## Teil A: Programmieraufgaben (35/70 Punkte)

## Aufgabe 1: Arrays und Strings (6/12 Punkte)

### a) String-Filterung (2/8 Punkte) ❌

**Schwere Fehler:**

- Funktion soll `print` ausgeben, aber Sie `return` eine Liste (-3 Punkte)
- `return` beendet die Funktion nach erstem Match (-2 Punkte)
- Leere Strings werden nicht abgefangen (`words[i][0]` würde Fehler werfen) (-1 Punkt)

**Korrigierte Version:**

```python
def print_words_starting_with(words: list[str], letter: str) -> None:
    for word in words:
        if word and word[0].lower() == letter.lower():  # Prüfung auf leere Strings
            print(word)
```

### b) Array-Manipulation (4/4 Punkte) ✅

- **Ausgabe:** Korrekt! `[1, 10, 20, 30, 4, 5]`
- **Begründung:** ✅ Richtig erkannt, dass Slice-Assignment die Elemente ersetzt

---

## Aufgabe 2: Objektorientiertes Design (8/18 Punkte)

### a) Klassen und Vererbung (6/12 Punkte) ⚠️

**Teilweise richtig:**

- `Vehicle.__init__`: ✅ Korrekt implementiert
- `Vehicle.get_age()`: ⚠️ Sollte Wert `return`, nicht `print` (-2 Punkte)
- `Car.__init__`: ❌ `super().__init__` Syntax falsch (-2 Punkte)
- `Car.get_info()`: ❌ Funktionsaufruf falsch (-2 Punkte)

**Korrigierte Version:**

```python
class Vehicle:
    def __init__(self, brand: str, year: int) -> None:
        self.brand = brand
        self.year = year
    
    def get_age(self) -> int:  # Return statt print
        return 2025 - self.year

class Car(Vehicle):
    def __init__(self, brand: str, year: int, doors: int) -> None:
        super().__init__(brand, year)  # Richtige super() Syntax
        self.doors = doors
    
    def get_info(self) -> str:
        return f"Auto: {self.brand} {self.get_age()} Jahre {self.doors} Türen"
```

### b) Objektverwendung (2/6 Punkte) ⚠️

**Fehler:**

- Objekterstellung: `Vehicle` statt `Car` verwendet (-2 Punkte)
- `Vehicle` hat keinen `doors` Parameter (-2 Punkte)

---

## Aufgabe 3: Funktionale Programmierung (12/20 Punkte)

### a) Lambda-Funktionen (4/12 Punkte) ⚠️

**Teilweise richtig:**

- Filtern: ✅ Korrekt mit Lambda-Funktion
- Namen extrahieren: ❌ `reduce` falsch verwendet, sollte `map` sein (-4 Punkte)
- Credits summieren: ❌ Syntax und Logik falsch (-4 Punkte)

**Korrigierte Version:**

```python
# 1. Filtern: ✅ Richtig
good_students = list(filter(lambda x: x["grade"] < 2.0, students))

# 2. Namen extrahieren:
names = list(map(lambda x: x["name"], good_students))

# 3. Credits summieren:
total_credits = reduce(lambda x, y: x + y["credits"], good_students, 0)
```

### b) Rekursion (8/8 Punkte) ✅

- **Perfekt!** Korrekte Implementierung der Fibonacci-Funktion
- Basis-Fälle und rekursiver Aufruf alle richtig

---

## Aufgabe 4: GUI-Programmierung (9/20 Punkte)

### a) Event-Handler Design (7/12 Punkte) ⚠️

**Gut begonnen:**

- GUI-Struktur mit QMainWindow: ✅ Grundstruktur richtig
- Layout-Setup: ✅ Korrekt
- Event-Handler für Plus-Button fehlt komplett (-5 Punkte)

```python
from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, 
                               QHBoxLayout, QLineEdit, QPushButton, 
                               QLabel, QGridLayout)
from PySide6.QtCore import Qt

class CalculatorWindow(QMainWindow):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.setWindowTitle("Taschenrechner")
        self.setMinimumSize(300, 400)
        
        # Zentrales Widget und Layout
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # GUI-Komponenten erstellen
        self.setup_ui()
        
        # Event-Handler verbinden
        self.connect_events()
    
    def setup_ui(self):
        # Eingabefelder für Zahlen
        self.input1 = QLineEdit()
        self.input1.setPlaceholderText("Erste Zahl eingeben...")
        self.main_layout.addWidget(QLabel("Erste Zahl:"))
        self.main_layout.addWidget(self.input1)
        
        self.input2 = QLineEdit()
        self.input2.setPlaceholderText("Zweite Zahl eingeben...")
        self.main_layout.addWidget(QLabel("Zweite Zahl:"))
        self.main_layout.addWidget(self.input2)
        
        # Buttons für Operationen
        button_layout = QHBoxLayout()
        self.plus_button = QPushButton("+")
        self.minus_button = QPushButton("-")
        self.multiply_button = QPushButton("*")
        self.divide_button = QPushButton("/")
        
        button_layout.addWidget(self.plus_button)
        button_layout.addWidget(self.minus_button)
        button_layout.addWidget(self.multiply_button)
        button_layout.addWidget(self.divide_button)
        
        self.main_layout.addLayout(button_layout)
        
        # Ergebnis-Anzeige
        self.main_layout.addWidget(QLabel("Ergebnis:"))
        self.result_label = QLabel("Hier erscheint das Ergebnis")
        self.result_label.setStyleSheet("font-size: 16px; font-weight: bold; "
                                       "border: 1px solid gray; padding: 10px;")
        self.result_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.result_label)
        
        # Clear Button
        self.clear_button = QPushButton("Löschen")
        self.main_layout.addWidget(self.clear_button)
    
    def connect_events(self):
        """Event-Handler mit Buttons verbinden"""
        self.plus_button.clicked.connect(self.on_plus_clicked)
        self.minus_button.clicked.connect(self.on_minus_clicked)
        self.multiply_button.clicked.connect(self.on_multiply_clicked)
        self.divide_button.clicked.connect(self.on_divide_clicked)
        self.clear_button.clicked.connect(self.on_clear_clicked)
    
    # Event-Handler Methoden (Callback-Funktionen!)
    def on_plus_clicked(self):
        """Event-Handler für Plus-Button"""
        try:
            # Werte aus Eingabefeldern holen
            num1 = float(self.input1.text())
            num2 = float(self.input2.text())
            
            # Berechnung durchführen
            result = num1 + num2
            
            # Ergebnis anzeigen
            self.result_label.setText(f"{num1} + {num2} = {result}")
            
        except ValueError:
            # Fehlerbehandlung für ungültige Eingaben
            self.result_label.setText("Fehler: Bitte gültige Zahlen eingeben!")
        except Exception as e:
            self.result_label.setText(f"Unerwarteter Fehler: {str(e)}")
    
    def on_minus_clicked(self):
        """Event-Handler für Minus-Button"""
        try:
            num1 = float(self.input1.text())
            num2 = float(self.input2.text())
            result = num1 - num2
            self.result_label.setText(f"{num1} - {num2} = {result}")
        except ValueError:
            self.result_label.setText("Fehler: Bitte gültige Zahlen eingeben!")
    
    def on_multiply_clicked(self):
        """Event-Handler für Multiplikation-Button"""
        try:
            num1 = float(self.input1.text())
            num2 = float(self.input2.text())
            result = num1 * num2
            self.result_label.setText(f"{num1} × {num2} = {result}")
        except ValueError:
            self.result_label.setText("Fehler: Bitte gültige Zahlen eingeben!")
    
    def on_divide_clicked(self):
        """Event-Handler für Division-Button"""
        try:
            num1 = float(self.input1.text())
            num2 = float(self.input2.text())
            
            # Division durch Null abfangen
            if num2 == 0:
                self.result_label.setText("Fehler: Division durch Null!")
                return
            
            result = num1 / num2
            self.result_label.setText(f"{num1} ÷ {num2} = {result}")
            
        except ValueError:
            self.result_label.setText("Fehler: Bitte gültige Zahlen eingeben!")
    
    def on_clear_clicked(self):
        """Event-Handler für Clear-Button"""
        self.input1.clear()
        self.input2.clear()
        self.result_label.setText("Hier erscheint das Ergebnis")

# Verwendung:
if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    import sys
    
    app = QApplication(sys.argv)
    calculator = CalculatorWindow()
    calculator.show()
    sys.exit(app.exec())
```

**Fehlender Event-Handler:**

```python
def on_plus_clicked(self):
    # Zahlen aus Eingabefeldern holen und addieren
    result = float(self.input1.text()) + float(self.input2.text())
    self.result_label.setText(str(result))
```

### b) Event-Konzepte (2/8 Punkte) ⚠️

- **Ereignisgesteuert vs. Sequenziell:** ✅ Richtig erklärt (2 Punkte)
- **Callback vs. normale Funktionen:** Keine Antwort gegeben (-6 Punkte)

### **Kernunterschied:**

|**Normale Funktion**|**Callback-Funktion**|
|---|---|
|**Sie** rufen auf|**System** ruft auf|
|Sofortige Ausführung|Spätere Ausführung|
|Vorhersagbarer Zeitpunkt|Unvorhersagbarer Zeitpunkt|
|Sequenziell|Ereignisgesteuert|

---

## Teil B: Theoretische Fragen (21/30 Punkte)

## Aufgabe 5: Programmiersprachen-Vergleich (8/12 Punkte)

### a) Typsysteme (4/6 Punkte) ✅

- **Dynamische Typisierung:** ✅ Flexibilität vs. Performance richtig erkannt
- **Statische Typisierung:** ✅ Fehlerprävention und Debugging-Vorteile genannt
- Etwas knapp, aber korrekt (-2 Punkte)

### b) Speicherverwaltung (4/6 Punkte) ✅

- **Pointer-Gefahren:** ✅ Dangling Pointer und Null-Pointer richtig identifiziert
- Antwort etwas ungenau formuliert (-2 Punkte)

---

## Aufgabe 6: Software-Engineering (6/10 Punkte)

### a) Code-Qualität (3/5 Punkte) ⚠️

- **Clean Code Definition:** ✅ Lesbarkeit, Verständlichkeit, Wartbarkeit richtig
- **Prinzipien:** Nur eines genannt (selbsterklärende Namen), zwei weitere fehlen (-2 Punkte)

**Fehlende Prinzipien:** Kleine Funktionen, DRY (Don't Repeat Yourself), Single Responsibility

### b) Testing (3/5 Punkte) ✅

- **Unit-Tests:** ✅ Richtig verstanden
- **Integrationstests:** ✅ Korrekt erklärt
- Wann welchen Ansatz wählen fehlt (-2 Punkte)
  
  ### **Praktische Entscheidungsregeln:**

|**Situation**|**Wähle**|**Grund**|
|---|---|---|
|Neue mathematische Funktion|**Unit-Test**|Schnell, isoliert, viele Edge-Cases|
|Login-System mit Datenbank|**Integrations-Test**|DB + Authentifizierung + Session|
|Bug in einer Sortierfunktion|**Unit-Test**|Schnell reproduzierbar und fixbar|
|Kompletter Bestellprozess|**Integration-Test**|Viele Komponenten beteiligt|
|Performance-kritische Funktion|**Unit-Test**|Isoliert messbar|
|Cross-Browser Kompatibilität|**Integration-Test**|Reale Browser-Umgebung nötig|

### **Goldene Regel:**

- **Unit-Tests:** "Funktioniert mein Code richtig?"
- **Integrationstests:** "Funktioniert mein System richtig?"

---

## Aufgabe 7: Algorithmen (4/8 Punkte)

### a) Komplexitätsanalyse (2/4 Punkte) ⚠️

- **Suchen in unsortierten Liste:** ❌ O(n), nicht O(n²) (-1 Punkt)
- **Einfügen in sortierte Liste:** ✅ O(n) ist korrekt (-1 Punkt für unvollständige Begründung)

### b) Datenstruktur-Wahl (2/4 Punkte) ⚠️

- **Dictionary:** Nicht optimal für "Element enthalten" Prüfung
- **Bessere Antwort:** Set (O(1) für Membership-Test) (-2 Punkte)

Die Kernbotschaft: **Hash-basierte Datenstrukturen (Set/Dictionary) sind unschlagbar für "Element enthalten" Prüfungen!**

---

## Zusammenfassung der Hauptfehler:

1. **Funktionsverhalten:** Verwechslung von `print` vs. `return`
2. **Syntax-Details:** `super()` Aufruf, `reduce` vs. `map` Unterscheidung
3. **Vollständigkeit:** Viele Antworten zu kurz oder unvollständig
4. **Algorithmus-Komplexität:** Zeitkomplexität von Suchoperationen

## Positive Aspekte:

- **Rekursion:** Perfekt beherrscht!
- **OOP-Grundlagen:** Konzepte verstanden, nur Syntax-Probleme
- **Filteroperationen:** Lambda-Funktionen gut eingesetzt
- **Theoretisches Verständnis:** Solide Grundkenntnisse vorhanden

**Note: 3,3 (56/100 Punkte)**

Diese Klausur war deutlich schwieriger als die erste. Mit mehr Übung bei GUI-Programmierung, funktionaler Programmierung und präziseren Antworten bei Theoriefragen können Sie sich stark verbessern!