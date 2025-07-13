## Pixelgrafik vs. Vektorgrafik

|Aspekt|Pixelgrafik|Vektorgrafik|
|---|---|---|
|**Speicherung**|Feste Farbwerte pro Pixel|Geometrische Beschreibung (Punkte, Kurven)|
|**Zeichnen**|Direkt auf Pixel-Buffer|Berechnung zur Renderzeit|
|**Zoom**|Pixelig, verlustbehaftet|Beliebig skalierbar, verlustfrei|
|**Dateigröße**|Abhängig von Auflösung|Abhängig von Objektanzahl|
|**Bearbeitung**|Pixel-basiert (Photoshop)|Objekt-basiert (Illustrator)|
|**Performance**|Konstant beim Rendern|Abhängig von Objektkomplexität|
|**Anwendung**|Fotos, realistische Bilder|Logos, Icons, technische Zeichnungen|

## Koordinaten-Transformationen ⭐

### Grundformel (Welt → Bildschirm):

```
bildschirm_x = (welt_x + pan_offset_x) * zoom_faktor
bildschirm_y = (welt_y + pan_offset_y) * zoom_faktor
```

**Reihenfolge:** Erst Pan (verschieben), dann Zoom (skalieren)

### Umkehrung (Bildschirm → Welt):

```
welt_x = (bildschirm_x / zoom_faktor) - pan_offset_x
welt_y = (bildschirm_y / zoom_faktor) - pan_offset_y
```

### Zoom um Mausposition:

```python
# Vor Zoom: Weltkoordinate unter Maus berechnen
welt_x_vor = (maus_x / zoom_alt) - pan_x
welt_y_vor = (maus_y / zoom_alt) - pan_y

# Zoom anwenden
zoom_neu = zoom_alt * zoom_faktor

# Nach Zoom: Pan korrigieren damit Mausposition gleich bleibt
welt_x_nach = (maus_x / zoom_neu) - pan_x
pan_x += welt_x_nach - welt_x_vor
```

## Stern-Mathematik (Polarkoordinaten) ⭐

### 5-zackiger Stern = 10 Punkte:

- **Äußere Punkte** (Index 0, 2, 4, 6, 8): voller Radius
- **Innere Punkte** (Index 1, 3, 5, 7, 9): reduzierter Radius (z.B. 40%)

### Formel:

```python
anzahl_punkte = sterne_zacken * 2  # z.B. 5 * 2 = 10
for i in range(anzahl_punkte):
    winkel = i * (2 * π / anzahl_punkte) - π/2  # -π/2 = Start oben
    
    if i % 2 == 0:
        radius = äußerer_radius
    else:
        radius = innerer_radius * 0.4  # 40% vom äußeren
    
    x = mittelpunkt_x + radius * cos(winkel)
    y = mittelpunkt_y + radius * sin(winkel)
```

### Polarkoordinaten Grundlagen:

```python
# Kartesisch → Polar
radius = sqrt(x² + y²)
winkel = atan2(y, x)

# Polar → Kartesisch  
x = radius * cos(winkel)
y = radius * sin(winkel)
```

## GUI-Architektur & Design Patterns

### Widget-Hierarchie:

```
QMainWindow
├── QFrame (central widget)
│   └── VectorGraphicsArea (custom widget)
├── QMenuBar
│   ├── Ansicht (Zoom, Pan)
│   ├── Objekte (Primitive hinzufügen)
│   └── Datei (Beenden)
└── QToolBar (Schnellzugriff)
```

### MVC-Pattern in Vektorgrafik:

- **Model**: Liste der VectorShape-Objekte
- **View**: VectorGraphicsArea (paintEvent)
- **Controller**: Event-Handler (Mouse, Wheel, Actions)

### Observer-Pattern:

```python
# Jede Änderung am Model triggert View-Update
def add_shape(self, shape):
    self.shapes.append(shape)
    self.update()  # Löst paintEvent aus
```

## Event-Handling für Vektorgrafik

### Mouse-Events:

```python
def mousePressEvent(self, event):
    if event.button() == Qt.MouseButton.RightButton:
        self.start_pan(event.position().toPoint())
    elif event.button() == Qt.MouseButton.LeftButton:
        self.select_object(event.position().toPoint())

def mouseMoveEvent(self, event):
    if self.panning:
        self.update_pan(event.position().toPoint())

def mouseReleaseEvent(self, event):
    if event.button() == Qt.MouseButton.RightButton:
        self.end_pan()
```

### Wheel-Event (Zoom):

```python
def wheelEvent(self, event):
    zoom_delta = 1.1 if event.angleDelta().y() > 0 else 1/1.1
    self.zoom_factor *= zoom_delta
    self.zoom_factor = max(0.1, min(10.0, self.zoom_factor))
    self.update()
```

### Paint-Event (Rendering):

```python
def paintEvent(self, event):
    painter = QPainter(self)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)
    
    for shape in self.shapes:
        shape.draw(painter, self.zoom_factor, self.offset_x, self.offset_y)
    
    painter.end()
```

## Objektorientierte Datenstrukturen

### Basisklasse (Polymorphie):

```python
class VectorShape:
    def __init__(self, x, y, width, height):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.line_color = QColor(0, 0, 0)
        self.fill_color = QColor(200, 200, 200, 100)
        self.line_width = 2
    
    def draw(self, painter, zoom, offset_x, offset_y):
        # Abstrakte Methode - in Unterklassen implementiert
        pass
    
    def get_bounds(self):
        return QRect(self.x, self.y, self.width, self.height)
```

