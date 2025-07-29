## 🔧 **ÜBUNGSBLATT 01: Systemumgebung & Programmiersprachen**

### **Theorie-Aufgaben**

#### **T1.1: Programmiersprachen-Vergleich (20 Punkte)**

Erkläre die Hauptunterschiede zwischen den vier Programmiersprachen des Kurses:

a) **Typisierung**: Vergleiche die Typsysteme von Python, Java, C++ und Scala

Python wird Interpretiert, während die anderen Kompliziert werden
Python ist dynamisch

**Verbesserung:**

- **Python**: Dynamisch typisiert, interpretiert ✅
- **Java**: Statisch typisiert, kompiliert zu Bytecode, läuft auf JVM
- **C++**: Statisch typisiert, kompiliert zu Maschinencode
- **Scala**: Statisch typisiert, kompiliert zu Bytecode, läuft auf JVM
- **Zusatz**: Statisch = Typen zur Compile-Zeit bekannt, Dynamisch = Typen zur Laufzeit

b) **Performance**: Warum ist C++ typischerweise schneller als Python? 

Wird in Maschinensprache übersetzt

**Deine Antwort:** ✅ Korrekt! C++ wird direkt in Maschinensprache übersetzt, Python wird interpretiert.

**Ergänzung:** Python hat zusätzlich Overhead durch dynamische Typisierung und Interpreter-Layer.

c) **Paradigmen**: Welche Programmierparadigmen unterstützt jede Sprache? 

C++ Funktion und OOP
Scala Funktional und OOP
Java OOP
Python Funktional und OOP

**Deine Antworten:**

- C++ Funktional und OOP ✅
- Scala Funktional und OOP ✅
- Java OOP ✅ (aber auch etwas funktional seit Java 8)
- Python Funktional und OOP ✅

**Ergänzung:** Alle unterstützen auch **prozedurales** Programmieren!

d) **Einsatzgebiete**: Nenne typische Anwendungsbereiche für jede Sprache

- **Python**: Data Science, Web-Development, Scripting, AI/ML
- **Java**: Enterprise-Anwendungen, Android-Apps, Web-Backend
- **C++**: Systemnahe Programmierung, Games, Embedded Systems
- **Scala**: Big Data (Spark), funktionale Web-Services

#### **T1.2: Rekursion vs. Iteration (15 Punkte)**

a) Erkläre den Unterschied zwischen Rekursion und Iteration

Bei Iteration wird für eine vorgegebene Länge eine Sache wiederholt und die Ergebnisse direkt berechnet 
Bei Rekursion wird die Funktion solange erneut aufgerufen bis ein Abbruchkriterium erreicht wurde und dann werden die Ergebnisse eingesammelt und zurück gegeben

b) Welche Vor- und Nachteile haben beide Ansätze?

Iteration hat den Vorteil, dass ich eine kläre länge habe, während Rekursion besser bei flexiblen Problemen ist

**Bessere Antwort:**

- **Iteration:**
    - ✅ Speicher-effizient (kein Stack-Overhead)
    - ✅ Meist schneller
    - ❌ Manchmal komplexer zu verstehen
- **Rekursion:**
    - ✅ Eleganter Code bei baumartig-strukturierten Problemen
    - ✅ Natürlicher bei selbst-ähnlichen Problemen
    - ❌ Stack-Overflow Risiko
    - ❌ Langsamer durch Funktionsaufrufe

c) Wann sollte man Rekursion verwenden, wann Iteration?

Iteration wenn ich eine feste Schritt Anzahl habe und das Problem nicht zu groß ist

**Besser:**

- **Rekursion**: Bäume, Fraktale, Divide-and-Conquer, mathematische Definitionen
- **Iteration**: Einfache Zählschleifen, große Datenmengen, Performance-kritisch
#### **T1.3: Primzahltest-Algorithmus (15 Punkte)**

a) Erkläre den Sieve of Eratosthenes Algorithmus

