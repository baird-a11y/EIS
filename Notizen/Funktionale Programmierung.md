# 🎯 **THEORIE-BLOCK**

### **1. Funktionale Programmierung Grundlagen** ⭐⭐⭐ **(KLAUSURRELEVANT)**

#### **1.1 Funktionales vs. Objektorientiertes Paradigma** 🔥 **(HÄUFIGE KLAUSURFRAGE)**

```python
# Objektorientiert: "Objekte tun Dinge"
shape.draw(painter)

# Funktional: "Funktionen transformieren Daten"
new_triangles = subdivide_triangles(triangles)
deformed_triangles = sine_wave_deform_triangles(new_triangles)
```

- **OO-Ansatz**: Objekte kapseln Daten und Verhalten
- **Funktionaler Ansatz**: Daten und Funktionen sind getrennt
- **Trade-off**: OO = einfach neue Typen, Funktional = einfach neue Operationen

#### **1.2 Das Expression Problem** 🔥 **(SEHR HÄUFIGE KLAUSURFRAGE)**

```python
# Problem: Neue Operation hinzufügen
# OO: Alle Klassen müssen erweitert werden
class Rectangle:
    def draw(self): pass
    def area(self): pass  # ← Muss zu ALLEN Klassen hinzugefügt werden!

class Circle:
    def draw(self): pass
    def area(self): pass  # ← Aufwändig bei vielen Shapes!

# Funktional: Einfach neue Funktion hinzufügen
def area(shape):
    if shape.type == "rectangle":
        return shape.width * shape.height
    elif shape.type == "circle":
        return π * shape.radius²
```

- **Das Problem**: Erweitern von Datentypen vs. Operationen
- **OO-Stärke**: Neue Typen hinzufügen (neue Shape-Klasse)
- **Funktionale Stärke**: Neue Operationen hinzufügen (neue Funktion)

#### **1.3 Unveränderlichkeit (Immutability)** ⭐⭐ **(KLAUSURRELEVANT)**

```python
# Funktional: Daten werden nicht verändert
def subdivide_triangle(triangle: Triangle) -> List[Triangle]:
    p1, p2, p3 = triangle
    # Original bleibt unverändert, neue Dreiecke werden erstellt
    return [new_triangle1, new_triangle2, new_triangle3, new_triangle4]

# Vs. Objektorientiert: Zustand wird verändert
shape.move(dx, dy)  # Verändert das Objekt direkt
```

- **Prinzip**: Original-Daten bleiben unverändert
- **Vorteil**: Keine Seiteneffekte, parallelisierbar
- **Nachteil**: Mehr Speicherverbrauch durch Kopien

#### **1.4 Reine Funktionen (Pure Functions)** ⭐⭐ **(KLAUSURRELEVANT)**

```python
def sine_wave_deform_point(point: Point, amplitude: float, wavelength: float, phase: float) -> Point:
    """Reine Funktion: Gleiche Eingabe → Gleiche Ausgabe, keine Seiteneffekte"""
    x, y = point
    y_offset = amplitude * sin(2 * π * x / wavelength + phase)
    return (x, y + y_offset)
```

- **Definition**: Keine Seiteneffekte, deterministische Ausgabe
- **Vorteile**: Testbar, parallelisierbar, cachebar
- **Beispiel**: Mathematische Transformationen

### **2. Funktionale Datenstrukturen** ⭐⭐⭐ **(KLAUSURRELEVANT)**

#### **2.1 Datenfluss-Architekturen** 🔥 **(HÄUFIGE KLAUSURFRAGE)**

```python
# Pipeline-Verarbeitung
rectangles = create_rectangles()
triangles = convert_to_triangles(rectangles)      # Shape → Triangles
subdivided = subdivide_triangles(triangles, 2)    # Triangles → mehr Triangles  
deformed = sine_wave_deform_triangles(subdivided) # Triangles → deformierte Triangles
svg_text = export_to_svg(deformed)                # Triangles → SVG-String
```

- **Konzept**: Daten fließen durch Transformationspipeline
- **Vorteil**: Klare Datenflüsse, zusammensetzbare Funktionen
- **Anwendung**: Compiler, Bildverarbeitung, Datenanalyse

#### **2.2 Geometrie-Extraktion für Funktionale Operationen** ⭐⭐ **(KLAUSURRELEVANT)**

