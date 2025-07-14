# Blatt_3.py

#!/usr/bin/env python3
"""
Übungsblatt 02 - GUI mit Menüleiste
EIS SoSem 2025
"""

from PySide6.QtCore import Qt, QPoint, QRect, QSize
from PySide6.QtGui import QKeySequence, QAction, QImage, QColor, QPainter, QPen, QPolygon, QFont
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, 
                              QVBoxLayout, QFrame, QMenuBar, QToolBar,
                              QMessageBox, QFileDialog)
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QDialog, QGridLayout, QSpinBox, QPushButton, QLabel


from math import sin, cos, pi as π
from abc import ABC, abstractmethod
from typing import List, Tuple
import sys

# Typ-Definitionen für bessere Lesbarkeit
Point = Tuple[float, float]
Triangle = Tuple[Point, Point, Point]


def subdivide_triangles(triangles: List[Triangle], n_times: int = 1) -> List[Triangle]:
        """Wendet Subdivision n-mal auf alle Dreiecke an"""
        result = triangles
        for i in range(n_times):
            new_triangles = []
            for triangle in result:
                # Wende Subdivision auf jedes Dreieck an
                # und füge die neuen Dreiecke zur Liste hinzu
                new_triangles.extend(subdivide_triangle(triangle))
            result = new_triangles
        return result

def subdivide_triangle(triangle: Triangle) -> List[Triangle]:
        """Wendet Subdivision n-mal auf alle Dreiecke an"""
        p1,p2,p3 = triangle

        # Mittelpunkte der Seiten berechnen
        mid1 = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)  # Mitte zwischen p1 und p2
        mid2 = ((p2[0] + p3[0]) / 2, (p2[1] + p3[1]) / 2)  # Mitte zwischen p2 und p3
        mid3 = ((p1[0] + p3[0]) / 2, (p1[1] + p3[1]) / 2)  # Mitte zwischen p1 und p3

        # Neue Dreiecke erstellen
        triangle1 = (p1,mid1, mid3) # Erstes neues Dreieck
        triangle2 = (mid1, p2, mid2)  # Zweites neues Dreieck
        triangle3 = (mid2, p3, mid3)  # Drittes neues Dreieck
        triangle4 = (mid1, mid2, mid3)  # Vierte neues Dreieck

        return [triangle1, triangle2, triangle3, triangle4]  # Liste der neuen Dreiecke zurückgeben


def sine_wave_deform_triangles(triangles: List[Triangle], 
                              amplitude: float = 50.0, 
                              wavelength: float = 200.0, 
                              phase: float = 0.0) -> List[Triangle]:
    """Wendet Sine-Wave Deformation auf alle Dreiecke an"""
    deformed_triangles = []
    
    for triangle in triangles:
        p1, p2, p3 = triangle
        
        # Nutze die bereits existierende Funktion!
        new_p1 = sine_wave_deform_point(p1, amplitude, wavelength, phase)
        new_p2 = sine_wave_deform_point(p2, amplitude, wavelength, phase)
        new_p3 = sine_wave_deform_point(p3, amplitude, wavelength, phase)
        
        deformed_triangle = (new_p1, new_p2, new_p3)
        deformed_triangles.append(deformed_triangle)
    
    return deformed_triangles

def sine_wave_deform_point(point: Point, amplitude: float = 50.0, 
                          wavelength: float = 200.0, phase: float = 0.0) -> Point:
    """Deformiert einen Punkt entlang einer Sinuskurve"""
    x, y = point
    y_offset = amplitude * sin(2 * π * x / wavelength + phase)
    return (x, y + y_offset)

def export_triangles_as_text(triangles: List[Triangle], filename: str = "triangles.txt"):
    with open(filename, "w") as file:  # ← Nur EINMAL öffnen, "w" statt "a"
        for i, triangle in enumerate(triangles):  # ← enumerate() ist eleganter
            p1, p2, p3 = triangle
            file.write(f"Triangle {i} ({p1[0]}, {p1[1]}), ({p2[0]}, {p2[1]}), ({p3[0]}, {p3[1]})\n")