Ich entferne alle Vielfache einer Primzahl beginnend mit der 2

b) Was ist die Zeitkomplexität des Algorithmus? 

**Deine Antwort:** O(n²) ❌

**Korrekt:** O(n log log n)

- Viel besser als O(n²)!
- Daher ist der Sieve so effizient

c) Wie könnte man ihn optimieren?

**Bessere Optimierungen:**

- Nur ungerade Zahlen speichern (außer 2)
- Segmented Sieve für sehr große Zahlen
- Wheel Factorization
- Parallellisierung
### **Praxis-Aufgaben**

#### **P1.1: Hello World in 4 Sprachen (20 Punkte)**

Implementiere ein "Hello World" Programm in allen vier Sprachen:

- Python
- Java
- C++
- Scala

Jedes Programm soll zusätzlich die aktuelle Uhrzeit ausgeben.

#### **P1.2: Primzahltest implementieren (30 Punkte)**

Implementiere einen Primzahltest in **zwei** verschiedenen Programmiersprachen:

```python
# Python Beispiel-Struktur
def is_prime(n):
    # Implementierung hier
    if n==1:
	    return f"{n} keine Primzahl"
    elif n==2:
	    return f"{n} ist eine Primzahl"
	elif:
		for i in n:
			if n%i==0:
				return f"{n} ist keine Primzahl"
	else:
		return f"{n} ist eine Primzahl"
    pass
	# Korrigierte Version
def is_prime(n):
    if n < 2:
        return f"{n} ist keine Primzahl"
    elif n == 2:
        return f"{n} ist eine Primzahl"
    else:
        for i in range(2, int(n**0.5) + 1):  # nur bis √n prüfen!
            if n % i == 0:
                return f"{n} ist keine Primzahl"
        return f"{n} ist eine Primzahl"

def sieve_of_eratosthenes(limit):
    # Implementierung hier
is_prime = list(range(2, limit+1))

print(f"Start: {is_prime}")

# Schritt 2: Vielfache entfernen

for i in range(2, int(limit**0.5) + 1):  # nur bis √10 = 3.16, also bis 3

    if i in is_prime:  # Falls i noch nicht gestrichen wurde

        print(f"\nEntferne Vielfache von {i}:")

        # Sammle alle Vielfachen von i (außer i selbst)

        to_remove = []

        for j in range(i*i, limit+1, i):  # ab i²

            if j in is_prime:

                to_remove.append(j)

        # Entferne sie

        for num in to_remove:

            is_prime.remove(num)

            print(f"  Entfernt: {num}")

        print(f"  Liste nach {i}: {is_prime}")

  

print(f"\nEndergebnis: {is_prime}")

# Test verschiedene Zahlen und messe Laufzeit
```

**Anforderungen:**

- Implementiere sowohl einen naiven Test als auch Sieve of Eratosthenes
- Messe und vergleiche die Laufzeiten
- Teste mit Zahlen: 97, 1009, 10007

#### **P1.3: GUI-Button Experiment (20 Punkte)**

Erstelle eine einfache GUI-Anwendung mit drei Buttons:

- Button 1: Zeigt "Hello World" in der Konsole
- Button 2: Zeigt aktuelle Uhrzeit in der Konsole
- Button 3: Zeigt die Zahl "42" in der Konsole

Implementiere dies in Python mit tkinter oder in einer anderen Sprache deiner Wahl.

# ✅ DEIN CODE - FUNKTIONIERT PERFEKT!
# Hier ist dein Code mit kleinen Verbesserungen und Erklärungen:

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QMessageBox, QPushButton, QFrame
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QColor
from datetime import datetime

