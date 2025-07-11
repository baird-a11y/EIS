# Übungsblatt 04 - Vektorgrafik OOP - Musterlösung
**Einführung in die Softwareentwicklung (EiS) - SoSem 2025**

> [!important] **Klausurrelevanz**:
> - **Abstrakte Klassen**: Vererbung und Polymorphismus
> - **Dynamic Dispatch**: Methodenaufruf über Vererbungshierarchie
> - **Bounding Box**: Geometrische Berechnungen
> - **Picking**: Punkttreffer in Objekten
> - **Geometrische Transformationen**: Skalierung und Verschiebung
> - **Handle-basierte Objektmanipulation**: Interaktive Grafikanwendung

> [!note] **Lernziele**:
> - Prozedurale Lösung zu OOP refaktorieren
> - Polymorphismus praktisch einsetzen
> - Abstrakte Methoden und Vererbung verstehen
> - Mausinteraktion und geometrische Operationen
> - Architektur-Überlegungen für erweiterbares System

---

## Aufgabe 0: Design (unbewertet)

> [!tip] **Architektur-Überlegungen für OOP-Refaktorierung**:
> - **Abstrakte Basisklasse**: `Shape` mit gemeinsamem Interface
> - **Polymorphismus**: Methoden wie `draw()`, `is_hit()`, `get_bounding_box()`
> - **Erweiterbarkeit**: Neue Shapes ohne Änderung der Render-Logik
> - **Kapselung**: Jede Shape-Klasse kapselt ihre Geometrie
> - **Einheitliche Schnittstelle**: Handle-System für alle Shapes

### Geplante OOP-Struktur:
```python
# Abstrakte Basisklasse
class Shape(ABC):
    @abstractmethod
    def draw(self, painter: QPainter, viewport: Dict, pixel_size: Tuple) -> None
    @abstractmethod
    def is_hit(self, world_x: float, world_y: float) -> bool
    @abstractmethod
    def get_bounding_box(self) -> Dict[str, float]
    @abstractmethod
    def get_num_handles(self) -> int
    @abstractmethod
    def get_handle(self, index: int) -> Tuple[float, float]
    @abstractmethod
    def move_handle(self, index: int, world_x: float, world_y: float) -> None

# Konkrete Implementierungen
class Rectangle(Shape): ...
class Circle(Shape): ...  
class Star(Shape): ...
```

---

## Aufgabe 1: OOP in Python und Scala (30 Punkte)

### Python-Implementierung (10 Punkte):

```python
from abc import ABC, abstractmethod
from typing import List

class Datum(ABC):
    """Abstrakte Basisklasse für Datumsdarstellung"""
    
    def __init__(self, tag: int, monat: int, jahr: int):
        self.tag = tag
        self.monat = monat
        self.jahr = jahr
    
    @abstractmethod
    def print_date(self) -> str:
        """Ausführliche Datumsausgabe"""
        pass
    
    @abstractmethod
    def print_date_short(self) -> str:
        """Kurze Datumsausgabe"""
        pass

class DatumDE(Datum):
    """Deutsche Datumsdarstellung"""
    
    MONATE = [
        "Januar", "Februar", "März", "April", "Mai", "Juni",
        "Juli", "August", "September", "Oktober", "November", "Dezember"
    ]
    
    def print_date(self) -> str:
        """24. Dezember 2024"""
        return f"{self.tag}. {self.MONATE[self.monat - 1]} {self.jahr}"
    
    def print_date_short(self) -> str:
        """24.12.24"""
        return f"{self.tag:02d}.{self.monat:02d}.{self.jahr % 100:02d}"

class DatumUS(Datum):
    """US-amerikanische Datumsdarstellung"""
    
    MONATE = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    
    def print_date(self) -> str:
        """December 24, 2024"""
        return f"{self.MONATE[self.monat - 1]} {self.tag}, {self.jahr}"
    
    def print_date_short(self) -> str:
        """12/24/24"""
        return f"{self.monat:02d}/{self.tag:02d}/{self.jahr % 100:02d}"

# Testprogramm
def test_datum():
    """Testet alle Datumsvarianten"""
    datum_de = DatumDE(24, 12, 2024)
    datum_us = DatumUS(24, 12, 2024)
    
    print("Deutsche Datumsdarstellung:")
    print(f"Lang: {datum_de.print_date()}")
    print(f"Kurz: {datum_de.print_date_short()}")
    
    print("\nUS-amerikanische Datumsdarstellung:")
    print(f"Lang: {datum_us.print_date()}")
    print(f"Kurz: {datum_us.print_date_short()}")

if __name__ == "__main__":
    test_datum()
```

### Scala-Implementierung (20 Punkte):

```scala
// Abstrakte Basisklasse
abstract class Datum(val tag: Int, val monat: Int, val jahr: Int) {
  def print_date(): String
  def print_date_short(): String
}

// Deutsche Datumsdarstellung
class DatumDE(tag: Int, monat: Int, jahr: Int) extends Datum(tag, monat, jahr) {
  private val monate = Array(
    "Januar", "Februar", "März", "April", "Mai", "Juni",
    "Juli", "August", "September", "Oktober", "November", "Dezember"
  )
  
  def print_date(): String = {
    s"${tag}. ${monate(monat - 1)} ${jahr}"
  }
  
  def print_date_short(): String = {
    f"${tag}%02d.${monat}%02d.${jahr % 100}%02d"
  }
}

// US-amerikanische Datumsdarstellung
class DatumUS(tag: Int, monat: Int, jahr: Int) extends Datum(tag, monat, jahr) {
  private val monate = Array(
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
  )
  
  def print_date(): String = {
    s"${monate(monat - 1)} ${tag}, ${jahr}"
  }
  
  def print_date_short(): String = {
    f"${monat}%02d/${tag}%02d/${jahr % 100}%02d"
  }
}

// Testprogramm
object DatumTest {
  def main(args: Array[String]): Unit = {
    val datumDE = new DatumDE(24, 12, 2024)
    val datumUS = new DatumUS(24, 12, 2024)
    
    println("Deutsche Datumsdarstellung:")
    println(s"Lang: ${datumDE.print_date()}")
    println(s"Kurz: ${datumDE.print_date_short()}")
    
    println("\nUS-amerikanische Datumsdarstellung:")
    println(s"Lang: ${datumUS.print_date()}")
    println(s"Kurz: ${datumUS.print_date_short()}")
  }
}
```

---

## Aufgabe 2: Vektorgrafik mit OOP (30 Punkte)

### Vollständige OOP-Refaktorierung:

```python
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, 
                               QVBoxLayout, QHBoxLayout, QPushButton, 
                               QMenuBar, QMenu, QColorDialog, QDialog,
                               QLabel, QDoubleSpinBox, QComboBox, QSpinBox)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QColor, QPen, QBrush, QPolygonF, QPointF
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Tuple, Optional
import sys
import math

# ==================== Hilfsdatenstrukturen ====================

class Vector2d:
    """2D-Vektor für Koordinaten"""
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def __add__(self, other: 'Vector2d') -> 'Vector2d':
        return Vector2d(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: 'Vector2d') -> 'Vector2d':
        return Vector2d(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar: float) -> 'Vector2d':
        return Vector2d(self.x * scalar, self.y * scalar)
    
    def distance(self, other: 'Vector2d') -> float:
        """Euklidische Distanz zu anderem Punkt"""
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx * dx + dy * dy)

class BoundingBox:
    """Axis-aligned Bounding Box"""
    def __init__(self, left: float, top: float, right: float, bottom: float):
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
    
    def contains(self, x: float, y: float) -> bool:
        """Prüft ob Punkt in Bounding Box liegt"""
        return (self.left <= x <= self.right and 
                self.bottom <= y <= self.top)
    
    def width(self) -> float:
        return self.right - self.left
    
    def height(self) -> float:
        return self.top - self.bottom

# ==================== Abstrakte Shape-Klasse ====================

class Shape(ABC):
    """Abstrakte Basisklasse für alle geometrischen Primitive"""
    
    def __init__(self, fill_color: QColor = QColor(100, 100, 255),
                 border_color: QColor = QColor(0, 0, 0),
                 border_width: float = 1.0):
        self.fill_color = fill_color
        self.border_color = border_color
        self.border_width = border_width
        self.selected = False
    
    @abstractmethod
    def draw(self, painter: QPainter, viewport: Dict[str, float], 
             pixel_size: Tuple[int, int]) -> None:
        """Zeichnet das Shape"""
        pass
    
    @abstractmethod
    def is_hit(self, world_x: float, world_y: float) -> bool:
        """Prüft ob Punkt das Shape trifft (Bounding Box Test)"""
        pass
    
    @abstractmethod
    def get_bounding_box(self) -> BoundingBox:
        """Gibt die Bounding Box zurück"""
        pass
    
    @abstractmethod
    def get_num_handles(self) -> int:
        """Anzahl der Transformations-Handles"""
        pass
    
    @abstractmethod
    def get_handle(self, index: int) -> Vector2d:
        """Position des Handle mit gegebenem Index"""
        pass
    
    @abstractmethod
    def move_handle(self, index: int, world_x: float, world_y: float) -> None:
        """Verschiebt Handle auf neue Position"""
        pass

# ==================== Konkrete Shape-Implementierungen ====================

class Rectangle(Shape):
    """Rechteck-Primitive"""
    
    def __init__(self, x: float, y: float, width: float, height: float,
                 fill_color: QColor = QColor(100, 100, 255),
                 border_color: QColor = QColor(0, 0, 0),
                 border_width: float = 1.0):
        super().__init__(fill_color, border_color, border_width)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self, painter: QPainter, viewport: Dict[str, float], 
             pixel_size: Tuple[int, int]) -> None:
        """Zeichnet das Rechteck"""
        pixel_x, pixel_y = world_to_pixel(self.x, self.y, viewport, pixel_size)
        pixel_width = world_to_pixel_size(self.width, viewport, pixel_size, 'width')
        pixel_height = world_to_pixel_size(self.height, viewport, pixel_size, 'height')
        
        painter.setBrush(QBrush(self.fill_color))
        painter.setPen(QPen(self.border_color, self.border_width))
        painter.drawRect(pixel_x, pixel_y, pixel_width, pixel_height)
    
    def is_hit(self, world_x: float, world_y: float) -> bool:
        """Bounding Box Test"""
        return self.get_bounding_box().contains(world_x, world_y)
    
    def get_bounding_box(self) -> BoundingBox:
        """Bounding Box des Rechtecks"""
        return BoundingBox(self.x, self.y + self.height, 
                          self.x + self.width, self.y)
    
    def get_num_handles(self) -> int:
        """Rechteck hat 4 Handles (Ecken)"""
        return 4
    
    def get_handle(self, index: int) -> Vector2d:
        """Handle-Positionen: 0=links oben, 1=rechts oben, 2=rechts unten, 3=links unten"""
        if index == 0:  # links oben
            return Vector2d(self.x, self.y + self.height)
        elif index == 1:  # rechts oben
            return Vector2d(self.x + self.width, self.y + self.height)
        elif index == 2:  # rechts unten
            return Vector2d(self.x + self.width, self.y)
        elif index == 3:  # links unten
            return Vector2d(self.x, self.y)
        else:
            raise IndexError(f"Handle index {index} out of range")
    
    def move_handle(self, index: int, world_x: float, world_y: float) -> None:
        """Verschiebt Handle und passt Rechteck an"""
        if index == 0:  # links oben
            new_width = self.x + self.width - world_x
            new_height = world_y - self.y
            self.x = world_x
            self.width = new_width
            self.height = new_height
        elif index == 1:  # rechts oben
            self.width = world_x - self.x
            self.height = world_y - self.y
        elif index == 2:  # rechts unten
            self.width = world_x - self.x
            new_height = self.y + self.height - world_y
            self.y = world_y
            self.height = new_height
        elif index == 3:  # links unten
            new_width = self.x + self.width - world_x
            new_height = self.y + self.height - world_y
            self.x = world_x
            self.y = world_y
            self.width = new_width
            self.height = new_height

class Circle(Shape):
    """Kreis-Primitive"""
    
    def __init__(self, x: float, y: float, radius: float,
                 fill_color: QColor = QColor(255, 100, 100),
                 border_color: QColor = QColor(0, 0, 0),
                 border_width: float = 1.0):
        super().__init__(fill_color, border_color, border_width)
        self.x = x
        self.y = y
        self.radius = radius
    
    def draw(self, painter: QPainter, viewport: Dict[str, float], 
             pixel_size: Tuple[int, int]) -> None:
        """Zeichnet den Kreis"""
        pixel_x, pixel_y = world_to_pixel(self.x, self.y, viewport, pixel_size)
        pixel_radius = world_to_pixel_size(self.radius, viewport, pixel_size, 'width')
        
        painter.setBrush(QBrush(self.fill_color))
        painter.setPen(QPen(self.border_color, self.border_width))
        painter.drawEllipse(pixel_x - pixel_radius, pixel_y - pixel_radius, 
                          2 * pixel_radius, 2 * pixel_radius)
    
    def is_hit(self, world_x: float, world_y: float) -> bool:
        """Bounding Box Test für Kreis"""
        return self.get_bounding_box().contains(world_x, world_y)
    
    def get_bounding_box(self) -> BoundingBox:
        """Bounding Box des Kreises"""
        return BoundingBox(self.x - self.radius, self.y + self.radius,
                          self.x + self.radius, self.y - self.radius)
    
    def get_num_handles(self) -> int:
        """Kreis hat 4 Handles (Kardinalrichtungen)"""
        return 4
    
    def get_handle(self, index: int) -> Vector2d:
        """Handle-Positionen: 0=oben, 1=rechts, 2=unten, 3=links"""
        if index == 0:  # oben
            return Vector2d(self.x, self.y + self.radius)
        elif index == 1:  # rechts
            return Vector2d(self.x + self.radius, self.y)
        elif index == 2:  # unten
            return Vector2d(self.x, self.y - self.radius)
        elif index == 3:  # links
            return Vector2d(self.x - self.radius, self.y)
        else:
            raise IndexError(f"Handle index {index} out of range")
    
    def move_handle(self, index: int, world_x: float, world_y: float) -> None:
        """Verschiebt Handle und passt Kreis an (wird zur Ellipse)"""
        if index == 0:  # oben - Y-Radius ändern
            self.radius = abs(world_y - self.y)
        elif index == 1:  # rechts - X-Radius ändern
            self.radius = abs(world_x - self.x)
        elif index == 2:  # unten - Y-Radius ändern
            self.radius = abs(world_y - self.y)
        elif index == 3:  # links - X-Radius ändern
            self.radius = abs(world_x - self.x)

class Star(Shape):
    """Stern-Primitive"""
    
    def __init__(self, x: float, y: float, outer_radius: float, 
                 inner_radius: float, points: int = 5,
                 fill_color: QColor = QColor(255, 255, 100),
                 border_color: QColor = QColor(0, 0, 0),
                 border_width: float = 1.0):
        super().__init__(fill_color, border_color, border_width)
        self.x = x
        self.y = y
        self.outer_radius = outer_radius
        self.inner_radius = inner_radius
        self.points = points
    
    def draw(self, painter: QPainter, viewport: Dict[str, float], 
             pixel_size: Tuple[int, int]) -> None:
        """Zeichnet den Stern"""
        # Stern-Punkte berechnen
        vertices = []
        for i in range(self.points * 2):
            angle = i * math.pi / self.points
            radius = self.outer_radius if i % 2 == 0 else self.inner_radius
            
            world_x = self.x + radius * math.cos(angle)
            world_y = self.y + radius * math.sin(angle)
            
            pixel_x, pixel_y = world_to_pixel(world_x, world_y, viewport, pixel_size)
            vertices.append(QPointF(pixel_x, pixel_y))
        
        # Polygon erstellen und zeichnen
        polygon = QPolygonF(vertices)
        painter.setBrush(QBrush(self.fill_color))
        painter.setPen(QPen(self.border_color, self.border_width))
        painter.drawPolygon(polygon)
    
    def is_hit(self, world_x: float, world_y: float) -> bool:
        """Bounding Box Test für Stern"""
        return self.get_bounding_box().contains(world_x, world_y)
    
    def get_bounding_box(self) -> BoundingBox:
        """Bounding Box des Sterns"""
        return BoundingBox(self.x - self.outer_radius, self.y + self.outer_radius,
                          self.x + self.outer_radius, self.y - self.outer_radius)
    
    def get_num_handles(self) -> int:
        """Stern hat 4 Handles (Bounding Box)"""
        return 4
    
    def get_handle(self, index: int) -> Vector2d:
        """Handle-Positionen: 0=links oben, 1=rechts oben, 2=rechts unten, 3=links unten"""
        if index == 0:  # links oben
            return Vector2d(self.x - self.outer_radius, self.y + self.outer_radius)
        elif index == 1:  # rechts oben
            return Vector2d(self.x + self.outer_radius, self.y + self.outer_radius)
        elif index == 2:  # rechts unten
            return Vector2d(self.x + self.outer_radius, self.y - self.outer_radius)
        elif index == 3:  # links unten
            return Vector2d(self.x - self.outer_radius, self.y - self.outer_radius)
        else:
            raise IndexError(f"Handle index {index} out of range")
    
    def move_handle(self, index: int, world_x: float, world_y: float) -> None:
        """Verschiebt Handle und skaliert Stern"""
        # Neue Radiuswerte basierend auf Handle-Position
        if index == 0:  # links oben
            self.outer_radius = abs(self.x - world_x)
        elif index == 1:  # rechts oben
            self.outer_radius = abs(world_x - self.x)
        elif index == 2:  # rechts unten
            self.outer_radius = abs(world_x - self.x)
        elif index == 3:  # links unten
            self.outer_radius = abs(self.x - world_x)
        
        # Inner radius proportional anpassen
        self.inner_radius = self.outer_radius * 0.5

# ==================== Viewport-Transformation ====================

def world_to_pixel(world_x: float, world_y: float, 
                  viewport: Dict[str, float], 
                  pixel_size: Tuple[int, int]) -> Tuple[int, int]:
    """Konvertiert Weltkoordinaten zu Pixelkoordinaten"""
    pixel_width, pixel_height = pixel_size
    
    world_width = viewport['world_right'] - viewport['world_left']
    world_height = viewport['world_top'] - viewport['world_bottom']
    
    norm_x = (world_x - viewport['world_left']) / world_width
    norm_y = (world_y - viewport['world_bottom']) / world_height
    
    pixel_x = int(norm_x * pixel_width)
    pixel_y = int((1.0 - norm_y) * pixel_height)
    
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
    else:
        world_height = viewport['world_top'] - viewport['world_bottom']
        return int(world_size * pixel_height / world_height)

def pixel_to_world(pixel_x: int, pixel_y: int,
                  viewport: Dict[str, float],
                  pixel_size: Tuple[int, int]) -> Tuple[float, float]:
    """Konvertiert Pixel- zu Weltkoordinaten"""
    pixel_width, pixel_height = pixel_size
    
    norm_x = pixel_x / pixel_width
    norm_y = 1.0 - (pixel_y / pixel_height)
    
    world_width = viewport['world_right'] - viewport['world_left']
    world_height = viewport['world_top'] - viewport['world_bottom']
    
    world_x = viewport['world_left'] + norm_x * world_width
    world_y = viewport['world_bottom'] + norm_y * world_height
    
    return world_x, world_y

# ==================== Interaktives Drawing Widget ====================

class InteractiveDrawingWidget(QWidget):
    """Erweiterte Zeichenfläche mit OOP-Shapes und Interaktion"""
    
    def __init__(self):
        super().__init__()
        self.scene: List[Shape] = []
        self.viewport = {
            'world_left': -2.0,
            'world_top': 2.0,
            'world_right': 2.0,
            'world_bottom': -2.0
        }
        self.setMinimumSize(800, 600)
        
        # Interaktionsstatus
        self.selected_shape: Optional[Shape] = None
        self.selected_handle: Optional[int] = None
        self.dragging = False
        self.last_mouse_pos: Optional[Tuple[int, int]] = None
        
        # Zoom und Pan
        self.zoom_factor = 1.0
        self.pan_x = 0.0
        self.pan_y = 0.0
        
    def set_scene(self, scene: List[Shape]):
        """Setzt die zu zeichnende Szene"""
        self.scene = scene
        self.update()
        
    def add_shape(self, shape: Shape):
        """Fügt ein Shape zur Szene hinzu"""
        self.scene.append(shape)
        self.update()
        
    def paintEvent(self, event):
        """Zeichnet die Szene"""
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor(255, 255, 255))
        
        size_tuple = (self.width(), self.height())
        
        # Alle Shapes zeichnen
        for shape in self.scene:
            shape.draw(painter, self.viewport, size_tuple)
            
            # Handles für selektierte Shapes zeichnen
            if shape.selected:
                self.draw_handles(shape, painter, size_tuple)
        
        painter.end()
    
    def draw_handles(self, shape: Shape, painter: QPainter, pixel_size: Tuple[int, int]):
        """Zeichnet die Handles für ein selektiertes Shape"""
        painter.setPen(QPen(QColor(255, 0, 0), 2))
        painter.setBrush(QBrush(QColor(255, 0, 0)))
        
        for i in range(shape.get_num_handles()):
            handle_pos = shape.get_handle(i)
            pixel_x, pixel_y = world_to_pixel(handle_pos.x, handle_pos.y, 
                                             self.viewport, pixel_size)
            painter.drawEllipse(pixel_x - 3, pixel_y - 3, 6, 6)
    
    def mousePressEvent(self, event):
        """Mausklick-Behandlung"""
        if event.button() == Qt.LeftButton:
            world_x, world_y = pixel_to_world(event.pos().x(), event.pos().y(),
                                             self.viewport, (self.width(), self.height()))
            
            # Erst prüfen ob Handle angeklickt wurde
            closest_shape, closest_handle = self.find_closest_handle(world_x, world_y)
            
            if closest_shape and closest_handle is not None:
                # Handle angeklickt
                self.selected_shape = closest_shape
                self.selected_handle = closest_handle
                self.dragging = True
            else:
                # Shape-Selektion
                hit_shape = self.find_hit_shape(world_x, world_y)
                
                # Alle Shapes deselektieren
                for shape in self.scene:
                    shape.selected = False
                
                # Getroffenes Shape selektieren
                if hit_shape:
                    hit_shape.selected = True
                    self.selected_shape = hit_shape
                else:
                    self.selected_shape = None
            
            self.last_mouse_pos = (event.pos().x(), event.pos().y())
            self.update()
    
    def mouseMoveEvent(self, event):
        """Mausbewegung-Behandlung"""
        if self.dragging and self.selected_shape and self.selected_handle is not None:
            world_x, world_y = pixel_to_world(event.pos().x(), event.pos().y(),
                                             self.viewport, (self.width(), self.height()))
            
            # Handle verschieben
            self.selected_shape.move_handle(self.selected_handle, world_x, world_y)
            self.update()
    
    def mouseReleaseEvent(self, event):
        """Mausloslassen-Behandlung"""
        if event.button() == Qt.LeftButton:
            self.dragging = False
            self.selected_handle = None
    
    def find_hit_shape(self, world_x: float, world_y: float) -> Optional[Shape]:
        """Findet das oberste Shape, das vom Punkt getroffen wird"""
        # Rückwärts durch die Liste (oberste Shapes zuerst)
        for shape in reversed(self.scene):
            if shape.is_hit(world_x, world_y):
                return shape
        return None
    
    def find_closest_handle(self, world_x: float, world_y: float) -> Tuple[Optional[Shape], Optional[int]]:
        """Findet das nächste Handle zu einem Punkt"""
        min_distance = float('inf')
        closest_shape = None
        closest_handle = None
        mouse_pos = Vector2d(world_x, world_y)
        
        for shape in self.scene:
            if shape.selected:  # Nur selektierte Shapes haben sichtbare Handles
                for i in range(shape.get_num_handles()):
                    handle_pos = shape.get_handle(i)
                    distance = handle_pos.distance(mouse_pos)
                    
                    if distance < min_distance:
                        min_distance = distance
                        closest_shape = shape
                        closest_handle = i
        
        # Nur zurückgeben wenn Handle nah genug ist
        if min_distance < 0.1:  # Tolerance in Weltkoordinaten
            return closest_shape, closest_handle
        
        return None, None
    
    # Zoom und Pan Funktionen
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

# ==================== Shape-Erstellungsdialog ====================

class CreateShapeDialog(QDialog):
    """Dialog zum Erstellen neuer Shapes"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Create New Shape")
        self.setModal(True)
        self.resize(300, 400)
        
        layout = QVBoxLayout(self)
        
        # Shape Type
        layout.addWidget(QLabel("Shape Type:"))
        self.shape_type = QComboBox()
        self.shape_type.addItems(["Rectangle", "Circle", "Star"])
        self.shape_type.currentTextChanged.connect(self.on_shape_type_changed)
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
        
        # Size Parameters
        self.size_layout = QVBoxLayout()
        self.setup_size_controls()
        layout.addLayout(self.size_layout)
        
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
        
        # Border Width
        border_layout = QHBoxLayout()
        border_layout.addWidget(QLabel("Border Width:"))
        self.border_width_spin = QDoubleSpinBox()
        self.border_width_spin.setRange(0.1, 10.0)
        self.border_width_spin.setValue(1.0)
        border_layout.addWidget(self.border_width_spin)
        layout.addLayout(border_layout)
        
        # Buttons
        button_layout = QHBoxLayout()
        
        create_btn = QPushButton("Create")
        create_btn.clicked.connect(self.accept)
        button_layout.addWidget(create_btn)
        
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.reject)
        button_layout.addWidget(cancel_btn)
        
        layout.addLayout(button_layout)
        
    def setup_size_controls(self):
        """Richtet die Größen-Controls basierend auf Shape-Typ ein"""
        # Alte Controls entfernen
        for i in reversed(range(self.size_layout.count())):
            self.size_layout.itemAt(i).widget().setParent(None)
        
        shape_type = self.shape_type.currentText().lower()
        
        if shape_type == "rectangle":
            # Width und Height
            width_layout = QHBoxLayout()
            width_layout.addWidget(QLabel("Width:"))
            self.width_spin = QDoubleSpinBox()
            self.width_spin.setRange(0.1, 10.0)
            self.width_spin.setValue(1.0)
            width_layout.addWidget(self.width_spin)
            self.size_layout.addLayout(width_layout)
            
            height_layout = QHBoxLayout()
            height_layout.addWidget(QLabel("Height:"))
            self.height_spin = QDoubleSpinBox()
            self.height_spin.setRange(0.1, 10.0)
            self.height_spin.setValue(1.0)
            height_layout.addWidget(self.height_spin)
            self.size_layout.addLayout(height_layout)
            
        elif shape_type == "circle":
            # Radius
            radius_layout = QHBoxLayout()
            radius_layout.addWidget(QLabel("Radius:"))
            self.radius_spin = QDoubleSpinBox()
            self.radius_spin.setRange(0.1, 10.0)
            self.radius_spin.setValue(0.5)
            radius_layout.addWidget(self.radius_spin)
            self.size_layout.addLayout(radius_layout)
            
        elif shape_type == "star":
            # Outer Radius
            outer_radius_layout = QHBoxLayout()
            outer_radius_layout.addWidget(QLabel("Outer Radius:"))
            self.outer_radius_spin = QDoubleSpinBox()
            self.outer_radius_spin.setRange(0.1, 10.0)
            self.outer_radius_spin.setValue(0.6)
            outer_radius_layout.addWidget(self.outer_radius_spin)
            self.size_layout.addLayout(outer_radius_layout)
            
            # Inner Radius
            inner_radius_layout = QHBoxLayout()
            inner_radius_layout.addWidget(QLabel("Inner Radius:"))
            self.inner_radius_spin = QDoubleSpinBox()
            self.inner_radius_spin.setRange(0.1, 10.0)
            self.inner_radius_spin.setValue(0.3)
            inner_radius_layout.addWidget(self.inner_radius_spin)
            self.size_layout.addLayout(inner_radius_layout)
            
            # Points
            points_layout = QHBoxLayout()
            points_layout.addWidget(QLabel("Points:"))
            self.points_spin = QSpinBox()
            self.points_spin.setRange(3, 20)
            self.points_spin.setValue(5)
            points_layout.addWidget(self.points_spin)
            self.size_layout.addLayout(points_layout)
    
    def on_shape_type_changed(self):
        """Wird aufgerufen wenn der Shape-Typ geändert wird"""
        self.setup_size_controls()
        
    def choose_fill_color(self):
        """Wählt Füllfarbe"""
        color = QColorDialog.getColor(self.fill_color, self)
        if color.isValid():
            self.fill_color = color
            
    def choose_border_color(self):
        """Wählt Rahmenfarbe"""
        color = QColorDialog.getColor(self.border_color, self)
        if color.isValid():
            self.border_color = color
            
    def get_shape(self) -> Shape:
        """Erstellt Shape basierend auf Dialog-Eingaben"""
        shape_type = self.shape_type.currentText().lower()
        
        if shape_type == "rectangle":
            return Rectangle(
                self.x_spin.value(), self.y_spin.value(),
                self.width_spin.value(), self.height_spin.value(),
                self.fill_color, self.border_color, self.border_width_spin.value()
            )
        elif shape_type == "circle":
            return Circle(
                self.x_spin.value(), self.y_spin.value(),
                self.radius_spin.value(),
                self.fill_color, self.border_color, self.border_width_spin.value()
            )
        elif shape_type == "star":
            return Star(
                self.x_spin.value(), self.y_spin.value(),
                self.outer_radius_spin.value(), self.inner_radius_spin.value(),
                self.points_spin.value(),
                self.fill_color, self.border_color, self.border_width_spin.value()
            )

# ==================== Hauptfenster ====================

class VectorGraphicsOOPMainWindow(QMainWindow):
    """Hauptfenster der OOP-Vektorgrafik-Anwendung"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EiS - Vektorgrafik OOP")
        self.setGeometry(100, 100, 1200, 800)
        
        # Central Widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout
        layout = QVBoxLayout(central_widget)
        
        # Toolbar
        toolbar_layout = QHBoxLayout()
        
        # Shape Creation
        self.btn_create_shape = QPushButton("Create Shape")
        self.btn_create_shape.clicked.connect(self.create_shape_dialog)
        toolbar_layout.addWidget(self.btn_create_shape)
        
        toolbar_layout.addWidget(QLabel("|"))
        
        # Test Scenes
        self.btn_test_scene1 = QPushButton("Test Scene 1")
        self.btn_test_scene1.clicked.connect(self.create_test_scene1)
        toolbar_layout.addWidget(self.btn_test_scene1)
        
        self.btn_test_scene2 = QPushButton("Test Scene 2")
        self.btn_test_scene2.clicked.connect(self.create_test_scene2)
        toolbar_layout.addWidget(self.btn_test_scene2)
        
        toolbar_layout.addWidget(QLabel("|"))
        
        # Zoom Controls
        self.btn_zoom_in = QPushButton("Zoom In")
        self.btn_zoom_in.clicked.connect(self.zoom_in)
        toolbar_layout.addWidget(self.btn_zoom_in)
        
        self.btn_zoom_out = QPushButton("Zoom Out")
        self.btn_zoom_out.clicked.connect(self.zoom_out)
        toolbar_layout.addWidget(self.btn_zoom_out)
        
        toolbar_layout.addWidget(QLabel("|"))
        
        # Pan Controls
        self.btn_pan_left = QPushButton("← Left")
        self.btn_pan_left.clicked.connect(self.pan_left)
        toolbar_layout.addWidget(self.btn_pan_left)
        
        self.btn_pan_right = QPushButton("Right →")
        self.btn_pan_right.clicked.connect(self.pan_right)
        toolbar_layout.addWidget(self.btn_pan_right)
        
        self.btn_pan_up = QPushButton("↑ Up")
        self.btn_pan_up.clicked.connect(self.pan_up)
        toolbar_layout.addWidget(self.btn_pan_up)
        
        self.btn_pan_down = QPushButton("↓ Down")
        self.btn_pan_down.clicked.connect(self.pan_down)
        toolbar_layout.addWidget(self.btn_pan_down)
        
        toolbar_layout.addWidget(QLabel("|"))
        
        # Clear
        self.btn_clear = QPushButton("Clear Scene")
        self.btn_clear.clicked.connect(self.clear_scene)
        toolbar_layout.addWidget(self.btn_clear)
        
        toolbar_layout.addStretch()
        
        layout.addLayout(toolbar_layout)
        
        # Drawing Area
        self.drawing_widget = InteractiveDrawingWidget()
        layout.addWidget(self.drawing_widget)
        
        # Menu Bar
        self.create_menu_bar()
        
        # Status Bar
        self.statusBar().showMessage("Ready - Click shapes to select, drag handles to transform")
        
    def create_menu_bar(self):
        """Erstellt die Menüleiste"""
        menubar = self.menuBar()
        
        # File Menu
        file_menu = menubar.addMenu('File')
        
        exit_action = file_menu.addAction('Exit')
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(self.close)
        
        # Edit Menu
        edit_menu = menubar.addMenu('Edit')
        
        create_action = edit_menu.addAction('Create Shape...')
        create_action.setShortcut('Ctrl+N')
        create_action.triggered.connect(self.create_shape_dialog)
        
        clear_action = edit_menu.addAction('Clear Scene')
        clear_action.setShortcut('Ctrl+X')
        clear_action.triggered.connect(self.clear_scene)
        
        # View Menu
        view_menu = menubar.addMenu('View')
        
        zoom_in_action = view_menu.addAction('Zoom In')
        zoom_in_action.setShortcut('Ctrl++')
        zoom_in_action.triggered.connect(self.zoom_in)
        
        zoom_out_action = view_menu.addAction('Zoom Out')
        zoom_out_action.setShortcut('Ctrl+-')
        zoom_out_action.triggered.connect(self.zoom_out)
        
        # Scene Menu
        scene_menu = menubar.addMenu('Scene')
        
        scene1_action = scene_menu.addAction('Test Scene 1')
        scene1_action.triggered.connect(self.create_test_scene1)
        
        scene2_action = scene_menu.addAction('Test Scene 2')
        scene2_action.triggered.connect(self.create_test_scene2)
        
    def create_shape_dialog(self):
        """Zeigt Dialog zum Erstellen neuer Shapes"""
        dialog = CreateShapeDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            new_shape = dialog.get_shape()
            self.drawing_widget.add_shape(new_shape)
            self.statusBar().showMessage(f"Added {type(new_shape).__name__}")
    
    def create_test_scene1(self):
        """Erstellt erste OOP-Testszene"""
        scene = [
            Rectangle(-1.5, -0.5, 1.0, 1.0, QColor(255, 100, 100)),
            Circle(0.5, 0.0, 0.4, QColor(100, 255, 100)),
            Star(0, -1.2, 0.6, 0.3, 5, QColor(255, 255, 100))
        ]
        self.drawing_widget.set_scene(scene)
        self.statusBar().showMessage("Loaded Test Scene 1")
        
    def create_test_scene2(self):
        """Erstellt zweite OOP-Testszene"""
        scene = [
            Rectangle(-1.0, 0.5, 2.0, 0.5, QColor(100, 100, 255)),
            Circle(-0.5, -0.3, 0.3, QColor(255, 150, 0)),
            Circle(0.5, -0.3, 0.3, QColor(255, 0, 255)),
            Star(0, -1.2, 0.4, 0.2, 6, QColor(0, 255, 255)),
            Rectangle(0.8, 0.8, 0.6, 0.4, QColor(255, 200, 100))
        ]
        self.drawing_widget.set_scene(scene)
        self.statusBar().showMessage("Loaded Test Scene 2")
        
    def clear_scene(self):
        """Leert die Szene"""
        self.drawing_widget.set_scene([])
        self.statusBar().showMessage("Scene cleared")
        
    def zoom_in(self):
        """Vergrößert die Ansicht"""
        self.drawing_widget.zoom_in()
        self.statusBar().showMessage(f"Zoom: {self.drawing_widget.zoom_factor:.2f}x")
        
    def zoom_out(self):
        """Verkleinert die Ansicht"""
        self.drawing_widget.zoom_out()
        self.statusBar().showMessage(f"Zoom: {self.drawing_widget.zoom_factor:.2f}x")
        
    def pan_left(self):
        """Verschiebt Ansicht nach links"""
        self.drawing_widget.pan_left()
        
    def pan_right(self):
        """Verschiebt Ansicht nach rechts"""
        self.drawing_widget.pan_right()
        
    def pan_up(self):
        """Verschiebt Ansicht nach oben"""
        self.drawing_widget.pan_up()
        
    def pan_down(self):
        """Verschiebt Ansicht nach unten"""
        self.drawing_widget.pan_down()

# ==================== Hauptprogramm ====================

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VectorGraphicsOOPMainWindow()
    window.show()
    app.exec_()
```

