### **Übungsblatt 1: Python Grundlagen & Arrays (≈2h)**

**Aufgabe 1.1: String-Array Verarbeitung mit Type-Annotations (20 Punkte)** 
Schreiben Sie eine Funktion `filter_strings(string_array: list[str]) -> list[str]`, die:

- Alle Strings zurückgibt, die mit "test" beginnen
- Leere Strings ignoriert
- Strings mit weniger als 3 Zeichen ignoriert

```python
from typing import List

def filter_strings(string_array: List[str]) -> List[str]:
    return [s for s in strings_array if s and len(s)>=3 and s.startswith("test")]

# Test: ["test123", "", "abc", "testing", "te"] → ["test123", "testing"]
```

**Aufgabe 1.2: Zahlen-Array Operationen mit Type-Annotations (25 Punkte)** Implementieren Sie mit vollständigen Typannotationen:

```python
from typing import Dict, Any, List

def array_operations(numbers: List[int]) -> Dict[str, Any]:

        summe = sum(numbers)

        max_number = max(numbers)

        even_counter = len(list(filter(lambda x: x%2==0,numbers)))

        sort_desc = sorted(numbers, reverse = True)

        return {"sum": summe, "max": max_number, "even_count": even_counter, "sort_desc": sort_desc}
    #{"sum": int, "max": int, "even_count": int, "sorted_desc": List[int]}
    
```

**Aufgabe 1.3: Konzeptfrage - Scala vs Python Syntax (15 Punkte)** Gegeben ist folgender Scala-Code:

```scala
val numbers = List(1, 2, 3, 4, 5)
val doubled = numbers.map(x => x * 2).filter(x => x > 4)
```

a) Übersetzen Sie diesen Code nach Python mit Type-Annotations
```python
numbers: List[int] = [1, 2, 3, 4, 5] 
doubled: List[int] = [x * 2 for x in numbers if x * 2 > 4]
```
b) Erklären Sie den Unterschied zwischen `val` und `var` in Scala 

- `val` = **unveränderlich** (wie `const` in anderen Sprachen)
- `var` = **veränderlich** (normale Variable)

c) Wie unterscheidet sich die Unveränderlichkeit in Scala von Python?

- **Python:** Dynamisch typisiert, Listen sind standardmäßig **mutable**
- **Scala:** Statisch typisiert, Collections sind standardmäßig **immutable**


---

### **Übungsblatt 2: Objektorientierte Programmierung - Python (≈2h)**

**Aufgabe 2.1: Abstrakte Klassen mit Type-Annotations (30 Punkte)** 
Implementieren Sie in Python:

```python
from abc import ABC, abstractmethod

from typing import Protocol

  

class Shape(ABC):

    def __init__(self, name: str, color: str) -> None:

        self.name = name

        self.color = color

    @abstractmethod

    def area(self) -> float:

        pass

    @abstractmethod

    def perimeter(self) -> float:
        pass

    def describe(self) -> str:

        return {self.name, self.color}

  

class Rectangle(Shape):

    def __init__(self, name: str, color: str, width: float, height: float) -> None:

        super().__init__(name,color)

        self.width = width

        self.height = height

  

    def area(self) -> float:

        return self.width * self.height

    def perimeter(self) -> float:

        return 2 * (self.width + self.height)

  

class Circle(Shape):

    def __init__(self, name: str, color: str, width: float, height: float) -> None:

        super().__init__(name,color)

        self.width = width

        self.height = height
	def area(self) -> float: 
		return 3.14159 * self.radius ** 2
	def perimeter(self) -> float: 
		return 2 * 3.14159 * self.radius 
```

**Aufgabe 2.2: Vererbung und Polymorphie mit Type-Annotations (25 Punkte)**

```python
from typing import List

  

class Vehicle:

    def __init__(self, brand: str, speed: int) -> None:

        self.brand =  brand

        self.speed = speed

    def move(self) -> str:

        return f"{self.brand} is moving at {self.speed} km/h"

class Car(Vehicle):

    def __init__(self, brand: str, speed: int, doors: int) -> None:

        super().__init__(brand, speed)

        self.doors = doors

    def drive(self) -> str:

        return self.speed

  

def test_vehicles(vehicles: List[Vehicle]) -> None:

    # Rufen Sie move() für alle Fahrzeuge auf (Polymorphie)

    for vehicle in vehicles:

        print(vehicle.move())
```

**Aufgabe 2.3: Konzeptfrage - OOP in verschiedenen Sprachen (15 Punkte)** 
a) Wie unterscheidet sich die Klassendefinition in Scala von Python?