```python
class MainWindow(QMainWindow):
    
    def show_dialog(self): 
        print("Hello World!")

    def show_time(self): 
        print(datetime.now())

    def print_to_console(self): 
        print("42")

    def __init__(self):
        super().__init__()
        self.setWindowTitle("EiS - Vektorgrafik")
        self.setGeometry(100, 100, 800, 600)
        
        # Frame als Container
        self.frame = QFrame(self) 
        self.setCentralWidget(self.frame) 
        self.my_layout = QVBoxLayout(self.frame) 
        self.frame.setLayout(self.my_layout) 
 
        # ❌ KLEINER FEHLER: Du überschreibst self.btn_dialog 3x!
        # Besser: Verschiedene Namen verwenden
        
        # Button 1: Hello World
        self.btn_hello = QPushButton("Hello World") 
        self.btn_hello.clicked.connect(self.show_dialog) 
        self.my_layout.addWidget(self.btn_hello)

        # Button 2: Show Time  
        self.btn_time = QPushButton("Show Time") 
        self.btn_time.clicked.connect(self.show_time) 
        self.my_layout.addWidget(self.btn_time)

        # Button 3: 42
        self.btn_42 = QPushButton("42") 
        self.btn_42.clicked.connect(self.print_to_console) 
        self.my_layout.addWidget(self.btn_42)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
```

---

## 🖥️ **ÜBUNGSBLATT 02: Graphische Benutzerschnittstellen**

### **Theorie-Aufgaben**

#### **T2.1: Event-Driven Programming (25 Punkte)**

a) **Ereignisorientierte Architektur**: Erkläre das Konzept der ereignisorientierten Programmierung

Der Code wird nur ausgeführt, wenn dieser aufgerufen wird und ist nicht ständig am laufen. Beispiel:
Der Code wird erst ausgeführt, wenn der Button geklickt wird


**Deine Antwort:** ✅ **Richtig!**

> "Code wird nur ausgeführt, wenn aufgerufen wird... Button-Beispiel"

**Ergänzung für Vollständigkeit:**

- Programm **wartet** auf Events (passiv)
- **Event-Handler** werden bei Events aufgerufen
- **Asynchrone Programmierung** - nicht linear von oben nach unten
- **Reaktiv** - Programm reagiert auf Benutzer-Input

b) **Event Loop**: Wie funktioniert eine Event Loop? 

Solange der Loop läuft, ist das Event aktiviert bzw. läuft es. Beispiel das aufrufen eines Fensters ist im loop bis es geschlossen wird

**Deine Antwort:** Teilweise richtig, aber unvollständig

**Was stimmt:** ✅ Loop läuft bis Fenster geschlossen wird **Was fehlt:** Event Loop **sammelt** und **verarbeitet** Events

**Vollständige Antwort:**

```
1. Event Loop läuft endlos (while True)
2. Sammelt Events aus Event Queue (Maus, Tastatur, Timer...)
3. Für jedes Event: Findet passenden Handler
4. Ruft Handler auf
5. Zurück zu Schritt 2
6. Stoppt nur bei quit/exit Event
```

c) **Callback-Funktionen**: Was sind Callbacks und wie werden sie verwendet?

**Deine Antwort:** **Nicht beantwortet!**

**Richtige Antwort:**

- **Definition:** Funktionen, die als Parameter übergeben werden
- **Zweck:** Werden später aufgerufen, wenn Event eintritt
- **Beispiel:** `button.clicked.connect(self.my_function)`
- `my_function` ist der Callback für das `clicked` Event

d) **Vor- und Nachteile**: Welche Vor- und Nachteile hat die ereignisorientierte Programmierung gegenüber linearen Programmen?

Es werden nur die Sachen genutzt die in der Sekunde gebraucht werden, dass spart Rechenleistung und andere Ressourcen

**Deine Antwort:** Nur Vorteile genannt, zu oberflächlich

**Vollständige Antwort:** **Vorteile:**

- ✅ Ressourcen-effizient (wie du sagtest)
- ✅ Benutzerfreundlich (reagiert sofort)
- ✅ Modularer Code
- ✅ Gut für GUIs geeignet

**Nachteile:**

- ❌ Komplexer zu debuggen
- ❌ Race Conditions möglich
- ❌ Schwerer zu verstehen für Anfänger
- ❌ Callback Hell bei vielen verschachtelten Events