---

## Aufgabe 3: Interaktion mit Vektorgrafik (40 Punkte)

### Teil a) Schnittstelle und Implementierung (30 Punkte)

**Siehe vollständige Implementierung oben** ✅

Die Lösung implementiert:

1. **Picking (Bounding Box Test)**:
   - Methode `is_hit()` in jeder Shape-Klasse
   - Einfacher Axis-Aligned Bounding Box Test
   - Effizient und ausreichend für die Aufgabe

2. **Geometrische Transformation**:
   - Handle-basiertes System mit `get_handle()` und `move_handle()`
   - 4 Handles pro Shape für Transformation
   - Nicht-uniforme Skalierung möglich

3. **Abstrakte Schnittstelle**:
   - Polymorphe Methoden für alle Transformationen
   - Erweiterbar für neue Shape-Typen

### Teil b) Mausinteraktion (10 Punkte)

**Siehe vollständige Implementierung oben** ✅

Die Lösung bietet:

1. **Shape-Selektion**: Klick auf Shape selektiert es
2. **Handle-Manipulation**: Drag & Drop von Handles 
3. **Visuelle Rückmeldung**: Handles werden rot dargestellt
4. **Intuitive Bedienung**: Funktioniert mit allen Shape-Typen

### Testcode-Beispiele:

```python
# Test für Picking
def test_picking():
    """Testet die Picking-Funktionalität"""
    rect = Rectangle(0, 0, 2, 1)
    
    # Treffer-Tests
    assert rect.is_hit(1.0, 0.5) == True   # Innerhalb
    assert rect.is_hit(3.0, 0.5) == False  # Außerhalb
    assert rect.is_hit(0.0, 0.0) == True   # Auf Kante
    
    circle = Circle(0, 0, 1)
    assert circle.is_hit(0.5, 0.5) == True   # Innerhalb Bounding Box
    assert circle.is_hit(1.5, 0.0) == False  # Außerhalb
    
    print("Picking tests passed!")

# Test für Transformationen
def test_transformations():
    """Testet die Transformations-Funktionalität"""
    rect = Rectangle(0, 0, 2, 1)
    
    # Handle-Tests
    assert rect.get_num_handles() == 4
    
    # Handle-Positionen
    handle_0 = rect.get_handle(0)  # links oben
    assert handle_0.x == 0 and handle_0.y == 1
    
    # Handle verschieben
    rect.move_handle(1, 3, 1)  # rechts oben nach (3,1)
    assert rect.width == 3
    
    print("Transformation tests passed!")

# Tests ausführen
if __name__ == "__main__":
    test_picking()
    test_transformations()
```

