

# **🎯 Kernkonzepte Objektorientierte Programmierung (OOP)**

#### **1. Abstrakte Klassen**

```python
from abc import ABC, abstractmethod

class VectorShape(ABC):
    @abstractmethod
    def draw(self, painter, zoom, offset_x, offset_y):
        pass
```

- **Zweck**: Definiert Interface, verhindert direkte Instanziierung
- **Verwendung**: Gemeinsame Struktur für verwandte Klassen

#### **2. Vererbung (Inheritance)**

```python
class Rectangle(VectorShape):
    def draw(self, painter, zoom, offset_x, offset_y):
        # Spezifische Implementierung
```

- **Vorteil**: Code-Wiederverwendung
- **Prinzip**: Unterklassen erben Eigenschaften und Methoden

#### **3. Polymorphismus**

```python
shapes = [Rectangle(...), Circle(...), Star(...)]
for shape in shapes:
    shape.draw(painter, zoom, offset_x, offset_y)  # Gleicher Aufruf, verschiedene Implementierungen
```

- **Definition**: Gleiche Schnittstelle, unterschiedliche Implementierung
- **Nutzen**: Flexibler, erweiterbarer Code

#### **4. Kapselung (Encapsulation)**

```python
def set_position(self, x, y):
    self.x = x
    self.y = y
```

- **Prinzip**: Kontrolle über Datenzugriff
- **Vorteil**: Validierung und Konsistenz möglich

### **🛠️ Praktische Design-Patterns**

#### **Template Method Pattern**

- **Oberklasse** definiert Struktur (`VectorShape`)
- **Unterklassen** implementieren Details (`Rectangle.draw()`)

#### **Strategy Pattern** (implizit)

- Verschiedene Zeichen-Strategien für verschiedene Formen
- Austauschbare Algorithmen durch gemeinsame Schnittstelle

### **📊 Architektur-Prinzipien**

#### **SOLID Principles (angewendet):**

- **S** - Single Responsibility: Jede Klasse hat eine Aufgabe
- **O** - Open/Closed: Erweiterbar ohne Änderung bestehenden Codes
- **L** - Liskov Substitution: Unterklassen sind austauschbar
- **I** - Interface Segregation: Klare, fokussierte Schnittstellen
- **D** - Dependency Inversion: Abhängigkeit von Abstraktionen

#### **Erweiterbarkeit**

```python
# Neue Form hinzufügen:
class Triangle(VectorShape):
    def draw(self, painter, zoom, offset_x, offset_y): ...
    def hit_test(self, point_x, point_y): ...
```

- Keine Änderung an bestehenden Klassen nötig!

### **🎨 GUI-Architektur Erkenntnisse**

#### **Model-View Trennung**

- **Model**: `VectorShape` und Unterklassen (Daten + Logik)
- **View**: `VectorGraphicsArea` (Darstellung)
- **Controller**: Event-Handler (Maus-Interaktion)

#### **Hit-Testing für Interaktivität**

```python
def hit_test(self, point_x, point_y):
    return (self.x <= point_x <= self.x + self.width and 
            self.y <= point_y <= self.y + self.height)
```

- **Bounding Box**: Effizient, einfach zu implementieren
- **Pixel-Perfect**: Genauer, aber aufwendiger

---

## **🚀 Nächste Schritte**

Du bist bereit für **Übungsblatt 05: Funktionale Programmierung**!

**Was dich erwartet:**

- Kombinieren von OOP und funktionalen Konzepten
- Higher-Order Functions
- Immutable Data Structures
- Functional Interfaces

**Möchtest du direkt weitermachen oder hast du Fragen zu den OOP-Konzepten?**