```python
# Neue Schnittstelle für funktionale Transformationen
class VectorShape(ABC):
    @abstractmethod
    def draw(self, painter):         # OO-Interface
        pass
    
    @abstractmethod  
    def describe_shape(self) -> List[Triangle]:  # Funktionales Interface
        """Geometrie als Daten-Struktur zurückgeben"""
        pass
```

- **Hybrid-Ansatz**: OO für GUI, Funktional für Transformationen
- **Grund**: Komplexe Transformationen brauchen Zugriff auf Geometrie-Daten
- **Trade-off**: Mehr Interfaces, aber mehr Flexibilität

### **3. Higher-Order Functions** ⭐⭐ **(MÖGLICHE KLAUSURFRAGE)**

```python
def apply_to_all_triangles(triangles: List[Triangle], transform_func) -> List[Triangle]:
    """Higher-Order Function: Nimmt Funktion als Parameter"""
    return [transform_func(triangle) for triangle in triangles]

# Verwendung:
deformed = apply_to_all_triangles(triangles, lambda t: sine_wave_deform_triangle(t))
```

- **Definition**: Funktionen als Parameter oder Rückgabewerte
- **Beispiele**: `map()`, `filter()`, `reduce()`
- **Nutzen**: Wiederverwendbare, komponierbare Funktionen

### **4. Funktionale vs. OO Design Trade-offs** ⭐⭐⭐ **(SEHR KLAUSURRELEVANT)**

|Aspekt|Objektorientiert|Funktional|
|---|---|---|
|**Neue Typen hinzufügen**|✅ Einfach (neue Klasse)|❌ Alle Funktionen erweitern|
|**Neue Operationen**|❌ Alle Klassen erweitern|✅ Einfach (neue Funktion)|
|**Performance**|✅ Weniger Kopien|❌ Viele Daten-Kopien|
|**Parallelisierung**|❌ Geteilte Zustände|✅ Keine Seiteneffekte|
|**Testbarkeit**|⚠️ Abhängt von Zustand|✅ Reine Funktionen|
|**GUI-Programmierung**|✅ Natürlich (Events, Zustand)|❌ Kompliziert|

---

# 🛠️ **PRAXIS-BLOCK**

### **1. Geometrie-Extraktion Implementation** ⭐⭐⭐ **(KLAUSURRELEVANT)**

```python
from typing import List, Tuple
Point = Tuple[float, float]
Triangle = Tuple[Point, Point, Point]

class Rectangle(VectorShape):
    def describe_shape(self) -> List[Triangle]:
        """Rechteck als 2 Dreiecke darstellen"""
        p1 = (self.x, self.y)                           # Oben Links
        p2 = (self.x + self.width, self.y)              # Oben Rechts  
        p3 = (self.x + self.width, self.y + self.height) # Unten Rechts
        p4 = (self.x, self.y + self.height)             # Unten Links
        
        triangle1 = (p1, p2, p3)  # Diagonale von A zu C
        triangle2 = (p1, p3, p4)
        return [triangle1, triangle2]

class Circle(VectorShape):
    def describe_shape(self) -> List[Triangle]:
        """Kreis als n Dreiecke (Pizza-Stücke)"""
        center_x = self.x + self.width/2
        center_y = self.y + self.height/2
        center_point = (center_x, center_y)
        radius = min(self.width, self.height)/2
        
        num_triangles = 32  # Auflösung
        triangles = []
        
        for i in range(num_triangles):
            angle1 = i * (2 * π / num_triangles)
            angle2 = (i + 1) * (2 * π / num_triangles)
            
            x1 = center_x + radius * cos(angle1)
            y1 = center_y + radius * sin(angle1)
            x2 = center_x + radius * cos(angle2)
            y2 = center_y + radius * sin(angle2)
            
            triangle = (center_point, (x1, y1), (x2, y2))
            triangles.append(triangle)
        
        return triangles
```

### **2. Funktionale Operatoren** ⭐⭐⭐ **(KLAUSURRELEVANT)**

```python
def subdivide_triangle(triangle: Triangle) -> List[Triangle]:
    """1 Dreieck → 4 kleinere Dreiecke"""
    p1, p2, p3 = triangle
    
    # Mittelpunkte der Kanten berechnen
    m12 = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
    m23 = ((p2[0] + p3[0]) / 2, (p2[1] + p3[1]) / 2)
    m31 = ((p3[0] + p1[0]) / 2, (p3[1] + p1[1]) / 2)
    
    # 4 neue Dreiecke
    t1 = (p1, m12, m31)      # Ecke bei p1
    t2 = (p2, m23, m12)      # Ecke bei p2  
    t3 = (p3, m31, m23)      # Ecke bei p3
    t4 = (m12, m23, m31)     # Mittleres Dreieck
    
    return [t1, t2, t3, t4]

def subdivide_triangles(triangles: List[Triangle], n_times: int = 1) -> List[Triangle]:
    """n-fache Subdivision aller Dreiecke"""
    result = triangles
    for _ in range(n_times):
        new_triangles = []
        for triangle in result:
            new_triangles.extend(subdivide_triangle(triangle))
        result = new_triangles
    return result
```