---

## Prüfungsrelevante Konzepte verstehen

### 1. Abstrakte Klassen vs. Interfaces

> [!important] **Klausurfrage**: Wann abstrakte Klassen, wann Interfaces?

| Aspekt | Abstrakte Klassen | Interfaces |
|--------|------------------|------------|
| **Gemeinsamer Code** | Ja, in Basisklasse | Nein, nur Signaturen |
| **Mehrfachvererbung** | Nein (in Python) | Ja (via Mixins) |
| **Datenfelder** | Ja | Nein |
| **Verwendung** | Verwandte Klassen | Unverwandte Klassen |

```python
# Abstrakte Klasse: Gemeinsame Attribute
class Shape(ABC):
    def __init__(self, fill_color, border_color):
        self.fill_color = fill_color  # Gemeinsames Attribut
        self.border_color = border_color
    
    @abstractmethod
    def draw(self): pass  # Abstrakte Methode

# Interface: Nur Verhalten
class Drawable(ABC):
    @abstractmethod
    def draw(self): pass

class Transformable(ABC):
    @abstractmethod
    def transform(self): pass
```

### 2. Polymorphismus und Dynamic Dispatch

> [!important] **Klausurfrage**: Wie funktioniert Dynamic Dispatch?

```python
# Polymorphismus in Aktion
def render_scene(shapes: List[Shape]):
    for shape in shapes:
        shape.draw()  # Ruft die richtige draw()-Methode auf
        # Rectangle.draw() für Rectangle
        # Circle.draw() für Circle
        # Star.draw() für Star

# Ohne Polymorphismus (schlechter Stil):
def render_scene_bad(shapes: List[Dict]):
    for shape in shapes:
        if shape['type'] == 'rectangle':
            draw_rectangle(shape)
        elif shape['type'] == 'circle':
            draw_circle(shape)
        elif shape['type'] == 'star':
            draw_star(shape)
        # Für jeden neuen Typ: Code ändern!
```

