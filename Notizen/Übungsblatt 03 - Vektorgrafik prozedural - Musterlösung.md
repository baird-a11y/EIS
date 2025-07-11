# Übungsblatt 03 - Vektorgrafik prozedural - Musterlösung
**Einführung in die Softwareentwicklung (EiS) - SoSem 2025**

> [!important] **Klausurrelevanz**:
> - **Prozedurale Programmierung**: Strukturierung ohne Klassen
> - **Viewport-Transformation**: Welt- zu Pixelkoordinaten
> - **2D-Grafik**: QPainter, Geometric Primitives
> - **Modularisierung**: Funktionen als Bausteine
> - **Datenstrukturen**: Listen, Dictionaries für Szenen

> [!note] **Lernziele**:
> - Komplexere Software prozedural strukturieren
> - Grafik-Programmierung mit QPainter
> - Koordinatentransformationen verstehen
> - Grundlage für spätere OOP-Refaktorierung

---

## Aufgabe 0: Design (unbewertet)

> [!tip] **Architektur-Überlegungen**:
> - **Modularität**: Trennung von Datenstrukturen und Funktionen
> - **Erweiterbarkeit**: Einfach neue Primitive hinzufügen
> - **Testbarkeit**: Jede Funktion einzeln prüfbar
> - **Einfachheit**: Bodenständige Lösung vor Eleganz

### Geplante Struktur:
```python
# Datenstrukturen
Scene = List[Shape]
Shape = Dict[str, Any]  # {"type": "circle", "x": 100, "y": 50, ...}

# Funktionen
def create_rectangle(x, y, width, height, color) -> Shape
def create_circle(x, y, radius, color) -> Shape
def create_star(x, y, radius, points, color) -> Shape
def render_scene(scene: Scene, painter: QPainter, viewport: Viewport)
```

---

## Aufgabe 1: Rahmenprogramm (10 Punkte)

### Python + PySide6 Lösung:

```python
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, 
                               QVBoxLayout, QHBoxLayout, QPushButton, 
                               QMenuBar, QMenu)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QColor, QPen, QBrush
import sys
from typing import List, Dict, Any, Tuple
import math

class DrawingWidget(QWidget):
    """Custom Widget für das Zeichnen der Vektorgrafik"""
    
    def __init__(self):
        super().__init__()
        self.scene: List[Dict[str, Any]] = []
        self.viewport = {
            'world_left': -2.0,
            'world_top': 2.0,
            'world_right': 2.0,
            'world_bottom': -2.0
        }
        self.setMinimumSize(800, 600)
        
    def set_scene(self, scene: List[Dict[str, Any]]):
        """Setzt die zu zeichnende Szene"""
        self.scene = scene
        self.update()  # Löst paintEvent aus
        
    def paintEvent(self, event):
        """Wird automatisch aufgerufen wenn Widget neu gezeichnet werden muss"""
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor(255, 255, 255))  # Weißer Hintergrund
        
        if self.scene:
            render_scene(self.scene, painter, self.viewport, self.size())
        
        painter.end()

class VectorGraphicsMainWindow(QMainWindow):
    """Hauptfenster der Vektorgrafik-Anwendung"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EiS - Vektorgrafik Prozedural")
        self.setGeometry(100, 100, 1000, 700)
        
        # Central Widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout
        layout = QVBoxLayout(central_widget)
        
        # Toolbar
        toolbar_layout = QHBoxLayout()
        
        self.btn_test_scene1 = QPushButton("Test Scene 1")
        self.btn_test_scene1.clicked.connect(self.create_test_scene1)
        toolbar_layout.addWidget(self.btn_test_scene1)
        
        self.btn_test_scene2 = QPushButton("Test Scene 2")
        self.btn_test_scene2.clicked.connect(self.create_test_scene2)
        toolbar_layout.addWidget(self.btn_test_scene2)
        
        self.btn_clear = QPushButton("Clear Scene")
        self.btn_clear.clicked.connect(self.clear_scene)
        toolbar_layout.addWidget(self.btn_clear)
        
        toolbar_layout.addStretch()  # Platz auffüllen
        
        layout.addLayout(toolbar_layout)
        
        # Drawing Area
        self.drawing_widget = DrawingWidget()
        layout.addWidget(self.drawing_widget)
        
        # Menu Bar
        self.create_menu_bar()
        
    def create_menu_bar(self):
        """Erstellt die Menüleiste"""
        menubar = self.menuBar()
        
        # File Menu
        file_menu = menubar.addMenu('File')
        
        exit_action = file_menu.addAction('Exit')
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(self.close)
        
        # Scene Menu
        scene_menu = menubar.addMenu('Scene')
        
        scene1_action = scene_menu.addAction('Test Scene 1')
        scene1_action.triggered.connect(self.create_test_scene1)
        
        scene2_action = scene_menu.addAction('Test Scene 2')
        scene2_action.triggered.connect(self.create_test_scene2)
        
        clear_action = scene_menu.addAction('Clear Scene')
        clear_action.triggered.connect(self.clear_scene)
        
    def create_test_scene1(self):
        """Erstellt erste Testszene"""
        scene = create_test_scene_1()
        self.drawing_widget.set_scene(scene)
        
    def create_test_scene2(self):
        """Erstellt zweite Testszene"""
        scene = create_test_scene_2()
        self.drawing_widget.set_scene(scene)
        
    def clear_scene(self):
        """Leert die Szene"""
        self.drawing_widget.set_scene([])

# Datenstrukturen und Primitive
def create_rectangle(x: float, y: float, width: float, height: float, 
                    fill_color: QColor = QColor(100, 100, 255), 
                    border_color: QColor = QColor(0, 0, 0),
                    border_width: float = 1.0) -> Dict[str, Any]:
    """Erstellt ein Rechteck-Primitive"""
    return {
        'type': 'rectangle',
        'x': x,
        'y': y,
        'width': width,
        'height': height,
        'fill_color': fill_color,
        'border_color': border_color,
        'border_width': border_width
    }

def create_circle(x: float, y: float, radius: float,
                 fill_color: QColor = QColor(255, 100, 100),
                 border_color: QColor = QColor(0, 0, 0),
                 border_width: float = 1.0) -> Dict[str, Any]:
    """Erstellt ein Kreis-Primitive"""
    return {
        'type': 'circle',
        'x': x,
        'y': y,
        'radius': radius,
        'fill_color': fill_color,
        'border_color': border_color,
        'border_width': border_width
    }

def create_star(x: float, y: float, outer_radius: float, inner_radius: float,
               points: int = 5,
               fill_color: QColor = QColor(255, 255, 100),
               border_color: QColor = QColor(0, 0, 0),
               border_width: float = 1.0) -> Dict[str, Any]:
    """Erstellt ein Stern-Primitive"""
    return {
        'type': 'star',
        'x': x,
        'y': y,
        'outer_radius': outer_radius,
        'inner_radius': inner_radius,
        'points': points,
        'fill_color': fill_color,
        'border_color': border_color,
        'border_width': border_width
    }

# Viewport-Transformation
def world_to_pixel(world_x: float, world_y: float, 
                  viewport: Dict[str, float], 
                  pixel_size: Tuple[int, int]) -> Tuple[int, int]:
    """Konvertiert Weltkoordinaten zu Pixelkoordinaten"""
    pixel_width, pixel_height = pixel_size
    
    # Weltkoordinaten-Bereich
    world_width = viewport['world_right'] - viewport['world_left']
    world_height = viewport['world_top'] - viewport['world_bottom']
    
    # Normalisieren (0 bis 1)
    norm_x = (world_x - viewport['world_left']) / world_width
    norm_y = (world_y - viewport['world_bottom']) / world_height
    
    # Zu Pixelkoordinaten (y-Achse umkehren!)
    pixel_x = int(norm_x * pixel_width)
    pixel_y = int((1.0 - norm_y) * pixel_height)  # Y-Achse umkehren
    
    return pixel_x, pixel_y

def world_to_pixel_size(world_size: float, 
                       viewport: Dict[str, float], 
                       pixel_size: Tuple[int, int],
                       dimension: str = 'width') -> int:
    """Konvertiert Weltgrößen zu Pixelgrößen"""
    pixel_width, pixel_height = pixel_size
    
    if dimension == 'width':
        world_width = viewport['world_right'] - viewport['world_left']
        return int(world_size * pixel_width / world_width)
    else:  # height
        world_height = viewport['world_top'] - viewport['world_bottom']
        return int(world_size * pixel_height / world_height)

# Rendering-Funktionen
def render_scene(scene: List[Dict[str, Any]], 
                painter: QPainter, 
                viewport: Dict[str, float],
                pixel_size) -> None:
    """Rendert eine komplette Szene"""
    size_tuple = (pixel_size.width(), pixel_size.height())
    
    for shape in scene:
        if shape['type'] == 'rectangle':
            draw_rectangle(shape, painter, viewport, size_tuple)
        elif shape['type'] == 'circle':
            draw_circle(shape, painter, viewport, size_tuple)
        elif shape['type'] == 'star':
            draw_star(shape, painter, viewport, size_tuple)
        else:
            print(f"Unknown shape type: {shape['type']}")

def draw_rectangle(rect: Dict[str, Any], 
                  painter: QPainter, 
                  viewport: Dict[str, float],
                  pixel_size: Tuple[int, int]) -> None:
    """Zeichnet ein Rechteck"""
    # Koordinaten transformieren
    pixel_x, pixel_y = world_to_pixel(rect['x'], rect['y'], viewport, pixel_size)
    pixel_width = world_to_pixel_size(rect['width'], viewport, pixel_size, 'width')
    pixel_height = world_to_pixel_size(rect['height'], viewport, pixel_size, 'height')
    
    # Zeichnen
    painter.setBrush(QBrush(rect['fill_color']))
    painter.setPen(QPen(rect['border_color'], rect['border_width']))
    painter.drawRect(pixel_x, pixel_y, pixel_width, pixel_height)

def draw_circle(circle: Dict[str, Any], 
               painter: QPainter, 
               viewport: Dict[str, float],
               pixel_size: Tuple[int, int]) -> None:
    """Zeichnet einen Kreis"""
    # Koordinaten transformieren
    pixel_x, pixel_y = world_to_pixel(circle['x'], circle['y'], viewport, pixel_size)
    pixel_radius = world_to_pixel_size(circle['radius'], viewport, pixel_size, 'width')
    
    # Zeichnen (drawEllipse erwartet top-left corner)
    painter.setBrush(QBrush(circle['fill_color']))
    painter.setPen(QPen(circle['border_color'], circle['border_width']))
    painter.drawEllipse(pixel_x - pixel_radius, pixel_y - pixel_radius, 
                       2 * pixel_radius, 2 * pixel_radius)

def draw_star(star: Dict[str, Any], 
             painter: QPainter, 
             viewport: Dict[str, float],
             pixel_size: Tuple[int, int]) -> None:
    """Zeichnet einen Stern"""
    from PySide6.QtGui import QPolygonF, QPointF
    
    # Stern-Punkte berechnen
    points = []
    num_points = star['points']
    
    for i in range(num_points * 2):
        angle = i * math.pi / num_points
        radius = star['outer_radius'] if i % 2 == 0 else star['inner_radius']
        
        world_x = star['x'] + radius * math.cos(angle)
        world_y = star['y'] + radius * math.sin(angle)
        
        pixel_x, pixel_y = world_to_pixel(world_x, world_y, viewport, pixel_size)
        points.append(QPointF(pixel_x, pixel_y))
    
    # Polygon erstellen und zeichnen
    polygon = QPolygonF(points)
    painter.setBrush(QBrush(star['fill_color']))
    painter.setPen(QPen(star['border_color'], star['border_width']))
    painter.drawPolygon(polygon)

# Testszenen
def create_test_scene_1() -> List[Dict[str, Any]]:
    """Erstellt erste Testszene"""
    return [
        create_rectangle(-1.5, 0.5, 1.0, 1.0, QColor(255, 100, 100)),
        create_circle(0.5, 0.5, 0.4, QColor(100, 255, 100)),
        create_star(0, -0.8, 0.6, 0.3, 5, QColor(255, 255, 100))
    ]

def create_test_scene_2() -> List[Dict[str, Any]]:
    """Erstellt zweite Testszene"""
    return [
        create_rectangle(-1.0, 1.0, 2.0, 0.5, QColor(100, 100, 255)),
        create_circle(-0.5, 0, 0.3, QColor(255, 150, 0)),
        create_circle(0.5, 0, 0.3, QColor(255, 0, 255)),
        create_star(0, -1.2, 0.4, 0.2, 6, QColor(0, 255, 255))
    ]

# Hauptprogramm
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VectorGraphicsMainWindow()
    window.show()
    app.exec_()
```