```python
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
```

```Scala
class Person(name: String, age: Int)  // Konstruktor-Parameter direkt
// ODER als Case Class:
case class Person(name: String, age: Int)  // Automatisch equals, toString, etc.
```
b) Was sind die Vor-/Nachteile von Python's Duck Typing vs Scala's statischer Typisierung? 

**Python Duck Typing:**

- ✅ **Vorteile:** Flexibel, weniger Code, Enten-Test ("If it walks like a duck...")
- ❌ **Nachteile:** Laufzeit-Fehler, schwerer zu debuggen, IDE-Support begrenzt

**Scala Statische Typisierung:**

- ✅ **Vorteile:** Compile-Zeit Fehlerprüfung, bessere IDE-Unterstützung, Performance
- ❌ **Nachteile:** Mehr Code, weniger Flexibilität, steile Lernkurve

c) Erklären Sie, warum C++ Mehrfachvererbung problematischer ist als Python's MRO.

**C++ Problem (Diamond Problem):**

```cpp
class A { int value; };
class B : public A {};
class C : public A {};
class D : public B, public C {};  // Welches A.value?
```

**Python MRO (Method Resolution Order):**

- Python löst das mit eindeutiger Reihenfolge (C3-Linearisierung)
- `Class.mro()` zeigt die Auflösungsreihenfolge
- Vermeidet Ambiguität durch klare Regeln


---

### **Übungsblatt 3: Python vs Scala Konzepte (≈2h)**

**Aufgabe 3.1: List Comprehensions vs Scala Collections (20 Punkte)** Implementieren Sie in Python mit Type-Annotations:

```python
from typing import List

numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# a) Alle geraden Zahlen quadriert
even_squared: List[int] = [ x**2 for x in numbers if x%2==0]# Implementieren Sie

# b) Alle ungeraden Zahlen als Strings
odd_strings: List[str] = [str(x) for x in numbers if x % 2!=0]

# c) Summe aller Zahlen > 5
sum_greater_five: int = sum([x for x in numbers if x>5])# Implementieren Sie
```

**Konzeptfrage:** Wie würde der gleiche Code in Scala aussehen? Erklären Sie die Unterschiede.

```scala

val numbers = List(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

// a) Alle geraden Zahlen quadriert
val even_squared = numbers.filter(_%2==0).map(x => x*x)
// b) Alle ungeraden Zahlen als Strings
val odd_strings = numbers.filter(_ % 2 != 0).map(_.toString)
// c) Summe aller Zahlen > 5
val sum_greater_five = numbers.filter(_>5).sum
```

**Aufgabe 3.2: Pattern Matching Simulation in Python (25 Punkte)** Scala hat Pattern Matching, Python nutzt if-elif-else. Implementieren Sie:

```python
def process_input(input_data: Any) -> str:

    # Verarbeitet verschiedene Eingabetypen:

    # - str → "Text: " + string

    if isinstance(input_data, str):

        return f"Text: {input_data}"

    if isinstance(input_data, int):

        if input_data > 0:

            return f"Positive Zahl: {input_data}"

        elif input_data < 0:

            return f"Negative Zahl: {input_data}"

        else:

            return "Null"

    # - list → "Liste mit X Elementen"

    if isinstance(input_data, list):

        return f"Liste mit {len(input_data)} Elementen"

    # - dict → "Dictionary mit X Schlüsseln"

    if isinstance(input_data, dict):

        return f"Dictionary mit {len(input_data)} Schlüsseln"

    # - andere → "Unbekannter Typ: " + type name

    return f"Unbekannter Typ: {type(input_data)}"
    
    

```

**Aufgabe 3.3: Konzeptfrage - Funktionale Konzepte (25 Punkte)** Gegeben ist folgender Scala-Code:

```scala
case class Person(name: String, age: Int)
val persons = List(Person("Anna", 25), Person("Bob", 30), Person("Charlie", 20))
val adults = persons.filter(_.age >= 18).map(_.name).mkString(", ")
```

a) Implementieren Sie den gleichen Code in Python mit Type-Annotations und dataclasses 

```python
@dataclass
class Person():
	def __init__(self, name: str, age: int) -> None:
		self.name = name
		self.age = age

persons: List[Person] = [Person("Anna", 25),Person("Bob", 30),Person("Charlie", 20)]
adults: list[str] = [i.name for i in persons if i.age >= 18]  # Liste der Namen von Erwachsenen

print(f"Erwachsene: {', '.join(adults)}")
```

b) Erklären Sie, was `_.age` in Scala bedeutet 

