# 🎯 **THEORIE-BLOCK**

### **1. Grundkonzepte der OOP** ⭐⭐⭐ **(KLAUSURRELEVANT)**

#### **1.1 Abstrakte Klassen** 🔥 **(HÄUFIGE KLAUSURFRAGE)**

```python
from abc import ABC, abstractmethod

class VectorShape(ABC):
    @abstractmethod
    def draw(self, painter, zoom, offset_x, offset_y):
        pass
```

- **Zweck**: Definiert Interface, verhindert direkte Instanziierung
- **Verwendung**: Gemeinsame Struktur für verwandte Klassen
- **Python-Syntax**: `ABC` und `@abstractmethod`

#### **1.2 Vererbung (Inheritance)** ⭐⭐⭐ **(KLAUSURRELEVANT)**

```python
class Rectangle(VectorShape):
    def draw(self, painter, zoom, offset_x, offset_y):
        # Spezifische Implementierung
```

- **IS-A Beziehung**: Rectangle ist ein VectorShape
- **Vorteil**: Code-Wiederverwendung, gemeinsame Schnittstelle
- **Prinzip**: Unterklassen erben Eigenschaften und Methoden

#### **1.3 Polymorphismus** 🔥 **(SEHR HÄUFIGE KLAUSURFRAGE)**

```python
shapes = [Rectangle(...), Circle(...), Star(...)]
for shape in shapes:
    shape.draw(painter, zoom, offset_x, offset_y)  # Gleicher Aufruf, verschiedene Implementierungen
```

- **Definition**: Gleiche Schnittstelle, unterschiedliche Implementierung
- **Nutzen**: Flexibler, erweiterbarer Code
- **Laufzeit-Binding**: Methode wird zur Laufzeit aufgelöst

#### **1.4 Kapselung (Encapsulation)** ⭐⭐ **(KLAUSURRELEVANT)**

```python
class Shape:
    def __init__(self):
        self._x = 0          # Protected (Konvention)
        self.__secret = 42   # Private (Name Mangling)
    
    @property
    def x(self):             # Getter
        return self._x
    
    @x.setter
    def x(self, value):      # Setter mit Validierung
        if value >= 0:
            self._x = value

def set_position(self, x, y):
    self.x = x
    self.y = y
```

- **Prinzip**: Kontrolle über Datenzugriff
- **Information Hiding**: Private/Protected Variablen
- **Vorteil**: Validierung und Konsistenz möglich

#### **1.5 Komposition vs. Vererbung** ⭐⭐ **(MÖGLICHE KLAUSURFRAGE)**

```python
# Vererbung: IS-A Beziehung
class Rectangle(VectorShape):
    pass

# Komposition: HAS-A Beziehung
class Shape:
    def __init__(self):
        self.style = DrawingStyle()  # Shape HAS-A DrawingStyle
```

- **Komposition**: Objekt enthält andere Objekte
- **Wann Vererbung**: IS-A Beziehung, gemeinsame Schnittstelle
- **Wann Komposition**: HAS-A Beziehung, Flexibilität

### **2. Design Patterns** ⭐⭐ **(KLAUSURRELEVANT)**

#### **2.1 Template Method Pattern** 🔥 **(HÄUFIGE KLAUSURFRAGE)**

```python
class VectorShape(ABC):
    @abstractmethod
    def draw(self, painter, zoom, offset_x, offset_y):
        pass
    
    def render(self, painter, zoom, offset_x, offset_y):
        # Template-Methode
        self.setup_drawing(painter)
        self.draw(painter, zoom, offset_x, offset_y)
        self.cleanup_drawing(painter)
```

- **Oberklasse** definiert Struktur/Algorithmus
- **Unterklassen** implementieren spezifische Schritte
- **Anwendung**: Gemeinsamer Ablauf, verschiedene Implementierungen

#### **2.2 Strategy Pattern** ⭐⭐ **(MÖGLICHE KLAUSURFRAGE)**

```python
class DrawingStrategy(ABC):
    @abstractmethod
    def draw(self, shape): pass

class VectorDrawing(DrawingStrategy):
    def draw(self, shape): pass

class RasterDrawing(DrawingStrategy):
    def draw(self, shape): pass
```

- **Verschiedene Algorithmen** für gleiche Aufgabe
- **Austauschbare Strategien** zur Laufzeit
- **Anwendung**: Verschiedene Zeichen-/Berechnungsverfahren

#### **2.3 Factory Pattern** ⭐ **(MÖGLICHE KLAUSURFRAGE)**

```python
class ShapeFactory:
    @staticmethod
    def create_shape(shape_type, x, y, width, height):
        if shape_type == "rectangle":
            return Rectangle(x, y, width, height)
        elif shape_type == "circle":
            return Circle(x, y, width, height)
        elif shape_type == "star":
            return Star(x, y, width, height)
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")
```

- **Objekt-Erzeugung** wird delegiert
- **Zentrale Stelle** für Instanziierung
- **Vorteil**: Entkopplung, einfache Erweiterung

#### **2.4 Observer Pattern** ⭐ **(MÖGLICHE KLAUSURFRAGE)**