---

## Aufgabe 2: Vektorgrafik-Primitive (30 Punkte)

### Teil a) Datenstrukturen (10 Punkte)

> [!note] **Lernziel**: Prozeduraler Ansatz mit Datenstrukturen

```python
# Typdefinitionen
from typing import List, Dict, Any, Tuple
from dataclasses import dataclass

# Alternative: Dataclass-Ansatz (eleganter)
@dataclass
class Rectangle:
    x: float
    y: float
    width: float
    height: float
    fill_color: QColor
    border_color: QColor
    border_width: float

@dataclass
class Circle:
    x: float
    y: float
    radius: float
    fill_color: QColor
    border_color: QColor
    border_width: float

@dataclass
class Star:
    x: float
    y: float
    outer_radius: float
    inner_radius: float
    points: int
    fill_color: QColor
    border_color: QColor
    border_width: float

# Szene als Liste
Scene = List[Any]  # Rectangle | Circle | Star
```

### Teil b) Rendering-System (20 Punkte)

> [!important] **Viewport-Transformation verstehen**:
> ```
> Weltkoordinaten → Pixelkoordinaten
> 
> 1. Normalisierung: (world_x - world_left) / world_width
> 2. Skalierung: norm_x * pixel_width  
> 3. Y-Achse umkehren: pixel_height - pixel_y
> ```