#### **T2.2: GUI-Frameworks (20 Punkte)**

a) Vergleiche Qt/PySide6 mit anderen GUI-Frameworks 

**Richtige Antwort:**

|Framework|Sprache|Plattform|Vorteile|Nachteile|
|---|---|---|---|---|
|**Qt/PySide6**|Python|Cross-platform|Professionell, mächtig|Größer, komplexer|
|**Tkinter**|Python|Cross-platform|Einfach, eingebaut|Weniger modern|
|**PyQt**|Python|Cross-platform|Wie PySide, aber andere Lizenz|GPL Lizenz|
|**Kivy**|Python|Mobile + Desktop|Touch-optimiert|Weniger native Optik|

b) Was ist das Signal-Slot System in Qt? 

Übergabe von Signalen wie das drücken einer Taste 

**Deine Antwort:** ✅ Grundidee richtig, aber zu knapp

**Ergänzung:**

python

```python
# Signal = Event (z.B. button.clicked)
# Slot = Handler-Funktion (z.B. self.on_click)
# Verbindung: signal.connect(slot)

button.clicked.connect(self.handle_click)  # clicked ist Signal
#            ^connect^    ^slot^
```

c) Erkläre die Widget-Hierarchie in GUI-Anwendungen 

QApplication
└── QMainWindow
    ├── QMenuBar
    │   ├── QMenu ("File")
    │   │   ├── QAction ("Open")
    │   │   └── QAction ("Save")
    │   └── QMenu ("Edit")
    ├── QToolBar
    │   ├── QAction ("New")
    │   └── QAction ("Cut")
    ├── QWidget (Central Widget)
    │   └── QVBoxLayout
    │       ├── QHBoxLayout (Toolbar)
    │       │   ├── QPushButton ("Rectangle")
    │       │   └── QPushButton ("Circle")
    │       └── CustomDrawingArea
    └── QStatusBar

**Zusatz-Info:**

- **Parent-Child Beziehungen**: Child wird mit Parent zerstört
- **Event Propagation**: Events bubbles durch den Baum
- **Coordinate Systems**: Relativ zum Parent

d) Was sind Layout-Manager und wozu dienen sie?

Unterteilung von Bereichen der GUI zur besseren Anpassbarkeit und Strukturierung

**Deine Antwort:** Richtige Richtung, aber zu knapp

**Vollständige Antwort:** **Zweck:**

- **Automatische Positionierung** von Widgets
- **Responsive Design** - passt sich an Fenster-Größe an
- **Cross-Platform Kompatibilität**

**Typen:**

- **QVBoxLayout**: Vertikal übereinander
- **QHBoxLayout**: Horizontal nebeneinander
- **QGridLayout**: Raster/Tabelle
- **QFormLayout**: Label-Input Paare
- **QStackedLayout**: Mehrere Seiten übereinander

**Ohne Layout-Manager:**

- Absolute Positionierung (x, y Koordinaten)
- Nicht responsive
- Viel manueller Aufwand

#### **T2.3: MVC-Pattern (15 Punkte)**

a) Erkläre das Model-View-Controller Pattern 

b) Wie könnte man es in einer GUI-Anwendung umsetzen? 

c) Welche Vorteile bietet die Trennung von Darstellung und Logik?

Einfache Anpassbarkeit und Erweiterbarkeit von Funktionen


### **Praxis-Aufgaben**

#### **P2.1: Hauptfenster mit Menüs (40 Punkte)**

Erstelle ein Hauptfenster mit folgenden Komponenten:

**Menüstruktur:**

```
Datei
  ├── Öffnen...
  ├── Speichern Als...
  └── Beenden...
Hilfe
  └── Informationen...
```

**Funktionalitäten:**

- **Beenden**: Zeigt Sicherheitsdialog ("Wirklich beenden?") mit Ja/Nein
- **Informationen**: Zeigt Dialog mit "Übungsblatt 02, EIS SoSem 2025, [Dein Name]"
- **Öffnen/Speichern**: Placeholder-Implementierung (später erweitert)

