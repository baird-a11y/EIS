# Kompakte Klausurzusammenfassung (SoSe 2025)

---

## 1. Programmiersprachen im Vergleich

### Performance-Ranking

**Benchmark-Ergebnisse (Matrix-Multiplikation 500×500):**

- **C++**: 1.27s (Referenz)
- **Java**: 1.5s (+18%)
- **Scala**: 1.6s (+26%)
- **Python**: 44s (+3400%!)

### Warum ist C++ schneller?

1. **Direkter Maschinencode** - keine Interpretation zur Laufzeit
2. **Statische Typisierung** - Compiler kennt alle Typen zur Compile-Zeit
3. **Manuelles Memory Management** - keine GC-Pausen

### Sprachen-Überblick

|Sprache|Kompilierung|Memory|Typsystem|Einsatz|
|---|---|---|---|---|
|**C++**|→ Maschinencode|Manuell|Statisch|System, Embedded|
|**Java**|→ JVM-Bytecode|GC|Statisch|Enterprise, Android|
|**Scala**|→ JVM-Bytecode|GC|Sehr streng|Big Data, FP|
|**Python**|Interpretiert|GC|Dynamisch|Data Science, Prototyping|

---

## 2. Softwareentwicklungsprozess

### Die vier Hauptphasen

1. **Analyse** (SE) - Anforderungen erfassen, Use Cases
2. **Design** (EIS) - Architektur entwerfen, UML-Diagramme
3. **Implementation** (EIP) - Programmieren, Testing
4. **Weitere Aspekte** (SE) - Management, Dokumentation

### Wasserfallmodell vs. Iterativ

**Wasserfall:**

- ✅ Klare Struktur, Planbarkeit
- ❌ Späte Fehlererkennung, starre Hierarchie

**Iterativ:**

- ✅ Frühe Fehlererkennung, Flexibilität
- ❌ Komplexere Koordination

---

## 3. Versionsverwaltung

### Git Grundkommandos

```bash
git init                    # Repository erstellen
git clone <url>            # Repository kopieren
git add <file>             # Datei für Commit vormerken
git commit -m "message"    # Änderungen committen
git push origin main       # Zum Remote-Repository senden
git pull                   # Änderungen vom Remote holen
```

### Verteilte vs. Zentrale Systeme

- **Zentral (SVN)**: Ein Server, lokale Arbeit eingeschränkt
- **Verteilt (Git)**: Jeder hat komplette Historie, offline-fähig

---

## 4. Vektorgrafik-Editor (Beispielprojekt)

### Koordinatensystem-Transformation

**Problem:** Weltkoordinaten (Y↑) → Pixelkoordinaten (Y↓)

**Lösung:**

1. Normalisierung: `norm_x = (world_x - left) / width`
2. Y-Umkehrung: `pixel_y = (1.0 - norm_y) * height`

### Navigation

- **Pan**: Viewport um dx/dy verschieben
- **Zoom**: Viewport-Größe ändern, um Mausposition zentrieren

---

## 5. Prozedurale Programmierung

### Charakteristika

- **Funktionsorientiert**: Problem in Funktionen aufteilen
- **Top-Down/Bottom-Up**: Hierarchische Zerlegung
- **Datenstrukturen**: Records und Arrays

### Probleme am Vektorgrafik-Beispiel

```python
# Problem: Redundante Typprüfungen
def draw_shape(shape):
    if shape['type'] == 'rectangle':
        draw_rectangle(shape)
    elif shape['type'] == 'circle':
        draw_circle(shape)
    # Diese Struktur in JEDER Funktion!

# Neue Shape → ALLE Funktionen ändern
```

**Hauptprobleme:**

- Redundante Fallunterscheidungen
- Schwierige Erweiterbarkeit
- Fehleranfälligkeit
- Keine Datenkapselung

---

## 6. GUI-Programmierung

### Event-driven Programming

**Konzept:** Event-Loop wartet auf Ereignisse und delegiert an Handler