Vor dem Punkt wird die Klasse geschrieben, also Klasse.Attribut. Ist nur ein Platzhalter für das aktuelle Element 
"`_.age` bedeutet: "Für jedes Element in der Liste, nimm dessen age-Attribut"

c) Wie unterscheidet sich Scala's `case class` von Python's `@dataclass`?


```Python @dataclass
@dataclass
class Person:
    name: str
    age: int
Automatisch: __init__, __repr__, __eq_
```


```scala
// Scala case class  
case class Person(name: String, age: Int)
// Automatisch: constructor, toString, equals, copy, pattern matching
```

- Scala case classes haben **pattern matching** eingebaut
- Scala ist **immutable** by default
- Python @dataclass ist **mutable** by default

**Aufgabe 3.4: Java vs Python Speicherverwaltung (10 Punkte)** Erklären Sie die Unterschiede zwischen:

- Java's Garbage Collection und Python's Reference Counting

	In Java wird nach einiger Zeit Speicher wieder freigegeben, während in Python nur auf einen Wert referenziert wird, also nicht immer ein Wert im Speicher angelegt wird sondern nur einmalig und dann darauf verwiesen.

	**Korrekt:** Python = Reference Counting + GC, Java = nur GC

- C++ manuelle Speicherverwaltung vs automatische GC

	In C++ muss ich den Speicher manuell wieder freigeben, während dieser bei automatischen GC freigegeben wird, sobald die Variable oder das Objekt nicht mehr gebraucht wird.

- Warum sind C++ Pointer gefährlicher als Python Referenzen?

	Pointer zeigen auf etwas, Referenzen referenzieren einen Wert. Bei ersterem kann es passieren, dass der Wert auf den der Point zeigt sich ändert ohne das der Pointer sich passend verschiebt. Beim zweiten "überschreibe" ich quasi den Wert auf den ich referenziert habe.
	**Korrekt:**
    - C++ Pointer können auf ungültigen Speicher zeigen (dangling pointer)
    - C++ hat keine Bounds-Checking (Buffer Overflow möglich)
    - Python Referenzen sind immer safe (keine Null-Pointer-Dereferenzierung)

---

## **TAG 2**

### **Übungsblatt 4: GUI-Programmierung mit Python (≈2h)**

**Aufgabe 4.1: Einfache GUI-Anwendung mit Type-Annotations (40 Punkte)** Erstellen Sie mit PySide6/Qt:

```python
from typing import Optional
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PySide6.QtWidgets import QLineEdit, QPushButton, QTextEdit, QLabel

class TextProcessor(QMainWindow): 
	def __init__(self) -> None: 
		super().__init__() 
		self.setup_ui() 
	
	def setup_ui(self) -> None: 
	# Fenster-Einstellungen 
		self.setWindowTitle("Textverarbeitung") 
		self.setGeometry(100, 100, 800, 600) 
		# Zentrales Widget und Layout 
		central = QWidget() 
		self.setCentralWidget(central) 
		layout = QVBoxLayout(central) 
		# Eingabefeld für Text 
		self.input = QLineEdit() 
		self.input.setPlaceholderText("Geben Sie Ihren Text hier ein...")
		self.input.setClearButtonEnabled(True) 
		self.input.setMinimumHeight(40) 
		self.input.setMaximumHeight(40) 
		self.input.setFocus() 
		layout.addWidget(self.input) 
		# Button "Verarbeiten" 
		self.process_text_button = QPushButton("Verarbeiten")
		self.process_text_button.clicked.connect(self.process_text)
		layout.addWidget(self.process_text_button) 
		# Ausgabebereich 
		self.output = QTextEdit() 
		layout.addWidget(self.output) 
	def process_text(self) -> None: 
	# Funktionalität: Text umkehren und Wortanzahl anzeigen 
	input_text: str = self.input.text() 
		if input_text: 
		reversed_text: str = input_text[::-1] 
		word_count: int = len(input_text.split()) 
		result: str = f"Umgekehrter Text: {reversed_text}\nWortanzahl: {word_count}" 
		self.output.setText(result) 
		else: 
			self.output.setText("Bitte geben Sie einen Text ein.")
```

**Aufgabe 4.2: Event-Handling mit Type-Annotations (30 Punkte)** Erweitern Sie die GUI um:

```python
from PySide6.QtCore import QTimer
from PySide6.QtGui import QAction, QKeySequence

class AdvancedTextProcessor(TextProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.timer: QTimer = QTimer()
        self.setup_menu()
        self.setup_statusbar()
    
    def setup_menu(self) -> None:
        # Menüleiste mit "Datei" → "Öffnen", "Speichern", "Beenden"
        menubar = self.menuBar()
        file_menu = menubar.addMenu("Datei")

		open_action = QAction("Open", self)
        open_action.setShortcut(QKeySequence.Open)  # Ctrl+O
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)
	    
	    save_action = QAction("Speichern", self)
        save_action.setShortcut(QKeySequence.Save)  # Ctrl+S
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)
	    
	    close_action = QAction("Beenden", self)
        close_action.setShortcut(QKeySequence.Close)  # Ctrl+O
        close_action.triggered.connect(self.close_file)
        file_menu.addAction(close_action)
        # Tastaturkürzel (Ctrl+O, Ctrl+S, Ctrl+Q)
        pass
    
    def setup_statusbar(self) -> None: 
    # Richtet die Statusleiste mit Zeitanzeige und Status-Informationen ein. 
    #Statusleiste initialisieren 
	    statusbar = self.statusBar() # Option 1: Nur Zeit anzeigen 
	    def update_time(): 
			current_time = QTime.currentTime().toString("HH:mm:ss")
			statusbar.showMessage(f"Aktuelle Uhrzeit: {current_time}") 
		# Timer für Zeitaktualisierung 
		self.time_timer = QTimer(self)
		self.time_timer.timeout.connect(update_time)
		self.time_timer.start(1000) # Update jede Sekunde 
		# Sofort die Zeit anzeigen 
		update_time()
	# Event-Handler Methoden 
	def open_file(self) -> None: 
		self.statusBar().showMessage("Datei öffnen...") 
		# Hier würde normalerweise ein FileDialog kommen 
	def save_file(self) -> None: 
		self.statusBar().showMessage("Datei speichern...") # Hier würde normalerweise ein Save-Dialog kommen
        
```

**Aufgabe 4.3: Konzeptfrage - GUI Frameworks (30 Punkte)** 
a) Vergleichen Sie Python's Qt (PySide6) mit Java's Swing - Vor-/Nachteile?

PySide6/Qt Vorteile: 
✅ Native Look & Feel auf allen Plattformen 
✅ Sehr umfangreiche Widget-Bibliothek 
✅ Starke Community, gut dokumentiert 
✅ Moderne API mit Signal-Slot System Java Swing Vorteile: 
✅ Plattformunabhängig (JVM) 
✅ Eingebaute Themes (Look & Feel) 
✅ Teil der Standard-Java-Bibliothek

Nachteile: 
❌ Qt: Lizenzkosten bei kommerzieller Nutzung 
❌ Swing: Veraltet, weniger moderne UI-Elemente


b) Wie unterscheidet sich ereignisorientierte Programmierung von prozeduraler? 

Ersteres wird nur ausgelöst, wenn das Ereignis eintritt also z.B. ein Knopf gedrückt wird.

**Ergänzung:**

- **Prozedural:** Code läuft sequenziell von oben nach unten
- **Ereignisorientiert:** Programm wartet auf Events (Clicks, Keyboard) und reagiert darauf

c) Erklären Sie das Observer-Pattern im Kontext von GUI-Events.

Das Beobachter-Muster ist ein Entwurfsmuster aus dem Bereich der Softwareentwicklung. Es gehört zur Kategorie der Verhaltensmuster und dient der Weitergabe von Änderungen an einem Objekt an von diesem Objekt abhängige Strukturen.

Heißt Weitergabe von Informationen nachdem ein Ereignis ausgelöst wurde wie das anklicken eines Buttons.

Button (Subject) benachrichtigt Event-Handler (Observer) button.clicked.connect(self.on_click) # Observer registriert sich # Wenn Button geklickt wird → Observer wird benachrichtigt

---

### **Übungsblatt 5: Funktionale Programmierung in Python (≈2h)**

**Aufgabe 5.1: Higher-Order Functions mit Type-Annotations (30 Punkte)**

```python
from typing import Callable, List, TypeVar

T = TypeVar('T')
U = TypeVar('U')

def apply_operations(data: List[T], operations: List[Callable[[T], T]]) -> List[T]:

    """Wendet alle Operationen nacheinander auf alle Daten an"""

    result = data

    for operation in operations:

        result = [operation(item) for item in result]

    return result

  

def compose_functions(f: Callable[[T], U], g: Callable[[U], T]) -> Callable[[T], T]:

    """Komponiert zwei Funktionen f und g zu einer neuen Funktion h"""

    def h(x: T) -> T:

        return g(f(x))

    return h

# Testen Sie mit:
numbers: List[int] = [1, 2, 3, 4, 5]
operations: List[Callable[[int], int]] = [
    lambda x: x * 2,
    lambda x: x + 1,
    lambda x: x ** 2
]
```