### 3. Bounding Box Berechnungen

> [!important] **Klausurfrage**: Verschiedene Bounding Box Implementierungen

```python
# Rechteck: Trivial
def get_bounding_box(self):
    return BoundingBox(self.x, self.y + self.height, 
                      self.x + self.width, self.y)

# Kreis: Radius addieren/subtrahieren
def get_bounding_box(self):
    return BoundingBox(self.x - self.radius, self.y + self.radius,
                      self.x + self.radius, self.y - self.radius)

# Stern: Äußerer Radius als Basis
def get_bounding_box(self):
    return BoundingBox(self.x - self.outer_radius, self.y + self.outer_radius,
                      self.x + self.outer_radius, self.y - self.outer_radius)
```

### 4. Handle-basierte Transformationen

> [!tip] **Prüfungsrelevant**: Handle-System verstehen

```python
# Handle-System Design-Pattern
class TransformableShape(Shape):
    def get_num_handles(self) -> int:
        """Anzahl der Manipulations-Handles"""
        return 4  # Standard: 4 Ecken
    
    def get_handle(self, index: int) -> Vector2d:
        """Position eines Handles"""
        pass  # Implementierung Shape-spezifisch
    
    def move_handle(self, index: int, x: float, y: float) -> None:
        """Verschiebt Handle und transformiert Shape"""
        pass  # Implementierung Shape-spezifisch

# Verwendung:
def transform_shape(shape: Shape, handle_index: int, new_pos: Vector2d):
    shape.move_handle(handle_index, new_pos.x, new_pos.y)
```

---

## Erweiterte Aufgaben und Verbesserungen

### 1. Gruppierung von Shapes

```python
class Group(Shape):
    """Gruppiert mehrere Shapes zusammen"""
    
    def __init__(self, shapes: List[Shape]):
        super().__init__()
        self.shapes = shapes
    
    def draw(self, painter: QPainter, viewport: Dict, pixel_size: Tuple) -> None:
        """Zeichnet alle Shapes in der Gruppe"""
        for shape in self.shapes:
            shape.draw(painter, viewport, pixel_size)
    
    def is_hit(self, world_x: float, world_y: float) -> bool:
        """Treffer wenn irgendein Shape getroffen"""
        return any(shape.is_hit(world_x, world_y) for shape in self.shapes)
    
    def get_bounding_box(self) -> BoundingBox:
        """Umschließende Bounding Box aller Shapes"""
        if not self.shapes:
            return BoundingBox(0, 0, 0, 0)
        
        boxes = [shape.get_bounding_box() for shape in self.shapes]
        
        min_left = min(box.left for box in boxes)
        max_right = max(box.right for box in boxes)
        max_top = max(box.top for box in boxes)
        min_bottom = min(box.bottom for box in boxes)
        
        return BoundingBox(min_left, max_top, max_right, min_bottom)
```