### **3. Sine-Wave Deformation** ⭐⭐⭐ **(KLAUSURRELEVANT)**

```python
def sine_wave_deform_point(point: Point, amplitude: float = 50.0, 
                          wavelength: float = 200.0, phase: float = 0.0) -> Point:
    """Deformiert einen Punkt entlang einer Sinuskurve"""
    x, y = point
    y_offset = amplitude * sin(2 * π * x / wavelength + phase)
    return (x, y + y_offset)

def sine_wave_deform_triangles(triangles: List[Triangle], 
                              amplitude: float = 50.0, 
                              wavelength: float = 200.0, 
                              phase: float = 0.0) -> List[Triangle]:
    """Wendet Sine-Wave Deformation auf alle Dreiecke an"""
    deformed_triangles = []
    
    for triangle in triangles:
        p1, p2, p3 = triangle
        
        # Jeden Punkt transformieren
        new_p1 = sine_wave_deform_point(p1, amplitude, wavelength, phase)
        new_p2 = sine_wave_deform_point(p2, amplitude, wavelength, phase)
        new_p3 = sine_wave_deform_point(p3, amplitude, wavelength, phase)
        
        deformed_triangle = (new_p1, new_p2, new_p3)
        deformed_triangles.append(deformed_triangle)
    
    return deformed_triangles
```

### **4. SVG-Export (Funktionale Serialisierung)** ⭐⭐ **(KLAUSURRELEVANT)**

```python
def export_triangles_as_svg(triangles: List[Triangle], filename: str, width=800, height=600):
    """Funktionale Datenkonvertierung: Triangles → SVG-Text → Datei"""
    with open(filename, "w") as file:
        # SVG Header
        file.write(f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">\n')
        
        # Jedes Dreieck als Polygon
        for triangle in triangles:
            p1, p2, p3 = triangle
            points = f"{p1[0]},{p1[1]} {p2[0]},{p2[1]} {p3[0]},{p3[1]}"
            file.write(f'  <polygon points="{points}" fill="lightblue" stroke="black" />\n')
        
        # SVG Footer
        file.write('</svg>\n')

def export_triangles_as_text(triangles: List[Triangle], filename: str):
    """Einfacher Text-Export für Debugging"""
    with open(filename, "w") as file:
        for i, triangle in enumerate(triangles):
            p1, p2, p3 = triangle
            file.write(f"Triangle {i}: ({p1[0]}, {p1[1]}), ({p2[0]}, {p2[1]}), ({p3[0]}, {p3[1]})\n")
```

### **5. Funktionale Pipeline** ⭐⭐ **(MÖGLICHE KLAUSURFRAGE)**

```python
def create_deformed_svg(shapes: List[VectorShape], filename: str):
    """Komplette funktionale Verarbeitungspipeline"""
    
    # 1. Shapes → Triangles (Geometrie extrahieren)
    all_triangles = []
    for shape in shapes:
        triangles = shape.describe_shape()
        all_triangles.extend(triangles)
    
    # 2. Subdivision für mehr Details
    fine_triangles = subdivide_triangles(all_triangles, n_times=2)
    
    # 3. Sine-Wave Deformation
    deformed_triangles = sine_wave_deform_triangles(
        fine_triangles, 
        amplitude=30, 
        wavelength=300, 
        phase=0
    )
    
    # 4. Export als SVG
    export_triangles_as_svg(deformed_triangles, filename)
    
    print(f"Pipeline: {len(shapes)} Shapes → {len(all_triangles)} → "
          f"{len(fine_triangles)} → {len(deformed_triangles)} Triangles → {filename}")
```

### **6. Hybrid OO/Funktional Integration** ⭐⭐ **(KLAUSURRELEVANT)**