**Aufgabe 5.2: Funktionale Stil mit map/filter/reduce (25 Punkte)**

```python
from functools import reduce
from typing import List

numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Implementieren Sie nur mit map(), filter(), reduce():
def functional_processing(numbers: List[int]) -> int:
    """
    1. Alle geraden Zahlen filtern
    2. Quadrieren
    3. Summe bilden
    """
    even_numbers = filter(lambda x: x % 2 == 0, numbers)

    quad_numbers = map(lambda x: x**2, even_numbers)

    sum_number = reduce(lambda x, y: x + y, quad_numbers)

    return sum_number

# Bonus: Implementieren Sie das gleiche mit List Comprehension
def pythonic_processing(numbers: List[int]) -> int:
	even_number: List[int] = [i for i in numbers if i%2==0]
	quad_number: List[int] = [j ** 2 for j in even_number]
	sum_number: int = sum(quad_number)
    return sum_number
```

**Aufgabe 5.3: Rekursion vs. Iteration Performance (25 Punkte)**

```python
import time
from typing import Dict

def fibonacci_recursive(n: int) -> int:
	if n == 1:
	    return 0
	elif n == 2:
		return 1
	else:
		return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
	
    

def fibonacci_iterative(n: int) -> int:
    if n == 1:

        return 0

    elif n == 2:

        return 1

    else:

        result_1: int = 0

        result_2: int = 1

        puffer: int = 0

        for i in range(n - 2):

            result_1 = result_1 + result_2

            puffer = result_2

            result_2 = result_1

            result_1 = puffer

        return result_1

def fibonacci_memoized(n: int, memo: Dict[int, int] = None) -> int:
    # Implementieren Sie mit Memoization

    if memo is None:

        memo = {}

    if n in memo:

        return memo[n]

    if n == 1:

        return 0

    elif n == 2:

        return 1

    else:

        memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)

    return memo[n]

def benchmark_fibonacci(n: int) -> None:
    # Recursive 
    start = time.time() 
    result_rec = fibonacci_recursive(n) 
    time_rec = time.time() - start 
    
    # Iterative 
    start = time.time() 
    result_iter = fibonacci_iterative(n) 
    time_iter = time.time() - start 
    
    # Memoized 
    start = time.time() 
    result_memo = fibonacci_memoized(n) 
    time_memo = time.time() - start 
    
    print(f"n={n}") print(f"Recursive: {result_rec}, Time: {time_rec:.4f}s")
    print(f"Iterative: {result_iter}, Time: {time_iter:.4f}s") 
    print(f"Memoized: {result_memo}, Time: {time_memo:.4f}s")
     
```

**Aufgabe 5.4: Konzeptfrage - Funktionale Programmierung (20 Punkte)** 
a) Wie unterscheidet sich Scala's funktionale Ausrichtung von Python's imperativem Stil? 

- **Scala:** Funktional by design - Immutable Collections, Pattern Matching, pure functions bevorzugt
- **Python:** Imperativ by design - Statements, mutable objects, side effects normal

b) Erklären Sie Immutability: Warum ist es in Scala default, in Python optional?

- **Scala:** Immutability = Objekte können nach Erstellung nicht verändert werden
- **Python:** Mutability = Listen, Dicts können verändert werden
- **Beispiel:** Scala `List(1,2,3).append(4)` erstellt neue Liste, Python `[1,2,3].append(4)` verändert Original

c) Was sind die Vor-/Nachteile von Pure Functions vs Side Effects?

**Korrekt:**

- **Pure Functions:** Gleicher Input → gleicher Output, keine Seiteneffekte
- **Side Effects:** Ändern globalen Zustand, I/O, Exceptions

**Vorteile Pure Functions:**

- Testbar, vorhersagbar, parallelisierbar
- Keine versteckten Abhängigkeiten

**Nachteile Pure Functions:**

- Schwer für I/O, Zustandsänderungen
- Manchmal weniger performant

---

### **Übungsblatt 6: Entwurfsmuster in Python (≈2h)**

**Aufgabe 6.1: Singleton Pattern mit Type-Annotations (20 Punkte)**