```python
# Event-Loop (konzeptuell)
while True:
    msg = wait_message()
    if msg.type == MOUSE_DOWN:
        handle_mouse_down(msg.x, msg.y)
    elif msg.type == KEY_PRESS:
        handle_key_press(msg.key)
```

### Qt-Framework Grundlagen

- **Widget-Hierarchie**: Baum von GUI-Elementen
- **Signal-Slot**: Lose gekoppelte Kommunikation
- **paintEvent()**: Automatisches Neuzeichnen

### Signal-Slot System

```python
# Signal-Slot Verbindung
button.clicked.connect(self.on_button_click)

# Custom Signals
shape_added = Signal(object)
shape_added.emit(new_shape)
```

---

## 7. Objektorientierte Programmierung

### Die drei Säulen

1. **Kapselung**: Daten + Methoden in Objekten
2. **Polymorphie**: Dynamic Dispatch nach Objekttyp
3. **Vererbung**: Hierarchische Code-Wiederverwendung

### OOP-Lösung für Vektorgrafik

```python
class Shape(ABC):
    @abstractmethod
    def draw(self, painter): pass
    
    @abstractmethod
    def contains_point(self, x, y): pass

class Rectangle(Shape):
    def draw(self, painter):
        painter.drawRect(self.x, self.y, self.width, self.height)
    
    def contains_point(self, x, y):
        return (self.x <= x <= self.x + self.width and 
                self.y <= y <= self.y + self.height)

# Polymorphe Verwendung
for shape in shapes:
    shape.draw(painter)  # Keine if-else nötig!
```

### Expression Problem

|Paradigma|Neue Typen|Neue Operationen|
|---|---|---|
|**OOP**|✅ Einfach (neue Klasse)|❌ Schwer (alle Klassen ändern)|
|**FP**|❌ Schwer (alle Funktionen ändern)|✅ Einfach (neue Funktion)|

---

## 8. Funktionale Programmierung

### Grundprinzipien

1. **Immutability**: Daten werden nicht verändert
2. **Pure Functions**: Keine Seiteneffekte
3. **Higher-Order Functions**: Funktionen als Parameter
4. **Deklarativ**: WAS statt WIE

### Higher-Order Functions

```python
# Map: Transformation auf alle Elemente
shapes = map_shapes(shapes, lambda s: translate_shape(s, 10, 10))

# Filter: Elemente nach Kriterium
large_shapes = filter_shapes(shapes, lambda s: get_area(s) > 1000)

# Reduce: Aggregation
total_area = reduce(lambda acc, s: acc + get_area(s), shapes, 0)
```

### Immutability Vorteile

- **Thread-sicher**: Keine Race Conditions
- **Einfaches Debugging**: Zustand ändert sich nicht unerwartet
- **Undo/Redo**: Alte Zustände bleiben erhalten
- **Caching**: Pure Functions sind memoizierbar

### Funktionale Lösung: SVG Export

```python
# Pipeline-Ansatz
def export_scene_to_svg(scene):
    return (scene.shapes
            .map(shape_to_svg)
            .join('\n')
            .wrap_in_svg_tags())
```

---

## 9. Design Patterns

### Model-View-Controller (MVC)

**Komponenten:**

- **Model**: Datenkapselung, unabhängig vom UI
- **View**: Datendarstellung, View = f(Model)
- **Controller**: Benutzerinteraktion, Event-Handling

```python
class VectorGraphicsModel:
    def add_shape(self, shape):
        self._shapes.append(shape)
        self._notify_observers('shape_added', shape)

class VectorGraphicsView(QWidget):
    def paintEvent(self, event):
        for shape in self._model.get_shapes():
            shape.draw(painter)

class VectorGraphicsController:
    def _on_mouse_press(self, event):
        if self._current_tool == 'rectangle':
            self._start_rectangle_creation(event.pos())
```

### Command Pattern

**Zweck:** Undo/Redo, Macro Recording