```python
class VectorGraphicsWindow(QMainWindow):
    def export_svg(self):
        """GUI-Integration: OO für Events, Funktional für Verarbeitung"""
        file_path, _ = QFileDialog.getSaveFileName(self, "SVG Export", "output.svg", "SVG Files (*.svg)")
        
        if file_path:
            # Funktionale Pipeline aufrufen
            create_deformed_svg(self.graphics_area.shapes, file_path)
            QMessageBox.information(self, "Erfolg", f"SVG exportiert: {file_path}")

    def apply_transformations(self):
        """Demo: Funktionale Operationen über GUI anwenden"""
        # Alle Shapes zu Dreiecken konvertieren
        all_triangles = []
        for shape in self.graphics_area.shapes:
            all_triangles.extend(shape.describe_shape())
        
        # Transformationen anwenden
        subdivided = subdivide_triangles(all_triangles, 1)
        deformed = sine_wave_deform_triangles(subdivided, amplitude=20)
        
        # Für Visualisierung: Neue Shape-Klasse die Triangles zeichnet
        triangle_shape = TriangleCollection(deformed)
        self.graphics_area.shapes.append(triangle_shape)
        self.graphics_area.update()
```

---

## 🔥 **KLAUSUR-CHECKLISTE**

### **Sehr wahrscheinliche Fragen (90%):**

- [ ] **Expression Problem**: OO vs. Funktional, Vor-/Nachteile erklären
- [ ] **Geometrie-Extraktion**: `describe_shape()` für Rectangle/Circle implementieren
- [ ] **Funktionale Operatoren**: Subdivision oder Sine-Wave implementieren
- [ ] **Unveränderlichkeit**: Warum und wie funktionale Datenstrukturen

### **Wahrscheinliche Fragen (70%):**

- [ ] **Reine Funktionen**: Definition und Vorteile
- [ ] **Datenfluss-Pipeline**: Mehrere Transformationen verketten
- [ ] **SVG-Export**: Triangles → XML-String Konvertierung
- [ ] **Hybrid-Programmierung**: Wann OO, wann funktional

### **Mögliche Fragen (40%):**

- [ ] **Higher-Order Functions**: `map()`, `filter()` auf Triangles anwenden
- [ ] **Lazy Evaluation**: On-demand Berechnung von Transformationen
- [ ] **Parallelisierung**: Warum funktional besser parallelisierbar
- [ ] **Trade-off Analyse**: Performance vs. Flexibilität

### **Typische Aufgabentypen:**

1. **Pipeline implementieren**: Shapes → Triangles → Transformation → Export
2. **Expression Problem**: Code zeigen der neue Operation/Type hinzufügt
3. **Subdivision-Algorithmus**: 1 Dreieck in 4 aufteilen
4. **Sine-Wave Formel**: Punkttransformation implementieren
5. **SVG-Format**: Polygon-Element für Dreieck erstellen

### **Wichtige Formeln/Konzepte auswendig können:**

```python
# Subdivision: Mittelpunkte berechnen
m12 = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

# Sine-Wave Deformation
y_offset = amplitude * sin(2 * π * x / wavelength + phase)

# SVG Polygon-Format
f'<polygon points="{x1},{y1} {x2},{y2} {x3},{y3}" fill="color" />'

# Funktionale Pipeline
data → transform1 → transform2 → transform3 → output
```

---

## 📝 **Schnell-Referenz für die Klausur**

```python
# Funktionale Geometrie-Extraktion
@abstractmethod
def describe_shape(self) -> List[Triangle]:
    pass

# Subdivision (1→4 Dreiecke)
def subdivide_triangle(triangle):
    p1, p2, p3 = triangle
    m12 = midpoint(p1, p2)  # Mittelpunkte
    m23 = midpoint(p2, p3)
    m31 = midpoint(p3, p1)
    return [(p1,m12,m31), (p2,m23,m12), (p3,m31,m23), (m12,m23,m31)]

# Sine-Wave Transformation
def deform_point(point, amplitude, wavelength):
    x, y = point
    y_new = y + amplitude * sin(2*π*x/wavelength)
    return (x, y_new)

# SVG Export
def to_svg(triangles):
    svg = '<svg>'
    for p1, p2, p3 in triangles:
        points = f"{p1[0]},{p1[1]} {p2[0]},{p2[1]} {p3[0]},{p3[1]}"
        svg += f'<polygon points="{points}"/>'
    svg += '</svg>'
    return svg

# Expression Problem Trade-off
# OO: Einfach neue Shapes, schwer neue Operationen
# Funktional: Schwer neue Shapes, einfach neue Operationen
```