```python
from typing import Optional, ClassVar
import threading

class DatabaseConnection:
    _instance: ClassVar[Optional['DatabaseConnection']] = None
    _lock: ClassVar[threading.Lock] = threading.Lock()
    
    def __new__(cls) -> 'DatabaseConnection':
        if cls.instance is None:
	        with cls._lock:
		        if cls._instance is None:
			        cls._instance = super().__new__(cls)
        pass
    
    def __init__(self) -> None:
        if not hasattr(self, 'initialized'):
            self.initialized: bool = True
            self.connected: bool = False
    
    def connect(self) -> bool:
        # Implementieren Sie
        pass
    
    def disconnect(self) -> bool:
        # Implementieren Sie
        pass
    
    def execute_query(self, sql: str) -> str:
        # Implementieren Sie
        pass
```

**Aufgabe 6.2: Observer Pattern mit Type-Annotations (35 Punkte)**

```python
from typing import List, Protocol
from abc import ABC, abstractmethod

class Observer(Protocol):
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        pass

class Subject(ABC):
    def __init__(self) -> None:
        self._observers: List[Observer] = []
    
    def attach(self, observer: Observer) -> None:
        pass
    
    def detach(self, observer: Observer) -> None:
        pass
    
    def notify(self) -> None:
        pass

class WeatherStation(Subject):
    def __init__(self) -> None:
        super().__init__()
        self._temperature: float = 0.0
        self._humidity: float = 0.0
        self._pressure: float = 0.0
    
    def set_measurements(self, temp: float, humidity: float, pressure: float) -> None:
        # Implementieren Sie
        pass

class WeatherDisplay:
    def __init__(self, name: str) -> None:
        self.name: str = name
    
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        # Implementieren Sie
        pass
```

**Aufgabe 6.3: Factory Pattern mit Type-Annotations (25 Punkte)**

```python
from typing import Union, Dict, Any
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass
    
    @abstractmethod
    def describe(self) -> str:
        pass

class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius: float = radius

class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width: float = width
        self.height: float = height

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type: str, **kwargs: Any) -> Shape:
        # Implementieren Sie:
        # "circle" → Circle(radius=kwargs["radius"])
        # "rectangle" → Rectangle(width=kwargs["width"], height=kwargs["height"])
        pass
```

**Aufgabe 6.4: Konzeptfrage - Design Patterns (20 Punkte)** a) Wie würde das Singleton Pattern in Scala mit `object` implementiert werden? b) Vergleichen Sie Java's Interface mit Python's Protocol/ABC c) Warum ist das Factory Pattern in statisch typisierten Sprachen (Java/Scala) wichtiger als in Python?

---

## **TAG 3**

### **Übungsblatt 7: Nebenläufigkeit & Client-Server Python (≈2h)**

**Aufgabe 7.1: Threading Grundlagen mit Type-Annotations (30 Punkte)**

```python
import threading
import time
from typing import List

def worker(worker_id: int, work_time: int, results: List[str]) -> None:
    """Simuliert Arbeit und sammelt Ergebnisse"""
    # Implementieren Sie mit Thread-safe Ausgabe
    pass

def main_threading() -> None:
    results: List[str] = []
    threads: List[threading.Thread] = []
    
    # Starten Sie 3 Worker parallel und warten Sie auf Beendigung
    # Geben Sie alle Ergebnisse aus
    pass
```

**Aufgabe 7.2: Race Conditions mit Type-Annotations (25 Punkte)**

```python
import threading
from typing import ClassVar

class UnsafeCounter:
    def __init__(self) -> None:
        self.value: int = 0
    
    def increment(self) -> None:
        self.value += 1

class SafeCounter:
    def __init__(self) -> None:
        self.value: int = 0
        self._lock: threading.Lock = threading.Lock()
    
    def increment(self) -> None:
        # Implementieren Sie Thread-safe Version
        pass
    
    def get_value(self) -> int:
        # Implementieren Sie Thread-safe Getter
        pass

def test_race_condition() -> None:
    # Testen Sie beide Counter mit 100 Threads, die je 1000x incrementieren
    pass
```

**Aufgabe 7.3: Producer-Consumer Pattern (35 Punkte)**

```python
import queue
import threading
import time
import random
from typing import Optional

def producer(q: queue.Queue[int], stop_event: threading.Event) -> None:
    """Erzeugt alle 0.5s eine Zufallszahl"""
    pass

def consumer(q: queue.Queue[int], stop_event: threading.Event, consumer_id: int) -> None:
    """Verarbeitet Zahlen (simuliert mit time.sleep)"""
    pass

def main_producer_consumer() -> None:
    # Implementieren Sie mit graceful shutdown
    pass
```

**Aufgabe 7.4: Konzeptfrage - Parallelität (10 Punkte)** a) Unterscheiden Sie Threading, Multiprocessing und Async/Await in Python b) Wie unterscheidet sich Java's Thread-Modell von Python's GIL? c) Erklären Sie, warum Scala's Actor-Model eleganter für Nebenläufigkeit ist