```python
class Command(ABC):
    def execute(self): pass
    def undo(self): pass

class AddShapeCommand(Command):
    def execute(self): model.add_shape(self.shape)
    def undo(self): model.remove_shape(self.shape)

# Usage
command_manager.execute_command(AddShapeCommand(new_rectangle))
command_manager.undo()  # Rückgängig machen
```

### Observer Pattern

**Zweck:** Lose Kopplung zwischen Objekten

```python
class Observable:
    def notify_observers(self, event_type, data):
        for observer in self._observers:
            observer.model_changed(event_type, data)

# Model ändert sich → View wird automatisch aktualisiert
```

---

## 10. Software Management & Teamwork

### Agile vs. Wasserfall

**Agile (Scrum):**

- Iterative Entwicklung (2-Wochen Sprints)
- Daily Standups, Sprint Reviews
- Kontinuierliches Feedback

**Wasserfall:**

- Sequenzielle Phasen
- Umfassende Planung vor Implementation
- Geeignet für kritische Systeme

### Git-Workflow für Teams

```bash
# Feature-Branch erstellen
git checkout -b feature/new-tool
git commit -m "Add circle tool"
git push origin feature/new-tool

# Pull Request erstellen
# Code Review
# Merge nach Approval
```

### Risikomanagement

**Typische Risiken:**

- Performance-Probleme → Frühe Tests
- Changing Requirements → Agile Ansatz
- Key Developer Unavailable → Cross-Training

---

## 11. Praktische Code-Patterns (Übungsrelevant)

### Python Type Annotations

```python
from typing import List, Dict, Any, Optional, Callable, TypeVar

# Grundlegende Typen
def filter_strings(string_array: List[str]) -> List[str]:
    return [s for s in string_array if s and len(s) >= 3 and s.startswith("test")]

# Dict mit verschiedenen Typen  
def array_operations(numbers: List[int]) -> Dict[str, Any]:
    return {
        "sum": sum(numbers),
        "max": max(numbers), 
        "even_count": len([x for x in numbers if x % 2 == 0]),
        "sorted_desc": sorted(numbers, reverse=True)
    }

# Generic Types
T = TypeVar('T')
def compose_functions(f: Callable[[T], int], g: Callable[[int], T]) -> Callable[[T], T]:
    return lambda x: g(f(x))
```

### OOP Grundmuster

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name: str, color: str) -> None:
        self.name = name
        self.color = color
    
    @abstractmethod
    def area(self) -> float:
        pass
    
    def describe(self) -> str:
        return f"{self.name} ({self.color})"

class Rectangle(Shape):
    def __init__(self, name: str, color: str, width: float, height: float) -> None:
        super().__init__(name, color)
        self.width = width
        self.height = height
    
    def area(self) -> float:
        return self.width * self.height

# Polymorphie nutzen
shapes: List[Shape] = [Rectangle("rect1", "red", 10, 5)]
for shape in shapes:
    print(f"{shape.describe()}: {shape.area()}")
```

### Funktionale Programmierung Patterns

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List Comprehensions
even_squared = [x**2 for x in numbers if x % 2 == 0]
odd_strings = [str(x) for x in numbers if x % 2 != 0]

# Map/Filter/Reduce Pattern
def functional_processing(nums: List[int]) -> int:
    even_nums = filter(lambda x: x % 2 == 0, nums)
    squared = map(lambda x: x**2, even_nums)
    return reduce(lambda x, y: x + y, squared)

# Higher-Order Functions
def apply_operations(data: List[T], operations: List[Callable[[T], T]]) -> List[T]:
    result = data
    for operation in operations:
        result = [operation(item) for item in result]
    return result
```

### GUI-Programmierung Essentials

