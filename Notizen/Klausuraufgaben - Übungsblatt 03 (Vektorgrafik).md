
# Aufgabe 1: Koordinaten-Transformationen (15 Punkte)

### a) Grundlegende Transformation (5 Punkte)

Ein Rechteck befindet sich in der Welt an Position `(80, 60)` mit Breite `120` und Höhe `90`.

**Gegeben:**

- Zoom-Faktor: `1.5`
- Pan-Offset: `(20, -10)`

**Berechnen Sie die Bildschirm-Koordinaten:**

- Linke obere Ecke: `(?, ?)`
- Rechte untere Ecke: `(?, ?)`

### b) Umkehr-Transformation (5 Punkte)

Ein Mausklick erfolgt an Bildschirm-Position `(180, 135)`.

**Gegeben:**

- Zoom-Faktor: `2.0`
- Pan-Offset: `(15, 25)`

**Berechnen Sie die entsprechende Welt-Koordinate.**

### c) Zoom um Mausposition (5 Punkte)

**Situation:** Zoom-Faktor soll von `1.0` auf `2.0` geändert werden. Die Mausposition `(200, 150)` soll nach dem Zoom an derselben Bildschirmposition bleiben.

**Gegeben vor Zoom:**

- Pan-Offset: `(10, 5)`
- Mausposition: `(200, 150)`

**Berechnen Sie den neuen Pan-Offset.**

---

# Aufgabe 2: Stern-Mathematik (20 Punkte)

### a) Grundlagen (8 Punkte)

**Zeichnen Sie einen 6-zackigen Stern:**

- Mittelpunkt: `(100, 100)`
- Äußerer Radius: `50`
- Innerer Radius: `25`

**Berechnen Sie die ersten 4 Punkte (Index 0-3):**

- Punkt 0: `(?, ?)`
- Punkt 1: `(?, ?)`
- Punkt 2: `(?, ?)`
- Punkt 3: `(?, ?)`

### b) Algorithmus (12 Punkte)

**Implementieren Sie die `calculate_star_points()` Funktion:**

```python
def calculate_star_points(center_x, center_y, outer_radius, inner_radius, num_points):
    """
    Berechnet die Koordinaten für einen Stern.
    
    Args:
        center_x, center_y: Mittelpunkt
        outer_radius: Äußerer Radius
        inner_radius: Innerer Radius  
        num_points: Anzahl Zacken
    
    Returns:
        List[tuple]: Liste von (x, y) Koordinaten
    """
    points = []
    # TODO: Implementierung
    
    return points
```

**Hinweis:** Verwenden Sie `math.cos()`, `math.sin()` und `math.pi`

---

# Aufgabe 3: Qt Event-Handling (25 Punkte)

### a) Mouse-Events (15 Punkte)

**Implementieren Sie die Pan-Funktionalität:**

```python
class VectorGraphicsArea(QWidget):
    def __init__(self):
        super().__init__()
        self.panning = False
        self.last_pan_point = None
        self.offset_x = 0.0
        self.offset_y = 0.0
        self.zoom_factor = 1.0
    
    def mousePressEvent(self, event):
        # TODO: Implementierung
        pass
    
    def mouseMoveEvent(self, event):
        # TODO: Implementierung
        pass
    
    def mouseReleaseEvent(self, event):
        # TODO: Implementierung  
        pass
```

**Anforderungen:**

- Pan mit rechter Maustaste
- Offset korrekt berechnen (Zoom berücksichtigen!)
- self.update() aufrufen

### b) Wheel-Event (10 Punkte)

**Implementieren Sie Zoom mit Mausrad:**

```python
def wheelEvent(self, event):
    # TODO: Zoom-Richtung bestimmen
    # TODO: Zoom-Faktor begrenzen (0.1 bis 10.0)
    # TODO: self.update() aufrufen
    pass
```

---

# Aufgabe 4: Objektorientierte Struktur (20 Punkte)

### a) Klassenhierarchie (8 Punkte)

**Entwerfen Sie die Vererbungshierarchie:**

```
VectorShape (abstrakt)
├── ?
├── ?
└── ?
```

**Welche Attribute gehören in die Basisklasse?** **Welche Methoden sollten abstrakt sein?**

### b) Rectangle-Implementierung (12 Punkte)

**Implementieren Sie die Rectangle-Klasse:**

```python
class Rectangle(VectorShape):
    def draw(self, painter, zoom, offset_x, offset_y):
        # TODO: Koordinaten transformieren
        # TODO: QPainter konfigurieren (Pen, Brush)
        # TODO: Rechteck zeichnen
        pass
```

**Berücksichtigen Sie:**

- Koordinaten-Transformation
- Rand- und Füllfarbe
- Integer-Koordinaten für drawing

---

# Aufgabe 5: Qt-Dialog (15 Punkte)

**Implementieren Sie einen Dialog zum Hinzufügen eines Kreises:**

```python
def show_add_circle_dialog(self):
    """Dialog für neuen Kreis"""
    # TODO: QDialog erstellen
    # TODO: Eingabefelder für X, Y, Durchmesser
    # TODO: OK/Abbrechen Buttons
    # TODO: Bei OK: Kreis zu self.shapes hinzufügen
    pass
```

**Anforderungen:**

- QSpinBox für Eingaben mit sinnvollen Bereichen
- Proper Layout (QGridLayout)
- Button-Events korrekt verbinden
- Validation (Durchmesser > 0)

---

# Aufgabe 6: Debugging (5 Punkte)

**Finden Sie die Fehler im Code:**

```python
class VectorGraphicsArea(QWidget):
    def __init__(self):
        super().__init__()
        self.shapes = []
        self.zoom = 1.0
        self.pan_x = 0
        self.pan_y = 0
    
    def wheelEvent(self, event):
        if event.angleDelta().y() > 0:
            self.zoom = self.zoom * 1.1
        else:
            self.zoom = self.zoom / 1.1
        self.update()
    
    def add_rectangle(self, x, y, w, h):
        rect = Rectangle(x, y, w, h)
        shapes.append(rect)
        update()
    
    def paintEvent(self, event):
        painter = QPainter(self)
        for shape in self.shapes:
            shape.draw(painter, zoom, pan_x, pan_y)
        # painter.end() vergessen?
```

**Wie viele Fehler finden Sie? Korrigieren Sie diese.**

---

## Musterlösungen

<details> <summary>Lösungen anzeigen</summary>

### Aufgabe 1a:

- Linke obere Ecke: `(150, 75)`
- Rechte untere Ecke: `(330, 210)`
- Rechnung: `(80 + 20) * 1.5 = 150`, `(60 + (-10)) * 1.5 = 75`

### Aufgabe 1b:

- Welt-Koordinate: `(75, 42.5)`
- Rechnung: `(180 / 2.0) - 15 = 75`, `(135 / 2.0) - 25 = 42.5`

### Aufgabe 6 - Fehler:

1. `shapes.append(rect)` → `self.shapes.append(rect)`
2. `update()` → `self.update()`
3. `shape.draw(painter, zoom, pan_x, pan_y)` → `shape.draw(painter, self.zoom, self.pan_x, self.pan_y)`
4. `painter.end()` fehlt
5. Zoom-Begrenzung fehlt

</details>

**Zeitvorgabe: 90 Minuten** **Hilfsmittel: Keine**

Wie würdest du bei diesen Aufgaben vorgehen? Welche siehst du als schwierigste?