---

### **Übungsblatt 8: Algorithmen & Datenstrukturen Python (≈2h)**

**Aufgabe 8.1: Sortieralgorithmen mit Type-Annotations (30 Punkte)**

```python
import time
from typing import List, Callable

def bubble_sort(arr: List[int]) -> List[int]:
    """Bubble Sort mit Optimierung (frühes Beenden)"""
    pass

def quick_sort(arr: List[int]) -> List[int]:
    """Quick Sort (rekursiv)"""
    pass

def benchmark_sort(sort_func: Callable[[List[int]], List[int]], 
                  data: List[int], name: str) -> None:
    """Misst Performance eines Sortieralgorithmus"""
    pass

def compare_algorithms() -> None:
    # Vergleichen Sie Performance für [100, 1000, 5000] Elemente
    pass
```

**Aufgabe 8.2: Verkettete Liste mit Type-Annotations (35 Punkte)**

```python
from typing import Optional, Any

class Node:
    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.next: Optional['Node'] = None

class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
    
    def append(self, data: Any) -> None:
        pass
    
    def prepend(self, data: Any) -> None:
        pass
    
    def delete(self, data: Any) -> bool:
        """Löscht erstes Vorkommen, gibt True zurück bei Erfolg"""
        pass
    
    def find(self, data: Any) -> Optional[Node]:
        pass
    
    def __str__(self) -> str:
        pass
    
    def __len__(self) -> int:
        pass
```

**Aufgabe 8.3: Rekursive Algorithmen mit Type-Annotations (25 Punkte)**

```python
from typing import List, Tuple

def binary_search(arr: List[int], target: int, 
                 left: int = 0, right: Optional[int] = None) -> int:
    """Binäre Suche (rekursiv), gibt Index zurück oder -1"""
    pass

def tower_of_hanoi(n: int, source: str, destination: str, auxiliary: str) -> List[str]:
    """Tower of Hanoi, gibt Liste der Bewegungen zurück"""
    pass

def gcd(a: int, b: int) -> int:
    """Größter gemeinsamer Teiler (Euklidischer Algorithmus)"""
    pass
```

**Aufgabe 8.4: Konzeptfrage - Algorithmus-Komplexität (10 Punkte)** a) Vergleichen Sie die Zeitkomplexität von Bubble Sort, Quick Sort und Python's Timsort b) Wie unterscheidet sich Speicherverwaltung bei rekursiven vs iterativen Algorithmen? c) Warum sind Collections in Scala oft immutable, während Python's mutable sind?

---

### **Übungsblatt 9: Klausur-Simulation (≈2h)**

**Aufgabe 9.1: Array-Verarbeitung mit Type-Annotations (15 Punkte)**

```python
from typing import Dict
import re

def count_words(text: str) -> Dict[str, int]:
    """
    Zählt Worthäufigkeiten (case-insensitive)
    Ignoriert Satzzeichen
    Beispiel: "Hello, World! Hello" → {"hello": 2, "world": 1}
    """
    pass

def analyze_text(text: str) -> Dict[str, Any]:
    """
    Erweiterte Textanalyse:
    - word_count: Anzahl Wörter
    - char_count: Anzahl Zeichen (ohne Leerzeichen)
    - longest_word: Längstes Wort
    - word_frequencies: Dict mit Worthäufigkeiten
    """
    pass
```

**Aufgabe 9.2: OOP Design mit Type-Annotations (25 Punkte)**

```python
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

@dataclass
class Medium(ABC):
    title: str
    year: int
    
    @abstractmethod
    def can_lend(self) -> bool:
        pass
    
    @abstractmethod
    def get_info(self) -> str:
        pass

@dataclass
class Book(Medium):
    author: str
    isbn: str
    is_available: bool = True
    
    def can_lend(self) -> bool:
        # Implementieren Sie
        pass

@dataclass  
class DVD(Medium):
    director: str
    duration_minutes: int
    is_available: bool = True

@dataclass
class Magazine(Medium):
    issue_number: int
    
    def can_lend(self) -> bool:
        # Magazine können nie ausgeliehen werden
        return False

class Library:
    def __init__(self) -> None:
        self.media: List[Medium] = []
        self.borrowed_media: Dict[str, datetime] = {}
    
    def add_medium(self, medium: Medium) -> None:
        pass
    
    def lend_medium(self, title: str) -> bool:
        pass
    
    def return_medium(self, title: str) -> bool:
        pass
    
    def list_available(self) -> List[Medium]:
        pass
```