```python
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PySide6.QtWidgets import QPushButton, QLineEdit, QTextEdit
from PySide6.QtCore import QTimer

class SimpleGUI(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setup_ui()
    
    def setup_ui(self) -> None:
        # Central Widget Setup
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        
        # Widgets hinzufügen
        self.input = QLineEdit()
        self.button = QPushButton("Process")
        self.output = QTextEdit()
        
        # Layout befüllen
        layout.addWidget(self.input)
        layout.addWidget(self.button)
        layout.addWidget(self.output)
        
        # Signal-Slot Verbindung
        self.button.clicked.connect(self.process_text)
    
    def process_text(self) -> None:
        text = self.input.text()
        self.output.setText(f"Processed: {text[::-1]}")
```

### Scala vs Python Syntax-Vergleiche

```python
# Python List Comprehension
numbers = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in numbers if x * 2 > 4]

# Entspricht Scala:
# val numbers = List(1, 2, 3, 4, 5)
# val doubled = numbers.map(_ * 2).filter(_ > 4)
```

### Performance & Memory Management

```python
# Fibonacci: Rekursiv vs Iterativ vs Memoized
def fibonacci_memoized(n: int, memo: Dict[int, int] = None) -> int:
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1 if n > 0 else 0
    memo[n] = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
    return memo[n]

# Pattern Matching Simulation
def process_input(data: Any) -> str:
    if isinstance(data, str):
        return f"Text: {data}"
    elif isinstance(data, int):
        return f"Number: {data}"
    elif isinstance(data, list):
        return f"List with {len(data)} elements"
    else:
        return f"Unknown type: {type(data)}"
```

---

## Spickzettel für die Klausur

### Performance-Zahlen

- C++: 1.27s, Java: 1.5s, Scala: 1.6s, Python: 44s

### Sprachen-Eigenschaften

||C++|Java|Scala|Python|
|---|---|---|---|---|
|**Kompilierung**|→ Maschinencode|→ Bytecode|→ Bytecode|Interpretiert|
|**Memory**|Manuell|GC|GC|GC + RefCount|
|**Typen**|Statisch|Statisch|Sehr streng|Dynamisch|

### Expression Problem

- **OOP**: Neue Typen ✅, Neue Operationen ❌
- **FP**: Neue Typen ❌, Neue Operationen ✅

### Code-Patterns Cheat Sheet

```python
# Type Annotations
def func(param: List[str]) -> Dict[str, Any]: pass

# OOP Abstraktion
class Base(ABC):
    @abstractmethod
    def method(self) -> None: pass

# List Comprehension
result = [f(x) for x in items if condition(x)]

# Functional Style
reduce(lambda a, b: a + b, map(lambda x: x**2, filter(lambda x: x > 0, nums)))

# GUI Signal-Slot
button.clicked.connect(self.handler)

# Pattern Matching
if isinstance(obj, TargetType):
    return process(obj)
```

### Scala vs Python Konzepte

```python
# Scala: val vs var
val x = 5        // unveränderlich
var y = 5        // veränderlich

# Python: List Comprehension
[x*2 for x in nums if x > 5]
# Scala: 
# nums.filter(_ > 5).map(_ * 2)

# Python @dataclass ≈ Scala case class
@dataclass
class Person:
    name: str
    age: int
```

### Memory Management

- **C++**: Manuell (new/delete, gefährlich)
- **Java**: Nur GC
- **Python**: Reference Counting + GC
- **Probleme**: C++ Dangling Pointer, Buffer Overflow

### Git Essentials

```bash
git add . && git commit -m "msg" && git push
git pull  # vor Arbeitsbeginn
git checkout -b feature/new-feature
```

### Qt Event-Handling

```python
def mousePressEvent(self, event):
    world_pos = self.pixel_to_world(event.pos())
    # Tool-spezifische Logik

def setup_ui(self):
    layout = QVBoxLayout()
    layout.addWidget(widget)
    self.button.clicked.connect(self.handler)
```

### Viewport-Transformation

```python
# Welt → Pixel
pixel_x = norm_x * width
pixel_y = (1.0 - norm_y) * height  # Y umkehren!

# Normalisierung
norm_x = (world_x - left) / world_width
```