**Code-Struktur (Python/PySide6):**

```python
import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.setup_menus()
    
    def setup_ui(self):
        # UI Setup hier
        pass
    
    def setup_menus(self):
        # Menü Setup hier
        pass
    
    def on_exit(self):
        # Beenden-Dialog hier
        pass
```

#### **P2.2: Toolbar hinzufügen (10 Punkte)**

Erweitere das Hauptfenster um eine Toolbar mit Buttons für:

- Öffnen (Icon + Text)
- Speichern (Icon + Text)
- Beenden (Icon + Text)

Die Buttons sollen die gleichen Aktionen wie das Menü auslösen.

#### **P2.3: Zeichenfläche implementieren (30 Punkte)**

Implementiere eine Zeichenfläche, auf der man mit der Maus malen kann:

**Anforderungen:**

- Malen bei gedrückter linker Maustaste
- Bild bleibt erhalten bei Fenster-Resize/Minimieren
- Verwende QImage für die Bildspeicherung
- Schwarzer Pinsel auf weißem Hintergrund

**Code-Grundgerüst:**

```python
class DrawingArea(QWidget):
    def __init__(self):
        super().__init__()
        self.image = QImage(800, 600, QImage.Format_RGB32)
        self.image.fill(Qt.white)
        self.drawing = False
        
    def mousePressEvent(self, event):
        # Maus-Ereignis behandeln
        pass
    
    def mouseMoveEvent(self, event):
        # Zeichnen implementieren
        pass
    
    def paintEvent(self, event):
        # Zeichnen auf Screen
        pass
```

#### **P2.4: Datei-Operationen (20 Punkte)**

Implementiere die Speichern/Öffnen Funktionalität:

- **Speichern Als**: Speichere das gemalte Bild als PNG-Datei
- **Öffnen**: Lade ein existierendes Bild in die Zeichenfläche

Verwende QFileDialog für die Dateiauswahl.

---

## 🎯 **Lösungshinweise & Tipps**

### **Allgemeine Tipps:**

1. **Lese alle Aufgaben durch, bevor du anfängst**
2. **Strukturiere deinen Code sauber** - verwende Klassen und Funktionen
3. **Teste häufig** - kleine Schritte sind besser als große Sprünge
4. **Dokumentiere deinen Code** - Kommentare helfen beim Verstehen

### **Debugging-Tipps:**

- Verwende `print()` Statements zum Debuggen
- Teste GUI-Komponenten einzeln
- Bei Qt-Problemen: Prüfe die offizielle Dokumentation

### **Performance-Messung:**

```python
import time

start = time.time()
# Dein Code hier
end = time.time()
print(f"Laufzeit: {end - start:.4f} Sekunden")
```

### **Häufige Fehler:**

1. **Vergessene Event-Handler** - Buttons ohne Funktionalität
2. **Falsche Widget-Hierarchie** - Layout-Probleme
3. **Fehlende super().**init**()** Aufrufe in Klassen
4. **Nicht behandelte Exceptions** - Programm stürzt ab

---

## 📝 **Bewertungskriterien**

### **Übungsblatt 01 (100 Punkte):**

- Theorie-Aufgaben: 50 Punkte
- Praxis-Aufgaben: 50 Punkte
- **Bonus**: Sauberer, dokumentierter Code (+10 Punkte)

### **Übungsblatt 02 (100 Punkte):**

- Theorie-Aufgaben: 60 Punkte
- Praxis-Aufgaben: 40 Punkte
- **Bonus**: Erweiterte GUI-Features (+10 Punkte)

### **Mindestanforderungen für das Bestehen:**

- Mindestens 50% der Punkte in jedem Übungsblatt
- Funktionsfähiger Code (kompiliert/läuft ohne Fehler)
- Dokumentation der wichtigsten Funktionen

**Viel Erfolg bei den Übungen! 🚀**