### 2. Erweiterte Picking-Algorithmen

```python
class Circle(Shape):
    def is_hit_precise(self, world_x: float, world_y: float) -> bool:
        """Präziser Kreistest statt Bounding Box"""
        dx = world_x - self.x
        dy = world_y - self.y
        distance = math.sqrt(dx * dx + dy * dy)
        return distance <= self.radius
    
    def is_hit(self, world_x: float, world_y: float) -> bool:
        """Kann zwischen präzise und Bounding Box wählen"""
        # return self.is_hit_precise(world_x, world_y)  # Präzise
        return self.get_bounding_box().contains(world_x, world_y)  # Schnell
```

### 3. Undo/Redo System

```python
from typing import Protocol
from dataclasses import dataclass

class Command(Protocol):
    """Command Pattern für Undo/Redo"""
    def execute(self) -> None: ...
    def undo(self) -> None: ...

@dataclass
class MoveHandleCommand:
    """Command für Handle-Bewegung"""
    shape: Shape
    handle_index: int
    old_position: Vector2d
    new_position: Vector2d
    
    def execute(self) -> None:
        self.shape.move_handle(self.handle_index, self.new_position.x, self.new_position.y)
    
    def undo(self) -> None:
        self.shape.move_handle(self.handle_index, self.old_position.x, self.old_position.y)

class CommandHistory:
    """Verwaltet Command History für Undo/Redo"""
    def __init__(self):
        self.commands: List[Command] = []
        self.current_index = -1
    
    def execute_command(self, command: Command):
        """Führt Command aus und fügt es zur History hinzu"""
        command.execute()
        # Alle Commands nach current_index löschen
        self.commands = self.commands[:self.current_index + 1]
        self.commands.append(command)
        self.current_index += 1
    
    def undo(self) -> bool:
        """Macht letzten Command rückgängig"""
        if self.current_index >= 0:
            self.commands[self.current_index].undo()
            self.current_index -= 1
            return True
        return False
    
    def redo(self) -> bool:
        """Wiederholt rückgängig gemachten Command"""
        if self.current_index < len(self.commands) - 1:
            self.current_index += 1
            self.commands[self.current_index].execute()
            return True
        return False
```

### 4. Erweiterte Transformationen

```python
class Transform:
    """Geometrische Transformationsmatrix"""
    def __init__(self, scale_x: float = 1.0, scale_y: float = 1.0,
                 translate_x: float = 0.0, translate_y: float = 0.0,
                 rotation: float = 0.0):
        self.scale_x = scale_x
        self.scale_y = scale_y
        self.translate_x = translate_x
        self.translate_y = translate_y
        self.rotation = rotation
    
    def apply_to_point(self, point: Vector2d) -> Vector2d:
        """Wendet Transformation auf Punkt an"""
        # Rotation
        cos_r = math.cos(self.rotation)
        sin_r = math.sin(self.rotation)
        
        x_rot = point.x * cos_r - point.y * sin_r
        y_rot = point.x * sin_r + point.y * cos_r
        
        # Skalierung
        x_scaled = x_rot * self.scale_x
        y_scaled = y_rot * self.scale_y
        
        # Translation
        x_final = x_scaled + self.translate_x
        y_final = y_scaled + self.translate_y
        
        return Vector2d(x_final, y_final)

class TransformableShape(Shape):
    """Shape mit Transformations-Support"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.transform = Transform()
    
    def set_transform(self, transform: Transform):
        """Setzt neue Transformation"""
        self.transform = transform
    
    def get_transformed_position(self, local_pos: Vector2d) -> Vector2d:
        """Transformiert lokale Position zu Weltposition"""
        return self.transform.apply_to_point(local_pos)
```

---

## Prüfungsfragen-Training

### Theoretische Fragen:

1. **Erklären Sie den Unterschied zwischen abstrakter Klasse und Interface in Python.**
   > **Antwort**: Abstrakte Klassen können gemeinsame Implementierungen und Attribute haben, Interfaces (Protocol) definieren nur Signaturen. Abstrakte Klassen nutzen `ABC` und `@abstractmethod`, Interfaces nutzen `typing.Protocol`.

2. **Was ist Dynamic Dispatch und wie funktioniert es in Python?**
   > **Antwort**: Automatische Auswahl der richtigen Methode basierend auf dem Typ des Objekts zur Laufzeit. Python nutzt das Dictionary im Objekt (`__dict__`) um die richtige Methode zu finden.

3. **Warum ist das Handle-System besser als direkte Koordinaten-Manipulation?**
   > **Antwort**: Einheitliche Schnittstelle für alle Shapes, benutzerfreundliche Interaktion, Shape-spezifische Transformations-Logik gekapselt.

### Praktische Aufgaben:

1. **Implementieren Sie eine `Triangle`-Klasse:**
```python
class Triangle(Shape):
    def __init__(self, p1: Vector2d, p2: Vector2d, p3: Vector2d,
                 fill_color: QColor = QColor(100, 255, 100),
                 border_color: QColor = QColor(0, 0, 0),
                 border_width: float = 1.0):
        super().__init__(fill_color, border_color, border_width)
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    
    def draw(self, painter: QPainter, viewport: Dict, pixel_size: Tuple) -> None:
        """Zeichnet das Dreieck"""
        points = []
        for p in [self.p1, self.p2, self.p3]:
            pixel_x, pixel_y = world_to_pixel(p.x, p.y, viewport, pixel_size)
            points.append(QPointF(pixel_x, pixel_y))
        
        polygon = QPolygonF(points)
        painter.setBrush(QBrush(self.fill_color))
        painter.setPen(QPen(self.border_color, self.border_width))
        painter.drawPolygon(polygon)
    
    def get_bounding_box(self) -> BoundingBox:
        """Bounding Box des Dreiecks"""
        xs = [self.p1.x, self.p2.x, self.p3.x]
        ys = [self.p1.y, self.p2.y, self.p3.y]
        return BoundingBox(min(xs), max(ys), max(xs), min(ys))
    
    def get_num_handles(self) -> int:
        return 3  # Drei Eckpunkte
    
    def get_handle(self, index: int) -> Vector2d:
        if index == 0: return self.p1
        elif index == 1: return self.p2
        elif index == 2: return self.p3
        else: raise IndexError(f"Handle index {index} out of range")
    
    def move_handle(self, index: int, world_x: float, world_y: float) -> None:
        if index == 0: self.p1 = Vector2d(world_x, world_y)
        elif index == 1: self.p2 = Vector2d(world_x, world_y)
        elif index == 2: self.p3 = Vector2d(world_x, world_y)
```

2. **Implementieren Sie eine `ShapeFactory`:**
```python
class ShapeFactory:
    """Factory Pattern für Shape-Erstellung"""
    
    @staticmethod
    def create_shape(shape_type: str, **kwargs) -> Shape:
        """Erstellt Shape basierend auf Typ"""
        if shape_type.lower() == 'rectangle':
            return Rectangle(**kwargs)
        elif shape_type.lower() == 'circle':
            return Circle(**kwargs)
        elif shape_type.lower() == 'star':
            return Star(**kwargs)
        elif shape_type.lower() == 'triangle':
            return Triangle(**kwargs)
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")
    
    @staticmethod
    def get_available_shapes() -> List[str]:
        """Gibt verfügbare Shape-Typen zurück"""
        return ['rectangle', 'circle', 'star', 'triangle']
```

---

## Fehlerbehandlung und Robustheit

### 1. Eingabe-Validierung