```python
class Observable:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def notify(self, event):
        for observer in self._observers:
            observer.update(event)
```

- **Lose Kopplung** zwischen Objekten
- **Automatische Benachrichtigung** bei Änderungen
- **Anwendung**: GUI-Events, Model-View-Architekturen

### **3. Architektur-Prinzipien** ⭐⭐⭐ **(SEHR KLAUSURRELEVANT)**

#### **3.1 SOLID Principles** 🔥 **(SEHR HÄUFIGE KLAUSURFRAGE)**

**S - Single Responsibility Principle:**

```python
class Rectangle:
    def __init__(self, x, y, width, height):
        # NUR für Rechteck-Daten verantwortlich
        pass
    
    def draw(self, painter):
        # NUR für Rechteck-Zeichnung verantwortlich
        pass
```

**O - Open/Closed Principle:**

```python
# Erweiterbar ohne Änderung bestehenden Codes
class Triangle(VectorShape):  # NEU hinzufügen
    def draw(self, painter, zoom, offset_x, offset_y): pass
    def hit_test(self, point_x, point_y): pass
# Keine Änderung an VectorShape oder anderen Klassen nötig!
```

**L - Liskov Substitution Principle:**

```python
def render_shapes(shapes: List[VectorShape]):
    for shape in shapes:
        shape.draw(painter, zoom, offset_x, offset_y)
# Jede Unterklasse von VectorShape muss hier funktionieren
```

**I - Interface Segregation:**

```python
class Drawable(ABC):
    @abstractmethod
    def draw(self): pass

class Transformable(ABC):
    @abstractmethod
    def transform(self): pass
# Getrennte, fokussierte Interfaces
```

**D - Dependency Inversion:**

```python
class VectorGraphicsArea:
    def __init__(self, shapes: List[VectorShape]):  # Abhängig von Abstraktion
        self.shapes = shapes  # nicht von konkreten Klassen
```

#### **3.2 Model-View-Controller (MVC)** ⭐⭐ **(KLAUSURRELEVANT)**

- **Model**: `VectorShape` und Unterklassen (Daten + Logik)
- **View**: `VectorGraphicsArea` (Darstellung)
- **Controller**: Event-Handler (Maus-Interaktion, Menüs)

### **4. Trade-offs und Wann OOP verwenden** ⭐⭐ **(MÖGLICHE KLAUSURFRAGE)**

#### **Vorteile von OOP:**

- **Wartbarkeit**: Klare Struktur, getrennte Verantwortlichkeiten
- **Erweiterbarkeit**: Neue Klassen ohne Änderung bestehender
- **Code-Wiederverwendung**: Vererbung, Komposition
- **Abstraktion**: Komplexität verbergen

#### **Nachteile von OOP:**

- **Komplexität**: Kann over-engineered werden
- **Performance-Overhead**: Methodenaufrufe, Vererbung
- **Lernkurve**: Schwieriger für Anfänger

#### **Wann OOP verwenden:**

- Komplexe Systeme mit vielen ähnlichen Objekten
- GUI-Anwendungen (natürliche Objekthierarchie)
- Wenn Erweiterbarkeit wichtig ist
- Team-Entwicklung (klare Schnittstellen)

---

# 🛠️ **PRAXIS-BLOCK**

### **1. Implementierung Abstrakte Klassen** ⭐⭐⭐ **(KLAUSURRELEVANT)**

```python
from abc import ABC, abstractmethod

class VectorShape(ABC):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = QColor(200, 200, 200, 100)
        self.line_width = 2
        self.fill_color = QColor(255, 255, 255)

    @abstractmethod
    def draw(self, painter, zoom, offset_x, offset_y):
        """Wird in Unterklassen überschrieben"""
        pass

    @abstractmethod
    def hit_test(self, point_x, point_y) -> bool:
        """Prüft, ob der Punkt innerhalb des Objekts liegt"""
        pass
```

### **2. Vererbung und Polymorphismus** ⭐⭐⭐ **(KLAUSURRELEVANT)**

```python
class Rectangle(VectorShape):
    def draw(self, painter, zoom, offset_x, offset_y):
        x = (self.x + offset_x) * zoom
        y = (self.y + offset_y) * zoom
        w = self.width * zoom
        h = self.height * zoom
        
        pen = QPen(self.color, self.line_width)
        brush = QColor(self.fill_color)
        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawRect(x, y, w, h)

    def hit_test(self, point_x, point_y):
        return (self.x <= point_x <= self.x + self.width and 
                self.y <= point_y <= self.y + self.height)
```

### **3. Kapselung mit Properties** ⭐⭐ **(MÖGLICHE KLAUSURFRAGE)**

```python
class VectorShape(ABC):
    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        if value >= 0:
            self._x = value
        else:
            raise ValueError("x must be non-negative")
    
    def set_position(self, x, y):
        """Kontrollierte Methode für Positionsänderung"""
        self.x = x
        self.y = y

    def move(self, dx, dy):
        """Relative Verschiebung"""
        self.x += dx
        self.y += dy
```

### **4. Hit-Testing für GUI-Interaktivität** ⭐⭐ **(KLAUSURRELEVANT)**