def export_triangles_as_svg(triangles: List[Triangle], filename: str = "output.svg", width=800, height=600):
    with open(filename, "w") as file:
        file.write(f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">\n')
        
        for triangle in triangles:
            # TODO: Punkte zu String konvertieren
            p1, p2, p3 = triangle
            p1_str = f"{p1[0]},{p1[1]}"
            p2_str = f"{p2[0]},{p2[1]}"
            p3_str = f"{p3[0]},{p3[1]}"
            # TODO: Polygon-Element schreiben
            file.write(f'  <polygon points="{p1_str} {p2_str} {p3_str}" fill="none" stroke="black" />\n')
        # TODO: SVG Footer schreiben
        file.write('</svg>\n')


# Abstrake Klasse für Datum mit zwei Unterklassen DatumUS und DatumEU
class Datum(ABC):
    """Abstrakte Basisklasse für Datum"""
    def __init__(self, tag, monat, jahr):
        self.tag = tag
        self.monat = monat
        self.jahr = jahr
    
    @abstractmethod
    def print_date(self):
        """Gibt das Datum ausführlich aus (z.B. 24. Dezember 2024)"""
        pass
    
    @abstractmethod
    def print_date_short(self):
        """Gibt das Datum kurz aus (z.B. 24.12.2024)"""
        pass
class DatumUS(Datum):
    """Datum im US-Format (MM/TT/JJJJ)"""
    MONTHS = [
        "Januar", "Februar", "März", "April", "Mai", 
        "Juni", "Juli", "August", "September", 
        "Oktober", "November", "Dezember"
    ] # Liste der Monatsnamen als Klassenattribut
    
    def print_date(self):
        """Ausführliche US-Ausgabe: December 24 2024"""
        monatsname = self.MONTHS[self.monat - 1]  # -1 weil Array bei 0 startet
        print(f"{monatsname} {self.tag} {self.jahr}")
    
    def print_date_short(self):
        """Kurze US-Ausgabe: 12/24/24"""
        jahr_kurz = self.jahr % 100  # Nur die letzten zwei Ziffern
        print(f"{self.monat}/{self.tag}/{jahr_kurz:02d}")


class DatumDE(Datum):
    """Datum im deutschen Format"""
    
    # Deutsche Monatsnamen
    MONATE = ["Januar", "Februar", "März", "April", "Mai", "Juni",
              "Juli", "August", "September", "Oktober", "November", "Dezember"]
    
    def print_date(self):
        """Ausführliche deutsche Ausgabe: 24. Dezember 2024"""
        monatsname = self.MONATE[self.monat - 1]
        print(f"{self.tag}. {monatsname} {self.jahr}")
    
    def print_date_short(self):
        """Kurze deutsche Ausgabe: 24.12.24"""
        jahr_kurz = self.jahr % 100
        print(f"{self.tag:02d}.{self.monat:02d}.{jahr_kurz:02d}")

    


class VectorShape(ABC):
    """Basisklasse für alle geometrischen Primitive"""
    
    def __init__(self, x, y, width, height):
        self.x = x # Position des Objekts
        self.y = y  # Position des Objekts
        self.width = width # Standardwerte für Breite
        self.height = height # Standardwerte für Breite und Höhe
        self.color = QColor(200,200,200,100)  # Transparenz 100%
        self.line_width = 2  # Standard Linienstärke
        self.fill_color = QColor(255, 255, 255) # Standard Füllfarbe (weiß)

    @abstractmethod
    def draw(self, painter, zoom, offset_x, offset_y):
        """Wird in Unterklassen überschrieben"""

    @abstractmethod
    def hit_test(self,  point_x, point_y) -> bool:
        """Prüft, ob der Punkt innerhalb des Objekts liegt"""

    @abstractmethod
    def describe_shape(self) -> List[Triangle]:
        """Beschreibt die Shape als Liste von Dreiecken"""
        pass
    
    def set_position(self, x, y):
        """Setzt die Position des Objekts"""
        self.x = x
        self.y = y

    def set_size(self, width, height):
        """Setzt die Größe des Objekts"""
        self.width = width
        self.height = height

    def move(self, dx, dy):
        """Verschiebt das Objekt um dx, dy"""
        self.x += dx
        self.y += dy

    def scale(self, factor_x, factor_y):
        """Skaliert das Objekt um die gegebenen Faktoren"""
        self.width *= factor_x
        self.height *= factor_y

    

    
    
    
    
class Rectangle(VectorShape):
    def draw(self, painter, zoom, offset_x, offset_y):
        # TODO: Koordinaten transformieren (unsere Formel!)
        x =(self.x + offset_x) * zoom # Transformiere x-Koordinate
        y =(self.y + offset_y) * zoom # Transformiere y-Koordinate
        w = self.width * zoom # Transformiere Breite
        h = self.height * zoom # Transformiere Höhe

        # TODO: QPainter konfigurieren
        # Stift und Pinsel konfigurieren
        pen = QPen(self.color, self.line_width) # Setze die Farbe und Linienstärke
        brush = QColor(self.fill_color) # Setze die Füllfarbe
        painter.setPen(pen)  # Setze den Stift
        painter.setBrush(brush)  # Setze den Pinsel

        # TODO: Rechteck zeichnen
        # Zeichne das Rechteck
        painter.drawRect(x,y,w,h)

    def hit_test(self, point_x, point_y):
            return (self.x <= point_x <= self.x + self.width and 
                self.y <= point_y <= self.y + self.height)
    
    def describe_shape(self):
        # Gibt die Form als Liste von Dreiecken zurück
        # Ein Rechteck kann in zwei Dreiecke unterteilt werden:
        p1 = (self.x, self.y) # Oben Links (A)
        p2 = (self.x+self.width, self.y) # Oben Rechts (B)
        p3 = (self.x+self.width, self.y+self.height) # Unten Rechts (C)
        p4 = (self.x, self.y+self.height) # Unten Links (D
        
        # Dreicke 1 ABC
        Triangle_1 = (p1, p2, p3)

        # Dreieck 2 ACD
        Triangle_2 = (p1, p3, p4)

        return [Triangle_1, Triangle_2]  # Liste der Dreiecke zurückgeben
    
    
        
class Circle(VectorShape):
    def draw(self, painter, zoom, offset_x, offset_y):
        # TODO: Gleiche Koordinaten-Transformation
        x = (self.x + offset_x) * zoom  # Transformiere x-Koordinate
        y = (self.y + offset_y) *zoom  # Transformiere y-Koordinate
        w = self.width * zoom  # Transformiere Breite
        h = self.height * zoom # Transformiere Höhe

        # TODO: painter.drawEllipse() verwenden
        pen =  QPen(self.color, self.line_width)  # Setze die Farbe und Linienstärke
        brush = QColor(self.fill_color)  # Setze die Füllfarbe
        painter.setPen(pen)
        painter.setBrush(brush)

        painter.drawEllipse(x,y,w,h)

    def hit_test(self, point_x, point_y):
        return (self.x <= point_x <= self.x + self.width and 
                self.y <= point_y <= self.y + self.height)
    
    def describe_shape(self):
        # Mittelpunkt berechnen (von der oberen linken Ecke der Bounding Box)
        center_x = self.x + self.width/2 # Da ich oben in der Ecke anfange muss ich noch zu dem Punkt gehen
        center_y = self.y + self.height/2
        center_point = (center_x, center_y)
        radius = min(self.width, self.height)/2
        
        num_triangles = 12
        triangles = []
        
        for i in range(num_triangles):
            angle1 = i * (2 * π / num_triangles)
            angle2 = (i + 1) * (2 * π / num_triangles)  # ← WICHTIG!
            
            # Zwei aufeinanderfolgende Punkte auf dem Rand
            x1 = center_x + radius * cos(angle1)
            y1 = center_y + radius * sin(angle1)
            point1 = (x1, y1)
            
            x2 = center_x + radius * cos(angle2)
            y2 = center_y + radius * sin(angle2)
            point2 = (x2, y2)
            
            # Dreieck: Mittelpunkt → Punkt1 → Punkt2
            triangle = (center_point, point1, point2)
            triangles.append(triangle)
    
        return triangles  # ← Nicht [triangles]!
        

class Star(VectorShape):
    def __init__(self, x, y, width, height, points=5):
        super().__init__(x, y, width, height)
        self.points = points
    
    def draw(self, painter, zoom, offset_x, offset_y):
        skalierung = 0.4  # Skalierung für den inneren Radius
        # TODO: Mittelpunkt berechnen (transformiert)
        center_x = (self.x + self.width/2 +offset_x)* zoom # Transformiere x-Koordinate
        center_y = (self.y + self.height/2 + offset_y) * zoom # Transformiere y-Koordinate
        # TODO: Äußerer/Innerer Radius
        outer_radius = min(self.width, self.height)/2* zoom  # Transformiere Radius
        inner_radius = outer_radius *(1-skalierung)  # Innerer Radius ist halb so groß wie äußerer
        
        # TODO: Punkte in Schleife berechnen
        star_points = []
        for i in range(self.points * 2):
            winkel = i * (2 * π / self.points) - π/2  # -π/2 = Start oben
            
            if i % 2 == 0:
                radius = outer_radius
            else:
                radius = inner_radius * 0.4  # 40% vom äußeren
            
            x = center_x + radius * cos(winkel)  # cos(winkel-π/2) für korrekte Ausrichtung
            y = center_y + radius * sin(winkel)  # sin(winkel-π/2) für korrekte Ausrichtung
            star_points.append(QPoint(int(x), int(y)))
        # TODO: QPolygon erstellen und zeichnen
        polygon = QPolygon(star_points)  # Erstelle ein Polygon aus den Punkten
        pen = QPen(self.color, self.line_width)  # Setze die Farbe und Linienstärke
        brush = QColor(self.fill_color)  # Setze die Füllfarbe
        painter.setPen(pen)
        painter.setBrush(brush)  # Setze den Pinsel
        painter.drawPolygon(polygon)  # Zeichne das Polygon

    def hit_test(self, point_x, point_y):
        return (self.x <= point_x <= self.x + self.width and 
                self.y <= point_y <= self.y + self.height) 
    

class VectorGraphicsArea(QWidget):
    """Widget für Zeichenfunktionen mit Maus-Unterstützung"""
    
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        # In __init__:
        self.shapes = []  # Liste für Vektorgrafik-Objekte
        self.zoom_factor = 1.0
        self.offset_x = 0.0  
        self.offset_y = 0.0

        # Pan-Zustand (für Maus-Drag)
        self.panning = False
        self.last_pan_point = None
        
        # Mouse-Tracking aktivieren
        self.setMouseTracking(True)

        # Testdaten hinzufügen
        self.shapes.append(Rectangle(50, 50, 100, 80))
        # self.shapes.append(Rectangle(200, 100, 150, 100))
        # In VectorGraphicsArea.__init__():
        self.shapes.append(Circle(100, 200, 80, 80))  # Kreis (width=height)
        self.shapes.append(Circle(300, 50, 120, 60))  # Ellipse (width≠height)

        #self.shapes.append(Star(200, 200, 100, 100, points=5))  # Sechszackiger Stern   
        # Mindestgröße festlegen
        self.setMinimumSize(640, 480)

        rect = Rectangle(100, 100, 200, 150)
        triangles = rect.describe_shape()           # 2 Dreiecke
        subdivided = subdivide_triangles(triangles, 2)  # 32 Dreiecke  
        deformed = sine_wave_deform_triangles(subdivided, 30, 300)  # Wellenform!
        export_triangles_as_text(deformed)
        export_triangles_as_svg(deformed, "output.svg", width=800, height=600)  # Exportiere als SVG
        
        
        # Mouse-Tracking aktivieren für mouseMoveEvent
        self.setMouseTracking(True)
    
    def paintEvent(self, event):
        painter = QPainter(self)
        
        for shape in self.shapes:
            shape.draw(painter, self.zoom_factor, self.offset_x, self.offset_y)
        
        painter.end()
        
    def mousePressEvent(self, event):
        """Wird aufgerufen wenn eine Maustaste gedrückt wird"""
        if event.button() == Qt.MouseButton.RightButton:
            self.panning = True
            self.last_pan_point = event.position().toPoint()
    
    def mouseReleaseEvent(self, event):
        """Wird aufgerufen wenn eine Maustaste losgelassen wird"""
        if event.button() == Qt.MouseButton.RightButton:
            self.panning = False
            self.last_pan_point = None
    
    def mouseMoveEvent(self, event):
        """Wird aufgerufen wenn die Maus bewegt wird"""
        if self.panning and self.last_pan_point is not None:
            current_point = event.position().toPoint()
            
            # Berechne Verschiebung
            dx = (current_point.x() - self.last_pan_point.x()) / self.zoom_factor
            dy = (current_point.y() - self.last_pan_point.y()) / self.zoom_factor
            
            # Offset aktualisieren
            self.offset_x += dx
            self.offset_y += dy
            
            # Widget neu zeichnen
            self.update()
            
            # Punkt aktualisieren
            self.last_pan_point = current_point

    def wheelEvent(self, event):
        """Zoom mit Mausrad"""
        # Zoom-Faktor berechnen
        zoom_delta = 1.1 if event.angleDelta().y() > 0 else 1/1.1
        
        # Zoom um Mausposition
        mouse_x = event.position().x()
        mouse_y = event.position().y()
        
        # Weltkoordinaten vor Zoom berechnen
        world_x_before = (mouse_x / self.zoom_factor) - self.offset_x
        world_y_before = (mouse_y / self.zoom_factor) - self.offset_y
        
        # Zoom anwenden
        self.zoom_factor *= zoom_delta
        
        # Zoom begrenzen
        self.zoom_factor = max(0.1, min(10.0, self.zoom_factor))
        
        # Weltkoordinaten nach Zoom berechnen
        world_x_after = (mouse_x / self.zoom_factor) - self.offset_x
        world_y_after = (mouse_y / self.zoom_factor) - self.offset_y
        
        # Offset korrigieren, damit Mausposition gleich bleibt
        self.offset_x += world_x_after - world_x_before
        self.offset_y += world_y_after - world_y_before
        
        # Widget neu zeichnen
        self.update()
    pass

    def zoom_in(self):
        """Vergrößern"""
        self.zoom_factor *= 1.2
        self.zoom_factor = min(10.0, self.zoom_factor)
        self.update()
    
    def zoom_out(self):
        """Verkleinern"""
        self.zoom_factor *= 0.8
        self.zoom_factor = max(0.1, self.zoom_factor)
        self.update()
    
    def reset_view(self):
        """Ansicht zurücksetzen"""
        self.zoom_factor = 1.0
        self.offset_x = 0.0
        self.offset_y = 0.0
        self.update()

    def add_rectangle(self, x, y, width, height):
        """Fügt ein neues Rechteck hinzu"""
        self.shapes.append(Rectangle(x, y, width, height))
        self.update()

    def clear_scene(self):
        """Löscht alle Objekte"""
        self.shapes.clear()
        self.update()

    def save_image(self, file_path: str) -> bool:
        """Speichert die aktuelle Zeichnung als Bilddatei"""
        try:
            # Erstelle ein QImage in der Größe des Widgets
            image = QImage(self.size(), QImage.Format.Format_ARGB32)
            image.fill(Qt.GlobalColor.white)  # Weißer Hintergrund
            
            # Zeichne alles auf das QImage
            painter = QPainter(image)
            for shape in self.shapes:
                shape.draw(painter, self.zoom_factor, self.offset_x, self.offset_y)
            painter.end()
            
            # Speichere das Bild
            return image.save(file_path)
            
        except Exception as e:
            print(f"Fehler beim Speichern: {e}")
            return False
    
    def load_image(self, image: QImage):
        """Lädt ein Bild als Hintergrund (optional)"""
        # Das ist optional - meist will man das Bild nur anzeigen
        self.background_image = image
        self.update()  # Widget neu zeichnen

class VectorGraphicsWindow(QMainWindow):
    """Hauptfenster der Anwendung"""
    
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        
        # Fenster-Titel setzen
        self.setWindowTitle("Übungsblatt 02 - EIS SoSem 2025")
        self.setMinimumSize(600, 400)
        
        # Zentrales Widget erstellen
        self.my_frame = QFrame(self)
        self.setCentralWidget(self.my_frame)
        
        # Layout erstellen
        self.my_layout = QVBoxLayout(self.my_frame)
        self.my_frame.setLayout(self.my_layout)
        
        # Paint-Area hinzufügen
        self.graphics_area = VectorGraphicsArea(self)
        self.my_layout.addWidget(self.graphics_area)
        
        # Menüleiste erstellen
        self.create_menu_bar()
        
        # Toolbar erstellen
        self.create_toolbar()
    
    def create_menu_bar(self):
        """Erstellt die Menüleiste"""
        menubar = self.menuBar()
        
        # Ansicht-Menü
        view_menu = menubar.addMenu("&Ansicht")
        
        self.zoom_in_action = QAction("Ver&größern", self)
        self.zoom_in_action.setShortcut(QKeySequence("Ctrl++"))
        self.zoom_in_action.triggered.connect(self.graphics_area.zoom_in)
        view_menu.addAction(self.zoom_in_action)
        
        self.zoom_out_action = QAction("Ver&kleinern", self)
        self.zoom_out_action.setShortcut(QKeySequence("Ctrl+-"))
        self.zoom_out_action.triggered.connect(self.graphics_area.zoom_out)
        view_menu.addAction(self.zoom_out_action)
        
        self.reset_view_action = QAction("Ansicht &zurücksetzen", self)
        self.reset_view_action.setShortcut(QKeySequence("Ctrl+0"))
        self.reset_view_action.triggered.connect(self.graphics_area.reset_view)
        view_menu.addAction(self.reset_view_action)
        
        view_menu.addSeparator()
        
        # Objekte-Menü
        objects_menu = menubar.addMenu("&Objekte")
        
        self.add_rect_action = QAction("&Rechteck hinzufügen", self)
        self.add_rect_action.triggered.connect(self.add_rectangle)
        objects_menu.addAction(self.add_rect_action)
        
        self.add_circle_action = QAction("&Kreis hinzufügen", self)
        # self.add_circle_action.triggered.connect(self.add_test_circle)
        objects_menu.addAction(self.add_circle_action)
        
        self.add_star_action = QAction("&Stern hinzufügen", self)
        # self.add_star_action.triggered.connect(self.add_test_star)
        objects_menu.addAction(self.add_star_action)
        
        objects_menu.addSeparator()
        
        self.clear_action = QAction("&Alle löschen", self)
        self.clear_action.setShortcut(QKeySequence("Ctrl+L"))
        # self.clear_action.triggered.connect(self.graphics_area.clear_scene)
        objects_menu.addAction(self.clear_action)
        
        objects_menu.addSeparator()
        
        self.test_scene_action = QAction("&Testszene laden", self)
        # self.test_scene_action.triggered.connect(self.graphics_area.create_test_scene)
        objects_menu.addAction(self.test_scene_action)
        
        # Datei-Menü
        file_menu = menubar.addMenu("&Datei")
        
        self.quit_action = QAction("&Beenden", self)
        self.quit_action.setShortcut(QKeySequence.StandardKey.Quit)
        self.quit_action.triggered.connect(self.close)
        file_menu.addAction(self.quit_action)

        self.save_action = QAction("&Speichern unter...", self)
        self.save_action.setShortcut(QKeySequence.StandardKey.SaveAs)
        self.save_action.triggered.connect(self.export_svg)
        file_menu.addAction(self.save_action)
    
    def create_toolbar(self):
        """Erstellt eine Toolbar mit den gleichen Aktionen wie das Menü"""
        # Haupttoolbar erstellen
        self.main_toolbar = self.addToolBar("Hauptwerkzeuge")
        
        # Zoom-Buttons
        self.main_toolbar.addAction(self.zoom_in_action)
        self.main_toolbar.addAction(self.zoom_out_action)
        self.main_toolbar.addAction(self.reset_view_action)
        
        self.main_toolbar.addSeparator()
        
        # Objekt-Buttons
        self.main_toolbar.addAction(self.add_rect_action)
        self.main_toolbar.addAction(self.add_circle_action)
        self.main_toolbar.addAction(self.add_star_action)
        
        self.main_toolbar.addSeparator()
        
        self.main_toolbar.addAction(self.clear_action)
        
    
    def open_file(self):
        """Datei öffnen Dialog - lädt ein PNG-Bild"""
        file_path, _ = QFileDialog.getOpenFileName(
            self, 
            "Bild öffnen", 
            "", 
            "PNG Files (*.png);;Alle Bilddateien (*.png *.jpg *.jpeg *.bmp);;Alle Dateien (*.*)"
        )
        
        if file_path:
            try:
                # Bild laden
                loaded_image = QImage(file_path)
                
                if loaded_image.isNull():
                    QMessageBox.warning(self, "Fehler", "Das Bild konnte nicht geladen werden!")
                    return
                
                # Bild in die Paint-Area laden
                self.graphics_area.load_image(loaded_image)
                print(f"Bild geladen: {file_path}")
                
            except Exception as e:
                QMessageBox.critical(self, "Fehler", f"Fehler beim Laden der Datei:\n{str(e)}")
    
    def save_file_as(self):
        """Speichern Als Dialog - speichert das gezeichnete Bild als PNG, JPEG oder SVG"""
        file_path, _ = QFileDialog.getSaveFileName(
            self, 
            "Bild speichern", 
            "zeichnung.png", 
            "PNG Files (*.png);;JPEG Files (*.jpg);;SVG Files (*.svg);;Alle Dateien (*.*)"
        )
        
        if file_path:
            try:
                # Stelle sicher, dass die Datei eine .png Endung hat
                if not file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp','svg')):
                    file_path += '.png'
                
                # Bild speichern
                success = self.graphics_area.save_image(file_path)
                
                if success:
                    QMessageBox.information(self, "Erfolg", f"Bild erfolgreich gespeichert:\n{file_path}")
                    print(f"Bild gespeichert: {file_path}")
                else:
                    QMessageBox.warning(self, "Fehler", "Das Bild konnte nicht gespeichert werden!")
                    
            except Exception as e:
                QMessageBox.critical(self, "Fehler", f"Fehler beim Speichern der Datei:\n{str(e)}")
    
    def quit_app(self):
        """Anwendung beenden mit Sicherheitsabfrage"""
        reply = QMessageBox.question(
            self, 
            "Beenden bestätigen", 
            "Möchten Sie die Anwendung wirklich beenden?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No  # Standard-Button
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            self.close()
    
    def clear_canvas(self):
        """Löscht die Zeichenfläche"""
        reply = QMessageBox.question(
            self, 
            "Zeichenfläche löschen", 
            "Möchten Sie die Zeichenfläche wirklich löschen?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            self.graphics_area.clear_image()
    
    def show_info(self):
        """Informations-Dialog anzeigen"""
        QMessageBox.information(
            self, 
            "Informationen", 
            "Übungsblatt 02\n"
            "EIS SoSem 2025\n"
            "Autor: [Dein Name hier]"
        )
    
    def closeEvent(self, event):
        """Wird beim Schließen des Fensters aufgerufen"""
        reply = QMessageBox.question(
            self, 
            "Beenden bestätigen", 
            "Möchten Sie die Anwendung wirklich beenden?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

    def add_rectangle(self):
        """Dialog für neues Rechteck"""
    
        dialog = QDialog(self)
        dialog.setWindowTitle("Rechteck hinzufügen")
        dialog.setFixedSize(250, 200)
        
        # Layout erstellen
        layout = QGridLayout(dialog)
        
        # Eingabefelder erstellen
        x_spinbox = QSpinBox()
        x_spinbox.setRange(0, 800)
        x_spinbox.setValue(100)
        
        y_spinbox = QSpinBox()
        y_spinbox.setRange(0, 600)
        y_spinbox.setValue(100)
        
        width_spinbox = QSpinBox()
        width_spinbox.setRange(10, 300)
        width_spinbox.setValue(100)
        
        height_spinbox = QSpinBox()
        height_spinbox.setRange(10, 300)
        height_spinbox.setValue(80)
        
        # Labels und Eingabefelder zum Layout hinzufügen
        layout.addWidget(QLabel("X-Position:"), 0, 0)
        layout.addWidget(x_spinbox, 0, 1)
        
        layout.addWidget(QLabel("Y-Position:"), 1, 0)
        layout.addWidget(y_spinbox, 1, 1)
        
        layout.addWidget(QLabel("Breite:"), 2, 0)
        layout.addWidget(width_spinbox, 2, 1)
        
        layout.addWidget(QLabel("Höhe:"), 3, 0)
        layout.addWidget(height_spinbox, 3, 1)
        
        # Buttons erstellen
        ok_button = QPushButton("OK")
        cancel_button = QPushButton("Abbrechen")
        
        # Button-Layout
        
        button_layout = QHBoxLayout()
        button_layout.addWidget(ok_button)
        button_layout.addWidget(cancel_button)
        
        layout.addLayout(button_layout, 4, 0, 1, 2)
        
        # Button-Funktionen
        def on_ok():
            x = x_spinbox.value()
            y = y_spinbox.value()
            w = width_spinbox.value()
            h = height_spinbox.value()
            self.graphics_area.add_rectangle(x, y, w, h)
            dialog.accept()
        
        def on_cancel():
            dialog.reject()
        
        ok_button.clicked.connect(on_ok)
        cancel_button.clicked.connect(on_cancel)
        
        # Dialog anzeigen
        dialog.exec()

    def export_svg(self):
        """SVG-Export Dialog"""
        file_path, _ = QFileDialog.getSaveFileName(
            self, 
            "Als SVG exportieren", 
            "zeichnung.svg", 
            "SVG Files (*.svg);;Alle Dateien (*.*)"
        )
        
        if file_path:
            try:
                # Stelle sicher, dass die Datei eine .svg Endung hat
                if not file_path.lower().endswith('.svg'):
                    file_path += '.svg'
                
                # Alle Shapes zu Dreiecken konvertieren
                all_triangles = []
                for shape in self.graphics_area.shapes:
                    triangles = shape.describe_shape()
                    all_triangles.extend(triangles)
                
                # SVG exportieren (deine Funktion!)
                export_triangles_as_svg(all_triangles, file_path)
                
                QMessageBox.information(self, "Erfolg", f"SVG erfolgreich exportiert:\n{file_path}")
                
            except Exception as e:
                QMessageBox.critical(self, "Fehler", f"Fehler beim SVG-Export:\n{str(e)}")
    


def main():
    """Hauptprogramm"""
    app = QApplication(sys.argv)
    
    # Hauptfenster erstellen und anzeigen
    main_window = VectorGraphicsWindow()
    main_window.show()
    # Datum-Objekte erstellen und ausgeben
    datum_us = DatumUS(24, 12, 2024)
    datum_us.print_date()  # Ausführliche US-Ausgabe
    datum_us.print_date_short()  # Kurze US-Ausgabe
    datum_de = DatumDE(24, 12, 2024)
    datum_de.print_date()  # Ausführliche deutsche Ausgabe
    datum_de.print_date_short()  # Kurze deutsche Ausgabe
    
    # Event-Loop starten
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())