**Aufgabe 9.3: GUI Taschenrechner (30 Punkte)**

```python
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, 
                               QGridLayout, QPushButton, QLineEdit, QVBoxLayout)
from typing import Optional

class Calculator(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.current_input: str = ""
        self.operator: Optional[str] = None
        self.first_number: Optional[float] = None
        self.setup_ui()
    
    def setup_ui(self) -> None:
        # Implementieren Sie GUI mit:
        # - Display (QLineEdit)
        # - Zahlen-Buttons (0-9)
        # - Operator-Buttons (+, -, *, /)
        # - Equals-Button (=)
        # - Clear-Button (C)
        pass
    
    def on_number_clicked(self, number: str) -> None:
        pass
    
    def on_operator_clicked(self, operator: str) -> None:
        pass
    
    def on_equals_clicked(self) -> None:
        pass
    
    def on_clear_clicked(self) -> None:
        pass
    
    def calculate(self, first: float, second: float, operator: str) -> float:
        pass
```

**Aufgabe 9.4: Konzeptfragen (30 Punkte)**

**a) Vererbung vs. Komposition (8 Punkte)** Erklären Sie an einem konkreten Beispiel:

- Wann sollten Sie Vererbung verwenden?
- Wann ist Komposition besser?
- Wie unterscheidet sich dies in Python vs Java?

**b) Statische vs. Dynamische Typisierung (8 Punkte)** Vergleichen Sie:

- Python (dynamisch) vs Scala (statisch)
- Type-Annotations in Python vs echte statische Typisierung
- Vor-/Nachteile für Entwicklung und Laufzeit

**c) Speicherverwaltung und Sicherheit (7 Punkte)** Erklären Sie:

- Warum sind C++ Pointer gefährlicher als Python Referenzen?
- Wie unterscheidet sich Java's Garbage Collection von Python's Reference Counting?
- Was sind Memory Leaks und wie entstehen sie in verschiedenen Sprachen?

**d) Entwurfsmuster Anwendung (7 Punkte)** Nennen Sie für jedes Pattern ein konkretes Anwendungsbeispiel:

- Singleton Pattern: _______________
- Observer Pattern: _______________
- Factory Pattern: _______________
- Strategy Pattern: _______________

## **Zusatz-Übung: Klausur-API Vorbereitung**

**Aufgabe 9.5: Dummy-API Programmierung (Bonus)** Basierend auf der Altklausur - üben Sie mit vereinfachten APIs:

```python
# Gegeben: Vereinfachte "EIS-API" (wie in echter Klausur)
class EISPainter:
    def set_pixel(self, x: int, y: int, color: bool) -> None:
        """Ein Pixel setzen (color = True/False für schwarz/weiß)"""
        pass

class EISWidget:
    def mouse_down(self, x: int, y: int) -> None: pass
    def mouse_up(self, x: int, y: int) -> None: pass  
    def mouse_move(self, x: int, y: int) -> None: pass
    def paint(self, painter: EISPainter) -> None: pass

# Implementieren Sie eine Klasse "EISButton" die EISWidget erweitert:
# - Zeigt Text an einer Position
# - Reagiert auf Mausklicks
# - Zeichnet Rahmen mit EISPainter
```

Diese Art von API wird vermutlich in der echten Klausur verwendet!

---

## **Bewertungsschema & Tipps**

### **Fokus auf Python mit Konzeptwissen:**

- ✅ **Alle Programmieraufgaben in Python** (mit Type-Annotations)
- ✅ **Konzeptfragen zu allen 4 Sprachen** (Python, Scala, Java, C++)
- ✅ **Code-Analyse** von Scala/Java-Fragmenten
- ✅ **Sprachvergleiche** und Design-Entscheidungen

### **Klausur-relevante Schwerpunkte:**

- **Programmieraufgaben:** Nur Python (mit Type-Annotations)
- **Konzeptfragen:** Python, Scala, Java, C++ Vergleiche
- **Code-Verständnis:** Scala/Java Code lesen und erklären können
- **Design-Patterns:** Implementierung in Python, Konzepte allgemein

### **Erfolgsrezept für Python-fokussierte Klausur:**

- Beherrschen Sie Python mit Type-Annotations perfekt
- Verstehen Sie die Konzepte aller 4 Sprachen
- Können Sie Scala/Java Code lesen und nach Python übersetzen
- Kennen Sie die Vor-/Nachteile verschiedener Sprachdesigns

**Viel Erfolg! Mit Python als Hauptsprache sind Sie bestens gerüstet! 🐍**