```python
def hit_test(self, point_x, point_y):
    # Axis-Aligned Bounding Box Test
    return (self.x <= point_x <= self.x + self.width and 
            self.y <= point_y <= self.y + self.height)

# Erweitert: Pixelgenaues Hit-Testing für Kreis
class Circle(VectorShape):
    def hit_test(self, point_x, point_y):
        center_x = self.x + self.width / 2
        center_y = self.y + self.height / 2
        radius = min(self.width, self.height) / 2
        
        distance = ((point_x - center_x) ** 2 + (point_y - center_y) ** 2) ** 0.5
        return distance <= radius
```

### **5. Erweiterbarkeit demonstrieren** ⭐⭐ **(MÖGLICHE KLAUSURFRAGE)**

```python
# Neue Form hinzufügen ohne Änderung bestehender Klassen:
class Triangle(VectorShape):
    def __init__(self, x, y, width, height, points=None):
        super().__init__(x, y, width, height)
        self.points = points or [
            (x, y + height),           # Unten links
            (x + width/2, y),          # Oben mitte
            (x + width, y + height)    # Unten rechts
        ]
    
    def draw(self, painter, zoom, offset_x, offset_y):
        transformed_points = []
        for px, py in self.points:
            tx = (px + offset_x) * zoom
            ty = (py + offset_y) * zoom
            transformed_points.append(QPoint(int(tx), int(ty)))
        
        polygon = QPolygon(transformed_points)
        pen = QPen(self.color, self.line_width)
        brush = QColor(self.fill_color)
        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawPolygon(polygon)
    
    def hit_test(self, point_x, point_y):
        return (self.x <= point_x <= self.x + self.width and 
                self.y <= point_y <= self.y + self.height)
```

### **6. Factory Pattern Anwendung** ⭐ **(MÖGLICHE KLAUSURFRAGE)**

```python
class ShapeFactory:
    @staticmethod
    def create_shape(shape_type, x, y, width, height, **kwargs):
        if shape_type.lower() == "rectangle":
            return Rectangle(x, y, width, height)
        elif shape_type.lower() == "circle":
            return Circle(x, y, width, height)
        elif shape_type.lower() == "star":
            points = kwargs.get('points', 5)
            return Star(x, y, width, height, points)
        elif shape_type.lower() == "triangle":
            return Triangle(x, y, width, height)
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")

# Verwendung:
shapes = [
    ShapeFactory.create_shape("rectangle", 10, 10, 100, 50),
    ShapeFactory.create_shape("circle", 50, 50, 80, 80),
    ShapeFactory.create_shape("star", 100, 100, 60, 60, points=6)
]
```

---

## 🔥 **KLAUSUR-CHECKLISTE**

### **Sehr wahrscheinliche Fragen (90%):**

- [ ] **Abstrakte Klassen**: Definition, Syntax, Verwendung
- [ ] **Polymorphismus**: Beispiel schreiben, Vorteile erklären
- [ ] **Vererbung**: IS-A vs HAS-A, `super()` verwenden
- [ ] **SOLID Principles**: Alle 5 erklären und Beispiele geben

### **Wahrscheinliche Fragen (70%):**

- [ ] **Template Method Pattern**: Struktur und Anwendung
- [ ] **Kapselung**: Private/Protected Variablen, Properties
- [ ] **Hit-Testing**: Bounding Box vs. pixelgenau
- [ ] **MVC-Architektur**: Trennung der Verantwortlichkeiten

### **Mögliche Fragen (40%):**

- [ ] **Factory Pattern**: Wann verwenden, Implementierung
- [ ] **Observer Pattern**: Event-System implementieren
- [ ] **Strategy Pattern**: Verschiedene Algorithmen austauschbar machen
- [ ] **Komposition vs. Vererbung**: Wann welches Prinzip

### **Typische Aufgabentypen:**

1. **Code vervollständigen**: Abstrakte Klasse + Unterklassen
2. **Design Pattern erkennen**: Welches Pattern wird verwendet?
3. **SOLID-Prinzip anwenden**: Code verbessern
4. **Erweiterung**: Neue Klasse hinzufügen ohne bestehenden Code zu ändern
5. **Fehler finden**: Verletzung von OOP-Prinzipien identifizieren

### **Wichtige Code-Snippets auswendig können:**

- Abstrakte Klasse mit `ABC` und `@abstractmethod`
- Vererbung mit `super().__init__()`
- Properties mit `@property` und `@setter`
- Factory-Methode mit `@staticmethod`

---

## 📝 **Schnell-Referenz für die Klausur**

```python
# Abstrakte Klasse
class Shape(ABC):
    @abstractmethod
    def draw(self): pass

# Vererbung
class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    
    def draw(self):  # Implementierung der abstrakten Methode
        pass

# Polymorphismus
shapes = [Circle(5), Rectangle(10, 20)]
for shape in shapes:
    shape.draw()  # Verschiedene draw() werden aufgerufen

# Properties
@property
def x(self): return self._x

@x.setter  
def x(self, value): self._x = value

# Factory
@staticmethod
def create(type): 
    if type == "circle": return Circle()
```