### Konkrete Implementierungen:

```python
class Rectangle(VectorShape):
    def draw(self, painter, zoom, offset_x, offset_y):
        x = (self.x + offset_x) * zoom
        y = (self.y + offset_y) * zoom
        w = self.width * zoom
        h = self.height * zoom
        
        painter.setPen(QPen(self.line_color, self.line_width))
        painter.setBrush(QBrush(self.fill_color))
        painter.drawRect(int(x), int(y), int(w), int(h))

class Circle(VectorShape):
    def draw(self, painter, zoom, offset_x, offset_y):
        # Ähnlich wie Rectangle, aber drawEllipse()
        pass

class Star(VectorShape):
    def __init__(self, x, y, width, height, points=5):
        super().__init__(x, y, width, height)
        self.points = points
    
    def draw(self, painter, zoom, offset_x, offset_y):
        # Stern-Mathematik + drawPolygon()
        pass
```

## Qt-Framework Essentials

### QPainter-Konfiguration:

```python
painter = QPainter(self)
painter.setRenderHint(QPainter.RenderHint.Antialiasing)  # Glättung
painter.setPen(QPen(color, width, Qt.PenStyle.SolidLine))
painter.setBrush(QBrush(fill_color))
```

### Geometrie-Primitive:

- **Rechteck**: `painter.drawRect(x, y, width, height)`
- **Ellipse/Kreis**: `painter.drawEllipse(x, y, width, height)`
- **Polygon**: `painter.drawPolygon(QPolygon(punkt_liste))`
- **Linie**: `painter.drawLine(start_point, end_point)`

### Dialog-Erstellung:

```python
def create_input_dialog(self):
    dialog = QDialog(self)
    layout = QGridLayout(dialog)
    
    # Eingabefelder
    spinbox = QSpinBox()
    spinbox.setRange(min_val, max_val)
    layout.addWidget(QLabel("Label:"), row, 0)
    layout.addWidget(spinbox, row, 1)
    
    # Buttons
    ok_button = QPushButton("OK")
    ok_button.clicked.connect(dialog.accept)
    
    result = dialog.exec()  # Modal dialog
    if result == QDialog.DialogCode.Accepted:
        return spinbox.value()
```

## Erweiterbarkeitsprinzipien

### Für Blatt 04 (OOP):

- **Abstrakte Basisklassen** mit abstrakten Methoden
- **Interface Segregation**: Separate Interfaces für Drawing, Picking, Transformation
- **Strategy Pattern**: Austauschbare Algorithmen (verschiedene Stern-Varianten)

### Für Blatt 05 (Funktional):

- **Immutable Shapes**: Transformation erzeugt neue Objekte
- **Pure Functions**: `transform(shape, operation) → new_shape`
- **Higher-Order Functions**: `map(transform_function, shapes)`

### Zukunftige Features:

```python
# Picking (Objektauswahl)
def pick_shape(self, point):
    for shape in reversed(self.shapes):  # Rückwärts = Vordergrund zuerst
        if shape.contains_point(point):
            return shape

# Transformation
def transform_shape(self, shape, matrix):
    # Affine Transformationen: Translation, Rotation, Skalierung
    pass

# Serialisierung
def export_to_svg(self, shapes):
    # SVG-XML generieren
    pass
```

## Mathematische Konzepte (Klausurrelevant)

### Affine Transformationen:

```
[x']   [sx  0   tx] [x]
[y'] = [0   sy  ty] [y]
[1 ]   [0   0   1 ] [1]

sx, sy = Skalierung
tx, ty = Translation
```

### Bounding Box Berechnung:

```python
def get_bounds(self):
    min_x = min(point.x for point in self.points)
    max_x = max(point.x for point in self.points)
    min_y = min(point.y for point in self.points)
    max_y = max(point.y for point in self.points)
    return QRect(min_x, min_y, max_x - min_x, max_y - min_y)
```

### Collision Detection (Punkt in Polygon):

```python
def point_in_polygon(point, polygon):
    # Ray-Casting Algorithmus
    # Anzahl Schnittpunkte mit Polygon-Kanten zählen
    pass
```

---

## Klausur-Fokus ⭐

### Must-Know Formeln:

1. **Koordinaten-Transformation**: `(welt + pan) * zoom`
2. **Polarkoordinaten**: `x = r*cos(θ), y = r*sin(θ)`
3. **Stern-Punkte**: `2*n Punkte, alternierend inner/outer radius`

### Wichtige Qt-Patterns:

1. **Custom Widget**: Erben von QWidget, paintEvent überschreiben
2. **Event-Handling**: Mouse/Wheel Events für Interaktion
3. **Dialog Creation**: Modal dialogs mit QSpinBox, QPushButton
4. **Action-System**: QAction für Menü/Toolbar mit Shortcuts

### Code-Patterns:

1. **Polymorphe Shape-Hierarchie** mit draw()-Methode
2. **Event-driven Updates** (self.update() nach Änderungen)
3. **Separation of Concerns** (Model/View/Controller)

**Tipische Klausuraufgaben:** Koordinaten umrechnen, Stern-Punkte berechnen, Event-Handler implementieren, Qt-Widget-Hierarchie zeichnen

