**WICHTIG: Nur 2 DIN-A4 Blätter erlaubt, handbeschrieben, eigenhändig angefertigt!**

---

## **BLATT 1 - SEITE 1: PYTHON SYNTAX ESSENTIALS**

### **Type-Annotations (PFLICHT in Klausur!)**

```python
# Basis
name: str = "text"
age: int = 25
price: float = 19.99
active: bool = True

# Collections  
numbers: list[int] = [1,2,3]
grades: dict[str,float] = {"Math":1.3}
point: tuple[int,int] = (10,20)

# Optional/Union
maybe: Optional[str] = None
value: Union[int,str] = 123

# Funktionen
def calc(data: list[int]) -> dict[str,int]:
    return {"sum": sum(data)}

# Klassen
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
```

### **OOP Basics (häufig in Klausur)**

```python
# Abstrakte Klassen
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self) -> float: pass

class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius
    def area(self) -> float:
        return 3.14 * self.radius ** 2

# Vererbung
class Student(Person):
    def __init__(self, name: str, age: int, id: str) -> None:
        super().__init__(name, age)
        self.student_id = id

# Dataclass
from dataclasses import dataclass
@dataclass
class Point:
    x: int
    y: int
```

### **Listen/Funktional (wichtig für Arrays)**

```python
# List Comprehensions
evens = [x for x in range(10) if x%2==0]
squares = [x**2 for x in numbers]

# map/filter/reduce
from functools import reduce
doubled = list(map(lambda x: x*2, nums))
evens = list(filter(lambda x: x%2==0, nums))
total = reduce(lambda a,b: a+b, nums)

# String-Array Processing (Klausur-Typ!)
def filter_strings(strings: list[str]) -> list[str]:
    return [s for s in strings if s and len(s)>=3 and s.startswith("test")]
```

---

## **BLATT 1 - SEITE 2: GUI PATTERNS (ereignisorientiert)**

### **PySide6 Grundgerüst (70-80% Klausur-Anteil!)**

```python
from PySide6.QtWidgets import *
from PySide6.QtCore import QTimer
from PySide6.QtGui import QAction, QKeySequence

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setup_ui()
    
    def setup_ui(self) -> None:
        # Central Widget
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        
        # Button + Signal
        btn = QPushButton("Click")
        btn.clicked.connect(self.on_click)
        layout.addWidget(btn)
        
        # Input/Output
        self.input = QLineEdit()
        self.output = QTextEdit()
        layout.addWidget(self.input)
        layout.addWidget(self.output)
        
        # Menu (häufig in Klausur!)
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        
        open_action = QAction("Open", self)
        open_action.setShortcut(QKeySequence.Open)  # Ctrl+O
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)
        
        # Statusbar mit Timer
        self.statusBar().showMessage("Ready")
        timer = QTimer()
        timer.timeout.connect(self.update_time)
        timer.start(1000)  # 1 Sekunde
    
    def on_click(self) -> None:
        text = self.input.text()
        self.output.setText(f"Processed: {text[::-1]}")  # Umkehren
    
    def open_file(self) -> None:
        # Dummy für Klausur
        self.statusBar().showMessage("File opened")
```

### **Layouts (wichtig für komplexere GUIs)**

```python
# Grid Layout
grid = QGridLayout()
grid.addWidget(QLabel("Name:"), 0, 0)
grid.addWidget(QLineEdit(), 0, 1)

# Horizontal/Vertical
hbox = QHBoxLayout()
hbox.addWidget(QPushButton("1"))
hbox.addWidget(QPushButton("2"))

vbox = QVBoxLayout()
vbox.addLayout(hbox)
vbox.addWidget(QTextEdit())
```

---

## **BLATT 2 - SEITE 1: DESIGN PATTERNS (OOP-Entwurf)**

### **Singleton (Thread-Safe)**

```python
import threading
class Database:
    _instance: Optional['Database'] = None
    _lock = threading.Lock()
    
    def __new__(cls) -> 'Database':
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
```

### **Observer (ereignisorientiert)**

```python
from typing import Protocol
class Observer(Protocol):
    def update(self, temp: float, humid: float) -> None: pass

class WeatherStation:
    def __init__(self) -> None:
        self._observers: list[Observer] = []
        self._temp: float = 0.0
    
    def attach(self, obs: Observer) -> None:
        self._observers.append(obs)
    
    def notify(self) -> None:
        for obs in self._observers:
            obs.update(self._temp, 50.0)
    
    def set_temp(self, temp: float) -> None:
        self._temp = temp
        self.notify()

class Display:
    def update(self, temp: float, humid: float) -> None:
        print(f"Temp: {temp}°C, Humidity: {humid}%")
```