```python
class Shape(ABC):
    def __init__(self, fill_color: QColor, border_color: QColor, border_width: float):
        if not isinstance(fill_color, QColor):
            raise TypeError("fill_color must be QColor")
        if not isinstance(border_color, QColor):
            raise TypeError("border_color must be QColor")
        if border_width <= 0:
            raise ValueError("border_width must be positive")
        
        self.fill_color = fill_color
        self.border_color = border_color
        self.border_width = border_width

class Rectangle(Shape):
    def __init__(self, x: float, y: float, width: float, height: float, **kwargs):
        super().__init__(**kwargs)
        
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
```

### 2. Sichere Handle-Manipulation

```python
class Shape(ABC):
    def move_handle_safe(self, index: int, world_x: float, world_y: float) -> bool:
        """Sichere Handle-Bewegung mit Validierung"""
        try:
            if not (0 <= index < self.get_num_handles()):
                return False
            
            # Backup der aktuellen Position
            old_state = self.get_state()
            
            # Transformation durchführen
            self.move_handle(index, world_x, world_y)
            
            # Validierung des neuen Zustands
            if not self.is_valid_state():
                self.restore_state(old_state)
                return False
            
            return True
        except Exception:
            return False
    
    @abstractmethod
    def get_state(self) -> Dict[str, Any]:
        """Gibt aktuellen Zustand zurück"""
        pass
    
    @abstractmethod
    def restore_state(self, state: Dict[str, Any]) -> None:
        """Stellt Zustand wieder her"""
        pass
    
    @abstractmethod
    def is_valid_state(self) -> bool:
        """Prüft ob aktueller Zustand gültig ist"""
        pass
```

---

## Häufige Fehler und Lösungen

### 1. **Vergessene abstrakte Methoden**
```python
# FALSCH: Abstrakte Methode nicht implementiert
class BadRectangle(Shape):
    def draw(self, painter): pass
    # is_hit() vergessen!

# RICHTIG: Alle abstrakten Methoden implementiert
class GoodRectangle(Shape):
    def draw(self, painter): pass
    def is_hit(self, x, y): pass
    def get_bounding_box(self): pass
    def get_num_handles(self): pass
    def get_handle(self, index): pass
    def move_handle(self, index, x, y): pass
```

### 2. **Falsche Handle-Indizierung**
```python
# FALSCH: Inkonsistente Handle-Indizierung
def get_handle(self, index):
    if index == 1: return self.top_left    # Startet bei 1!
    elif index == 2: return self.top_right

# RICHTIG: Konsistente 0-basierte Indizierung
def get_handle(self, index):
    if index == 0: return self.top_left    # Startet bei 0
    elif index == 1: return self.top_right
    elif index == 2: return self.bottom_right
    elif index == 3: return self.bottom_left
    else: raise IndexError(f"Handle index {index} out of range")
```

### 3. **Bounding Box Berechnungsfehler**
```python
# FALSCH: Vertauschte Koordinaten
def get_bounding_box(self):
    return BoundingBox(self.x, self.y, self.x + self.width, self.y + self.height)
    # Y-Koordinaten sind falsch!

# RICHTIG: Korrekte Y-Koordinaten
def get_bounding_box(self):
    return BoundingBox(self.x, self.y + self.height, self.x + self.width, self.y)
    # top > bottom in Weltkoordinaten
```

---

## Performance-Optimierungen

### 1. **Dirty Flag Pattern**
```python
class OptimizedShape(Shape):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._cached_bounding_box = None
        self._bbox_dirty = True
    
    def get_bounding_box(self) -> BoundingBox:
        """Gecachte Bounding Box Berechnung"""
        if self._bbox_dirty:
            self._cached_bounding_box = self._calculate_bounding_box()
            self._bbox_dirty = False
        return self._cached_bounding_box
    
    def move_handle(self, index: int, world_x: float, world_y: float) -> None:
        """Invalidiert Cache bei Änderung"""
        super().move_handle(index, world_x, world_y)
        self._bbox_dirty = True
    
    @abstractmethod
    def _calculate_bounding_box(self) -> BoundingBox:
        """Berechnet Bounding Box neu"""
        pass
```

### 2. **Spatial Indexing**
```python
class SpatialIndex:
    """Einfacher Spatial Index für schnelles Picking"""
    def __init__(self, grid_size: float = 1.0):
        self.grid_size = grid_size
        self.grid: Dict[Tuple[int, int], List[Shape]] = {}
    
    def add_shape(self, shape: Shape):
        """Fügt Shape zum Index hinzu"""
        bbox = shape.get_bounding_box()
        
        # Betroffene Grid-Zellen berechnen
        min_x = int(bbox.left // self.grid_size)
        max_x = int(bbox.right // self.grid_size)
        min_y = int(bbox.bottom // self.grid_size)
        max_y = int(bbox.top // self.grid_size)
        
        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                cell = (x, y)
                if cell not in self.grid:
                    self.grid[cell] = []
                self.grid[cell].append(shape)
    
    def find_shapes_at(self, world_x: float, world_y: float) -> List[Shape]:
        """Findet Shapes an Position (schneller als linear search)"""
        cell_x = int(world_x // self.grid_size)
        cell_y = int(world_y // self.grid_size)
        cell = (cell_x, cell_y)
        
        if cell in self.grid:
            return [shape for shape in self.grid[cell] 
                   if shape.is_hit(world_x, world_y)]
        return []
```

---

## Vorbereitung auf Übungsblatt 05

> [!tip] **Nächste Schritte**: 
> In Übungsblatt 05 wird die OOP-Lösung zu funktionaler Programmierung erweitert:
> - **Datenfluss-Architektur** statt Objektmethoden
> - **Immutable Datenstrukturen** statt veränderbarer Objekte
> - **Funktionale Transformationen** statt Objektmanipulation
> - **SVG-Export** durch funktionale Serialisierung

### Vorbereitung auf funktionale Konzepte:
```python
# Von OOP (Methoden auf Objekten):
circle = Circle(0, 0, 1)
circle.move_handle(0, 2, 0)  # Verändert Objekt

# Zu funktional (Daten + Funktionen):
circle = Circle(0, 0, 1)
new_circle = move_handle(circle, 0, 2, 0)  # Gibt neues Objekt zurück

# Datenfluss-Pipeline:
result = shapes |> filter_visible |> transform_coordinates |> render_svg
```

---

## Zusammenfassung

> [!summary] **Gelernte Konzepte**:
> - **Abstrakte Klassen**: Gemeinsame Schnittstelle für verwandte Typen
> - **Polymorphismus**: Einheitliche Behandlung verschiedener Typen
> - **Dynamic Dispatch**: Automatische Methodenauswahl zur Laufzeit
> - **Handle-System**: Benutzerfreundliche Objekt-Manipulation
> - **Bounding Box**: Effiziente geometrische Berechnungen
> - **Picking**: Interaktive Objektauswahl

> [!tip] **Für die Klausur merken**:
> - Abstrakte Klassen haben gemeinsame Implementierungen, Interfaces nur Signaturen
> - Dynamic Dispatch wählt Methode basierend auf Objekttyp zur Laufzeit
> - Handle-System bietet einheitliche Transformations-Schnittstelle
> - Bounding Box ist axis-aligned für einfache Berechnungen
> - Polymorphismus eliminiert if-elif-Ketten für Typenbehandlung
> - OOP ist gut für erweiterbare Typen, funktional für erweiterbare Operationen

**Weiter zu Übungsblatt 05: Funktionale Programmierung und SVG-Export! 🚀**