**Siehe vollständige Implementierung oben** ✅

---

## Aufgabe 3: Interaktion - Zoom und Pan (20 Punkte)

### Erweiterte DrawingWidget-Klasse:

```python
class InteractiveDrawingWidget(DrawingWidget):
    """Erweiterte Zeichenfläche mit Zoom und Pan"""
    
    def __init__(self):
        super().__init__()
        self.zoom_factor = 1.0
        self.pan_x = 0.0
        self.pan_y = 0.0
        
    def zoom_in(self):
        """Vergrößert die Ansicht"""
        self.zoom_factor *= 1.2
        self.update_viewport()
        
    def zoom_out(self):
        """Verkleinert die Ansicht"""
        self.zoom_factor /= 1.2
        self.update_viewport()
        
    def pan_left(self):
        """Verschiebt Ansicht nach links"""
        self.pan_x -= 0.2 / self.zoom_factor
        self.update_viewport()
        
    def pan_right(self):
        """Verschiebt Ansicht nach rechts"""
        self.pan_x += 0.2 / self.zoom_factor
        self.update_viewport()
        
    def pan_up(self):
        """Verschiebt Ansicht nach oben"""
        self.pan_y += 0.2 / self.zoom_factor
        self.update_viewport()
        
    def pan_down(self):
        """Verschiebt Ansicht nach unten"""
        self.pan_y -= 0.2 / self.zoom_factor
        self.update_viewport()
        
    def update_viewport(self):
        """Aktualisiert Viewport basierend auf Zoom und Pan"""
        base_width = 4.0 / self.zoom_factor
        base_height = 4.0 / self.zoom_factor
        
        self.viewport = {
            'world_left': -base_width/2 + self.pan_x,
            'world_right': base_width/2 + self.pan_x,
            'world_top': base_height/2 + self.pan_y,
            'world_bottom': -base_height/2 + self.pan_y
        }
        self.update()

# Erweiterte Toolbar
def create_extended_toolbar(self):
    """Erweiterte Toolbar mit Zoom/Pan-Controls"""
    toolbar_layout = QHBoxLayout()
    
    # Zoom Controls
    zoom_in_btn = QPushButton("Zoom In")
    zoom_in_btn.clicked.connect(self.drawing_widget.zoom_in)
    toolbar_layout.addWidget(zoom_in_btn)
    
    zoom_out_btn = QPushButton("Zoom Out")
    zoom_out_btn.clicked.connect(self.drawing_widget.zoom_out)
    toolbar_layout.addWidget(zoom_out_btn)
    
    toolbar_layout.addSeparator()
    
    # Pan Controls
    pan_left_btn = QPushButton("← Left")
    pan_left_btn.clicked.connect(self.drawing_widget.pan_left)
    toolbar_layout.addWidget(pan_left_btn)
    
    pan_right_btn = QPushButton("Right →")
    pan_right_btn.clicked.connect(self.drawing_widget.pan_right)
    toolbar_layout.addWidget(pan_right_btn)
    
    pan_up_btn = QPushButton("↑ Up")
    pan_up_btn.clicked.connect(self.drawing_widget.pan_up)
    toolbar_layout.addWidget(pan_up_btn)
    
    pan_down_btn = QPushButton("↓ Down")
    pan_down_btn.clicked.connect(self.drawing_widget.pan_down)
    toolbar_layout.addWidget(pan_down_btn)
    
    return toolbar_layout
```

---

## Aufgabe 4: Objekterstellung (20 Punkte)

### Einfache Variante (10 Punkte) - Dialog-basiert:

```python
from PySide6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, 
                               QLabel, QDoubleSpinBox, QPushButton,
                               QComboBox, QColorDialog)

class CreateShapeDialog(QDialog):
    """Dialog zum Erstellen neuer Primitive"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Create New Shape")
        self.setModal(True)
        
        layout = QVBoxLayout(self)
        
        # Shape Type
        layout.addWidget(QLabel("Shape Type:"))
        self.shape_type = QComboBox()
        self.shape_type.addItems(["Rectangle", "Circle", "Star"])
        layout.addWidget(self.shape_type)
        
        # Position
        pos_layout = QHBoxLayout()
        pos_layout.addWidget(QLabel("X:"))
        self.x_spin = QDoubleSpinBox()
        self.x_spin.setRange(-10.0, 10.0)
        self.x_spin.setValue(0.0)
        pos_layout.addWidget(self.x_spin)
        
        pos_layout.addWidget(QLabel("Y:"))
        self.y_spin = QDoubleSpinBox()
        self.y_spin.setRange(-10.0, 10.0)
        self.y_spin.setValue(0.0)
        pos_layout.addWidget(self.y_spin)
        
        layout.addLayout(pos_layout)
        
        # Size
        size_layout = QHBoxLayout()
        size_layout.addWidget(QLabel("Width/Radius:"))
        self.size1_spin = QDoubleSpinBox()
        self.size1_spin.setRange(0.1, 10.0)
        self.size1_spin.setValue(1.0)
        size_layout.addWidget(self.size1_spin)
        
        size_layout.addWidget(QLabel("Height/Inner Radius:"))
        self.size2_spin = QDoubleSpinBox()
        self.size2_spin.setRange(0.1, 10.0)
        self.size2_spin.setValue(1.0)
        size_layout.addWidget(self.size2_spin)
        
        layout.addLayout(size_layout)
        
        # Colors
        color_layout = QHBoxLayout()
        
        self.fill_color = QColor(100, 100, 255)
        self.fill_color_btn = QPushButton("Fill Color")
        self.fill_color_btn.clicked.connect(self.choose_fill_color)
        color_layout.addWidget(self.fill_color_btn)
        
        self.border_color = QColor(0, 0, 0)
        self.border_color_btn = QPushButton("Border Color")
        self.border_color_btn.clicked.connect(self.choose_border_color)
        color_layout.addWidget(self.border_color_btn)
        
        layout.addLayout(color_layout)
        
        # Buttons
        button_layout = QHBoxLayout()
        
        create_btn = QPushButton("Create")
        create_btn.clicked.connect(self.accept)
        button_layout.addWidget(create_btn)
        
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.reject)
        button_layout.addWidget(cancel_btn)
        
        layout.addLayout(button_layout)
        
    def choose_fill_color(self):
        color = QColorDialog.getColor(self.fill_color, self)
        if color.isValid():
            self.fill_color = color
            
    def choose_border_color(self):
        color = QColorDialog.getColor(self.border_color, self)
        if color.isValid():
            self.border_color = color
            
    def get_shape(self) -> Dict[str, Any]:
        """Erstellt Shape basierend auf Dialog-Eingaben"""
        shape_type = self.shape_type.currentText().lower()
        
        if shape_type == "rectangle":
            return create_rectangle(
                self.x_spin.value(), self.y_spin.value(),
                self.size1_spin.value(), self.size2_spin.value(),
                self.fill_color, self.border_color
            )
        elif shape_type == "circle":
            return create_circle(
                self.x_spin.value(), self.y_spin.value(),
                self.size1_spin.value(),
                self.fill_color, self.border_color
            )
        elif shape_type == "star":
            return create_star(
                self.x_spin.value(), self.y_spin.value(),
                self.size1_spin.value(), self.size2_spin.value(),
                5, self.fill_color, self.border_color
            )

# Integration in Hauptfenster
def add_shape_dialog(self):
    """Zeigt Dialog zum Hinzufügen neuer Shapes"""
    dialog = CreateShapeDialog(self)
    if dialog.exec_() == QDialog.Accepted:
        new_shape = dialog.get_shape()
        current_scene = self.drawing_widget.scene.copy()
        current_scene.append(new_shape)
        self.drawing_widget.set_scene(current_scene)
```

### Schwierige Variante (20 Punkte) - Mouse-basiert:

```python
class MouseDrawingWidget(InteractiveDrawingWidget):
    """Zeichnen mit Mausinteraktion"""
    
    def __init__(self):
        super().__init__()
        self.drawing_mode = None  # 'rectangle', 'circle', 'star'
        self.start_point = None
        self.current_point = None
        self.preview_shape = None
        
    def set_drawing_mode(self, mode: str):
        """Setzt den Zeichenmodus"""
        self.drawing_mode = mode
        self.setCursor(Qt.CrossCursor)
        
    def mousePressEvent(self, event):
        """Startet das Zeichnen"""
        if self.drawing_mode and event.button() == Qt.LeftButton:
            # Pixelkoordinaten zu Weltkoordinaten
            pixel_pos = (event.pos().x(), event.pos().y())
            self.start_point = self.pixel_to_world(pixel_pos)
            self.current_point = self.start_point
            
    def mouseMoveEvent(self, event):
        """Aktualisiert Vorschau während des Zeichnens"""
        if self.drawing_mode and self.start_point:
            pixel_pos = (event.pos().x(), event.pos().y())
            self.current_point = self.pixel_to_world(pixel_pos)
            self.update_preview()
            
    def mouseReleaseEvent(self, event):
        """Beendet das Zeichnen"""
        if self.drawing_mode and self.start_point and event.button() == Qt.LeftButton:
            self.create_shape_from_mouse()
            self.start_point = None
            self.current_point = None
            self.preview_shape = None
            self.update()
            
    def pixel_to_world(self, pixel_pos: Tuple[int, int]) -> Tuple[float, float]:
        """Konvertiert Pixel- zu Weltkoordinaten"""
        pixel_x, pixel_y = pixel_pos
        pixel_width = self.width()
        pixel_height = self.height()
        
        # Normalisierung (Y-Achse umkehren)
        norm_x = pixel_x / pixel_width
        norm_y = 1.0 - (pixel_y / pixel_height)
        
        # Weltkoordinaten
        world_width = self.viewport['world_right'] - self.viewport['world_left']
        world_height = self.viewport['world_top'] - self.viewport['world_bottom']
        
        world_x = self.viewport['world_left'] + norm_x * world_width
        world_y = self.viewport['world_bottom'] + norm_y * world_height
        
        return world_x, world_y
        
    def create_shape_from_mouse(self):
        """Erstellt Shape basierend auf Mausinteraktion"""
        if not self.start_point or not self.current_point:
            return
            
        x1, y1 = self.start_point
        x2, y2 = self.current_point
        
        # Bounding Box berechnen
        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2
        width = abs(x2 - x1)
        height = abs(y2 - y1)
        
        # Shape erstellen
        new_shape = None
        if self.drawing_mode == 'rectangle':
            new_shape = create_rectangle(
                min(x1, x2), min(y1, y2), width, height,
                QColor(100, 150, 255), QColor(0, 0, 0)
            )
        elif self.drawing_mode == 'circle':
            radius = max(width, height) / 2
            new_shape = create_circle(
                center_x, center_y, radius,
                QColor(255, 150, 100), QColor(0, 0, 0)
            )
        elif self.drawing_mode == 'star':
            outer_radius = max(width, height) / 2
            inner_radius = outer_radius * 0.5
            new_shape = create_star(
                center_x, center_y, outer_radius, inner_radius, 5,
                QColor(255, 255, 100), QColor(0, 0, 0)
            )
            
        if new_shape:
            current_scene = self.scene.copy()
            current_scene.append(new_shape)
            self.set_scene(current_scene)
            
    def update_preview(self):
        """Aktualisiert die Zeichnungsvorschau"""
        if self.start_point and self.current_point:
            self.update()
            
    def paintEvent(self, event):
        """Erweiterte paintEvent mit Vorschau"""
        super().paintEvent(event)
        
        # Vorschau zeichnen
        if self.drawing_mode and self.start_point and self.current_point:
            painter = QPainter(self)
            painter.setPen(QPen(QColor(200, 200, 200), 2, Qt.DashLine))
            painter.setBrush(QBrush())  # Transparent
            
            size_tuple = (self.width(), self.height())
            x1, y1 = self.start_point
            x2, y2 = self.current_point
            
            if self.drawing_mode == 'rectangle':
                px1, py1 = world_to_pixel(x1, y1, self.viewport, size_tuple)
                px2, py2 = world_to_pixel(x2, y2, self.viewport, size_tuple)
                painter.drawRect(min(px1, px2), min(py1, py2), 
                               abs(px2 - px1), abs(py2 - py1))
            elif self.drawing_mode == 'circle':
                center_x, center_y = (x1 + x2) / 2, (y1 + y2) / 2
                radius = max(abs(x2 - x1), abs(y2 - y1)) / 2
                pcx, pcy = world_to_pixel(center_x, center_y, self.viewport, size_tuple)
                pradius = world_to_pixel_size(radius, self.viewport, size_tuple, 'width')
                painter.drawEllipse(pcx - pradius, pcy - pradius, 
                                  2 * pradius, 2 * pradius)
            
            painter.end()

# Erweiterte Toolbar für Zeichenmodi
def create_drawing_toolbar(self):
    """Toolbar mit Zeichenmodi"""
    toolbar_layout = QHBoxLayout()
    
    # Drawing Mode Buttons
    rect_btn = QPushButton("Rectangle")
    rect_btn.setCheckable(True)
    rect_btn.clicked.connect(lambda: self.set_drawing_mode('rectangle'))
    toolbar_layout.addWidget(rect_btn)
    
    circle_btn = QPushButton("Circle")
    circle_btn.setCheckable(True)
    circle_btn.clicked.connect(lambda: self.set_drawing_mode('circle'))
    toolbar_layout.addWidget(circle_btn)
    
    star_btn = QPushButton("Star")
    star_btn.setCheckable(True)
    star_btn.clicked.connect(lambda: self.set_drawing_mode('star'))
    toolbar_layout.addWidget(star_btn)
    
    # Selection Mode
    select_btn = QPushButton("Select")
    select_btn.setCheckable(True)
    select_btn.clicked.connect(lambda: self.set_drawing_mode(None))
    toolbar_layout.addWidget(select_btn)
    
    return toolbar_layout
```

---

## Prüfungsrelevante Konzepte verstehen

### 1. Prozedurale vs. Objektorientierte Programmierung