### **Factory**

```python
class ShapeFactory:
    @staticmethod
    def create(shape_type: str, **kwargs) -> 'Shape':
        if shape_type == "circle":
            return Circle(kwargs["radius"])
        elif shape_type == "rect":
            return Rectangle(kwargs["width"], kwargs["height"])
        raise ValueError(f"Unknown: {shape_type}")
```

### **Strategy**

```python
class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data: list[int]) -> list[int]: pass

class BubbleSort(SortStrategy):
    def sort(self, data: list[int]) -> list[int]:
        arr = data.copy()
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

class Context:
    def __init__(self, strategy: SortStrategy) -> None:
        self._strategy = strategy
    def sort(self, data: list[int]) -> list[int]:
        return self._strategy.sort(data)
```

---

## **BLATT 2 - SEITE 2: KONZEPTE & KLAUSUR-TIPPS**

### **Sprachvergleiche (20-30% Theorie-Anteil)**

**Python vs Scala Syntax:**

```python
# Python
evens = [x*2 for x in nums if x%2==0]
def add(a: int, b: int) -> int: return a+b

# Scala Equivalent  
val evens = nums.filter(_%2==0).map(_*2)
def add(a: Int, b: Int): Int = a + b
```

**Wichtige Konzeptunterschiede:**

- **Python:** Dynamisch typisiert, Duck Typing, Reference Counting + GC
- **Scala:** Statisch typisiert, Typ-Inferenz, JVM Garbage Collection
- **Java:** Statisch, Interfaces, keine Mehrfachvererbung, GC
- **C++:** Statisch, Multiple Inheritance, manuelle Speicherverwaltung

**Warum C++ Pointer gefährlicher:**

- Null-Pointer Dereferencing → Crash
- Memory Leaks (new ohne delete)
- Buffer Overflow möglich
- Dangling Pointers nach delete

### **Threading Essentials**

```python
import threading, queue, time

# Basic Thread
def worker(id: int) -> None:
    print(f"Worker {id} done")

t = threading.Thread(target=worker, args=(1,))
t.start(); t.join()

# Thread-Safe Counter
class SafeCounter:
    def __init__(self) -> None:
        self._value = 0
        self._lock = threading.Lock()
    def increment(self) -> None:
        with self._lock:
            self._value += 1

# Producer-Consumer
def producer(q: queue.Queue) -> None:
    for i in range(5):
        q.put(f"item_{i}")

def consumer(q: queue.Queue) -> None:
    while not q.empty():
        item = q.get()
        print(f"Processing {item}")
        q.task_done()
```

### **Algorithmen Quick Reference**

```python
# Binary Search (rekursiv)
def bin_search(arr: list[int], target: int, left: int=0, right: int=None) -> int:
    if right is None: right = len(arr)-1
    if left > right: return -1
    mid = (left + right) // 2
    if arr[mid] == target: return mid
    elif arr[mid] > target: return bin_search(arr, target, left, mid-1)
    else: return bin_search(arr, target, mid+1, right)

# Fibonacci (memoized)
def fib(n: int, memo: dict[int,int] = None) -> int:
    if memo is None: memo = {}
    if n in memo: return memo[n]
    if n <= 1: return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
```

### **🚨 KLAUSUR-SURVIVAL-GUIDE**

**Erlaubt/Gefordert:** ✅ Type-Annotations ÜBERALL verwenden ✅ Pseudocode wenn Syntax vergessen: `# Prüfe_Typ(obj, typ) statt isinstance` ✅ Python ODER Scala, freie Wahl pro Aufgabe ✅ Deutsche oder englische Antworten

**Klausur-Struktur:**

- **70-80% Praxis:** GUI, OOP, Funktional, Arrays
- **20-30% Theorie:** Sprachvergleiche, Konzepte
- **Wahlaufgabe:** Standard ODER "Scala für Wiederholer" (nur eine lösen!)

**Typische Dummy-APIs (wie Altklausur):**

```python
class EISPainter:
    def set_pixel(self, x: int, y: int, color: bool) -> None: pass

class EISWidget(ABC):
    def mouse_down(self, x: int, y: int) -> None: pass
    def paint(self, painter: EISPainter) -> None: pass
```

**Last-Minute Tipps:** 🎯 Eine eindeutige Lösung pro Aufgabe 🎯 Falsche Lösungen durchstreichen  
🎯 Saubere Einrückung (Python!) 🎯 Wahlaufgabe klar markieren 🎯 Kein Taschenrechner nötig 🎯 3 Stunden Zeit - gut einteilen!