> [!important] **Klausurfrage**: Wann ist prozedurale Programmierung vorteilhaft?

| Aspekt | Prozedural | OOP |
|--------|------------|-----|
| **Einfachheit** | Direkt, wenig Abstraktion | Komplexere Strukturen |
| **Erweiterbarkeit** | Schwieriger bei neuen Typen | Leichter bei neuen Typen |
| **Datenkapselung** | Keine | Strenge Kapselung |
| **Code-Wiederverwendung** | Durch Funktionen | Durch Vererbung |

```python
# Prozedural: Neue Primitive = Neue Funktionen überall
def render_scene(scene, painter):
    for shape in scene:
        if shape['type'] == 'rectangle':
            draw_rectangle(shape, painter)
        elif shape['type'] == 'circle':
            draw_circle(shape, painter)
        elif shape['type'] == 'triangle':  # NEU!
            draw_triangle(shape, painter)  # Überall hinzufügen!
        # ... weitere Stellen auch ändern!
```

### 2. Viewport-Transformation

> [!important] **Klausurfrage**: Wie funktioniert die Viewport-Transformation?

```python
def world_to_pixel_explained(world_x, world_y, viewport, pixel_size):
    """Schritt-für-Schritt Erklärung der Transformation"""
    
    # Schritt 1: Normalisierung (0 bis 1)
    world_width = viewport['world_right'] - viewport['world_left']
    norm_x = (world_x - viewport['world_left']) / world_width
    
    # Schritt 2: Skalierung auf Pixelgröße
    pixel_x = norm_x * pixel_size[0]
    
    # Schritt 3: Y-Achse umkehren (Welt: unten=0, Pixel: oben=0)
    world_height = viewport['world_top'] - viewport['world_bottom']
    norm_y = (world_y - viewport['world_bottom']) / world_height
    pixel_y = (1.0 - norm_y) * pixel_size[1]  # Y-Achse umkehren!
    
    return int(pixel_x), int(pixel_y)
```

### 3. Datenstrukturen für Grafik

> [!tip] **Prüfungsfrage**: Welche Datenstrukturen eignen sich für Vektorgrafik?

```python
# Variante 1: Dictionary (flexibel, aber unsicher)
shape = {
    'type': 'circle',
    'x': 100, 'y': 50,
    'radius': 25,
    'color': QColor(255, 0, 0)
}

# Variante 2: Dataclass (typisiert, aber prozedural)
@dataclass
class Circle:
    x: float
    y: float
    radius: float
    color: QColor

# Variante 3: Union Types (modern)
from typing import Union
Shape = Union[Rectangle, Circle, Star]
```

### 4. Koordinatensysteme

> [!important] **Unterschied verstehen**:
> - **Weltkoordinaten**: Mathematisch (Y nach oben, Ursprung beliebig)
> - **Pixelkoordinaten**: Bildschirm (Y nach unten, Ursprung links oben)

---

## Erweiterte Aufgaben und Tipps

### Stern-Algorithmus verstehen:

```python
def create_star_points(center_x, center_y, outer_radius, inner_radius, points):
    """Stern-Punkte berechnen - Algorithmus erklärt"""
    vertices = []
    
    for i in range(points * 2):
        # Winkel: 360° / (2 * points) pro Schritt
        angle = i * math.pi / points
        
        # Alternierend äußerer und innerer Radius
        radius = outer_radius if i % 2 == 0 else inner_radius
        
        # Polarkoordinaten zu kartesischen
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        
        vertices.append((x, y))
    
    return vertices
```

### Performance-Optimierungen:

```python
def optimized_render_scene(scene, painter, viewport, pixel_size):
    """Optimierte Rendering-Funktion"""
    
    # Frustum Culling: Nur sichtbare Objekte zeichnen
    for shape in scene:
        if is_shape_visible(shape, viewport):
            render_shape(shape, painter, viewport, pixel_size)
            
def is_shape_visible(shape, viewport):
    """Prüft ob Shape im sichtbaren Bereich liegt"""
    # Bounding Box des Shapes
    if shape['type'] == 'rectangle':
        left = shape['x']
        right = shape['x'] + shape['width']
        top = shape['y'] + shape['height']
        bottom = shape['y']
    elif shape['type'] == 'circle':
        left = shape['x'] - shape['radius']
        right = shape['x'] + shape['radius']
        top = shape['y'] + shape['radius']
        bottom = shape['y'] - shape['radius']
    
    # Überschneidung mit Viewport prüfen
    return not (right < viewport['world_left'] or 
               left > viewport['world_right'] or
               top < viewport['world_bottom'] or
               bottom > viewport['world_top'])
```

---

## Prüfungsfragen-Training

### Theoretische Fragen:

1. **Nennen Sie drei Vor- und Nachteile prozeduraler Programmierung für Grafiksoftware.**
   > **Vorteile**: Einfach zu verstehen, direkter Kontrollfluss, wenig Abstraktion
   > **Nachteile**: Schwer erweiterbar, Code-Duplikation, keine Datenkapselung

2. **Erklären Sie die Viewport-Transformation Schritt für Schritt.**
   > **Antwort**: Normalisierung → Skalierung → Y-Achse umkehren

3. **Warum muss die Y-Achse bei der Transformation umgekehrt werden?**
   > **Antwort**: Weltkoordinaten (Y nach oben) vs. Pixelkoordinaten (Y nach unten)

### Praktische Aufgaben:

1. **Implementieren Sie eine Funktion `create_triangle()`:**
```python
def create_triangle(x1, y1, x2, y2, x3, y3, fill_color, border_color):
    """Erstellt ein Dreieck-Primitive"""
    return {
        'type': 'triangle',
        'points': [(x1, y1), (x2, y2), (x3, y3)],
        'fill_color': fill_color,
        'border_color': border_color
    }
```

2. **Schreiben Sie eine Funktion für Bounding-Box-Berechnung:**
```python
def calculate_bounding_box(shape):
    """Berechnet Bounding Box für beliebige Shape"""
    if shape['type'] == 'rectangle':
        return {
            'left': shape['x'],
            'right': shape['x'] + shape['width'],
            'top': shape['y'] + shape['height'],
            'bottom': shape['y']
        }
    elif shape['type'] == 'circle':
        return {
            'left': shape['x'] - shape['radius'],
            'right': shape['x'] + shape['radius'],
            'top': shape['y'] + shape['radius'],
            'bottom': shape['y'] - shape['radius']
        }
```

---

## Vorbereitung auf Übungsblatt 04

> [!tip] **Nächste Schritte**: 
> In Übungsblatt 04 wird diese prozedurale Lösung zu OOP refaktoriert:
> - **Abstrakte Klasse `Shape`** statt Dictionary
> - **Polymorphismus** statt if-elif-Ketten
> - **Vererbung** für neue Primitive
> - **Kapselung** von Daten und Methoden

### Wichtige Überlegungen:
```python
# Von prozedural:
def draw_rectangle(rect, painter):
    painter.drawRect(rect['x'], rect['y'], rect['width'], rect['height'])

def draw_circle(circle, painter):
    painter.drawEllipse(circle['x'], circle['y'], circle['radius'])

# Zu OOP:
class Shape:
    def draw(self, painter): pass  # Abstract

class Rectangle(Shape):
    def draw(self, painter):
        painter.drawRect(self.x, self.y, self.width, self.height)

class Circle(Shape):
    def draw(self, painter):
        painter.drawEllipse(self.x, self.y, self.radius)
```

---

## Häufige Fehler und Lösungen

### 1. **Y-Achse vergessen umzukehren**
```python
# FALSCH:
pixel_y = norm_y * pixel_height

# RICHTIG:
pixel_y = (1.0 - norm_y) * pixel_height
```

### 2. **Viewport-Grenzen falsch berechnet**
```python
# FALSCH:
world_width = viewport['world_right'] + viewport['world_left']

# RICHTIG:
world_width = viewport['world_right'] - viewport['world_left']
```

### 3. **Shape-Typen nicht erweitert**
```python
# FALSCH: Neuer Shape-Typ vergessen
if shape['type'] == 'rectangle':
    draw_rectangle(shape, painter)
elif shape['type'] == 'circle':
    draw_circle(shape, painter)
# Star vergessen!

# RICHTIG: Vollständige Behandlung
shape_renderers = {
    'rectangle': draw_rectangle,
    'circle': draw_circle,
    'star': draw_star
}
renderer = shape_renderers.get(shape['type'])
if renderer:
    renderer(shape, painter)
```

---

## Zusammenfassung

> [!summary] **Gelernte Konzepte:**
> - **Prozedurale Strukturierung**: Funktionen + Datenstrukturen
> - **Viewport-Transformation**: Welt- zu Pixelkoordinaten
> - **2D-Grafik-Programmierung**: QPainter verwenden
> - **Interaktive GUIs**: Mouse-Events und Zoom/Pan
> - **Modularisierung**: Trennung von Daten und Algorithmen

> [!tip] **Für die Klausur merken:**
> - Prozedurale Programmierung ist einfach aber schwer erweiterbar
> - Viewport-Transformation: Normalisierung → Skalierung → Y-Achse umkehren
> - Y-Achse in Pixel- vs. Weltkoordinaten ist umgekehrt
> - Datenstrukturen (Dict vs. Dataclass) haben Vor-/Nachteile
> - Frustum Culling für Performance-Optimierung

**Weiter zu Übungsblatt 04: OOP-Refaktorierung dieser Lösung! 🎯**