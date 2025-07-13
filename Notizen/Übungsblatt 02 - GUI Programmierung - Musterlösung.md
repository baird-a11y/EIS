## 1. Grundlagen der GUI-Programmierung

### 1.1 Event-Driven Programming (Ereignisorientierte Programmierung)

**Konzept aus der Vorlesung:**

- **Event Loop**: Hauptschleife wartet auf Ereignisse (Mausklicks, Tastatureingaben)
- **Event Handling**: Behandlung von Ereignissen durch spezielle Methoden
- **Widget-Hierarchie**: Baumstruktur von GUI-Elementen
- **Querverweise**: Events können zwischen verschiedenen Objekten gesendet werden

```python
# Event-Loop wird gestartet mit:
app.exec()  # Blockiert bis Anwendung beendet wird
```

### 1.2 Widget-Hierarchie und Layout-Management

**Wichtige Konzepte:**

- **Parent-Child Beziehungen**: Jedes Widget kann ein übergeordnetes Widget haben
- **Layout-Manager**: Automatische Anordnung von Widgets
- **Central Widget**: Hauptinhalt eines QMainWindow

```python
# Hierarchie aufbauen:
self.setCentralWidget(self.my_frame)    # Frame wird zum Hauptinhalt
self.my_frame.setLayout(self.my_layout) # Layout dem Frame zuweisen
self.my_layout.addWidget(widget)        # Widget zum Layout hinzufügen
```

## 2. Klassenbasierte GUI-Entwicklung

### 2.1 Vererbung von Qt-Klassen

**Warum Vererbung wichtig ist:**

- Anpassung des Verhaltens von Standard-Widgets
- Hinzufügung eigener Funktionalität
- Event-Handling überschreiben

```python
class MyWindow(QMainWindow):    # Erbt von QMainWindow
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)  # Parent-Konstruktor aufrufen!
        # Eigene Initialisierung hier
```

### 2.2 Member-Variablen für Widget-Referenzen

**Warum als Member speichern:**

- Zugriff von verschiedenen Methoden
- Event-Handler benötigen Referenzen
- Wiederverwendung von Actions in Menü und Toolbar

```python
# Actions als Member-Variablen:
self.open_action = QAction("Öffnen", self)
self.save_action = QAction("Speichern", self)

# Verwendung in Menü UND Toolbar:
file_menu.addAction(self.open_action)
toolbar.addAction(self.open_action)
```

## 3. Event-Handling Mechanismen

### 3.1 Signal-Slot Mechanismus

**Konzept:** Lose Kopplung zwischen Sender und Empfänger

```python
# Signal mit Slot verbinden:
button.clicked.connect(self.my_method)
action.triggered.connect(self.my_method)

# Ein Signal kann mehrere Slots haben:
self.quit_action.triggered.connect(self.quit_app)
self.quit_action.triggered.connect(self.save_settings)
```

### 3.2 Event-Methoden überschreiben

**Wichtige Event-Methoden:**

```python
class MyPaintArea(QWidget):
    def paintEvent(self, event):
        """Wird aufgerufen wenn Widget neu gezeichnet werden muss"""
        painter = QPainter(self)
        painter.drawImage(0, 0, self.image)
    
    def mousePressEvent(self, event):
        """Wird aufgerufen wenn Maustaste gedrückt wird"""
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = True
    
    def mouseMoveEvent(self, event):
        """Wird aufgerufen wenn Maus bewegt wird"""
        if self.drawing:
            # Zeichne Linie von last_point zu current_point
    
    def closeEvent(self, event):
        """Wird aufgerufen wenn Fenster geschlossen werden soll"""
        reply = QMessageBox.question(...)
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()  # Schließen erlauben
        else:
            event.ignore()  # Schließen verhindern
```

## 4. Menüs und Toolbars

### 4.1 QAction - Zentrale Kommando-Abstraktion

**Warum QAction verwenden:**

- Einheitliche Behandlung von Menü-Items und Toolbar-Buttons
- Automatische Keyboard-Shortcuts
- Einheitliche Enable/Disable Logik

```python
# QAction erstellen mit allen Features:
action = QAction("&Öffnen...", self)  # & für Alt-Shortcut
action.setShortcut(QKeySequence.StandardKey.Open)  # Ctrl+O
action.setToolTip("Datei öffnen")
action.triggered.connect(self.open_file)

# In Menü und Toolbar verwenden:
file_menu.addAction(action)
toolbar.addAction(action)
```

### 4.2 Menüleisten-Struktur

```python
def create_menu_bar(self):
    menubar = self.menuBar()
    
    # Hauptmenü erstellen:
    file_menu = menubar.addMenu("&Datei")
    
    # Untermenüs hinzufügen:
    file_menu.addAction(self.open_action)
    file_menu.addSeparator()  # Trennlinie
    file_menu.addAction(self.quit_action)
```

## 5. Grafik und Bildverarbeitung

### 5.1 QPainter - Das Zeichensystem

**Wichtige Konzepte:**

- **Double Buffering**: Zeichnen auf QImage, dann auf Widget
- **Coordinate System**: (0,0) ist links oben
- **Painter State**: Pen, Brush, Transform werden gespeichert

```python
# Zeichnen auf QImage (persistente Speicherung):
painter = QPainter(self.image)
pen = QPen(color, width, Qt.PenStyle.SolidLine)
painter.setPen(pen)
painter.drawLine(start_point, end_point)
painter.end()  # Wichtig: Painter freigeben!

# Zeichnen auf Widget (nur Anzeige):
def paintEvent(self, event):
    painter = QPainter(self)
    painter.drawImage(0, 0, self.image)  # Gespeichertes Bild anzeigen
```

### 5.2 QImage vs. QPainter

**QImage:**

- Pixelbasierte Bildspeicherung
- Kann geladen/gespeichert werden
- Format: RGB32, ARGB32, etc.

**QPainter:**

- Zeichnet auf verschiedene "Paint Devices"
- QWidget, QImage, QPrinter, etc.
- Zustandsbasiert (Pen, Brush, Transform)

```python
# Bild erstellen und initialisieren:
self.image = QImage(640, 480, QImage.Format.Format_RGB32)
self.image.fill(QColor(255, 255, 255))  # Weiß füllen

# Bild speichern/laden:
success = self.image.save("drawing.png")
loaded_image = QImage("drawing.png")
```

## 6. Datei-Operationen und Dialoge

### 6.1 QFileDialog - Dateiauswahl

```python
# Datei öffnen:
file_path, _ = QFileDialog.getOpenFileName(
    parent=self,
    caption="Bild öffnen",
    directory="",  # Startverzeichnis
    filter="PNG Files (*.png);;Alle Dateien (*.*)"
)

# Datei speichern:
file_path, _ = QFileDialog.getSaveFileName(
    parent=self,
    caption="Bild speichern",
    directory="drawing.png",  # Vorschlag
    filter="PNG Files (*.png)"
)
```

### 6.2 QMessageBox - Benutzer-Dialoge

```python
# Ja/Nein Frage:
reply = QMessageBox.question(
    self,
    "Titel",
    "Frage?",
    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
    QMessageBox.StandardButton.No  # Default
)

if reply == QMessageBox.StandardButton.Yes:
    # Aktion ausführen
```

## 7. Architektur-Patterns für GUIs

### 7.1 Model-View-Controller (MVC) Konzept

**Im unserem Paint-Beispiel:**

- **Model**: QImage (Bilddaten)
- **View**: MyPaintArea (Anzeige)
- **Controller**: Event-Handler (Maus-Events)

### 7.2 Separation of Concerns

```python
class MyPaintArea(QWidget):  # View + Controller
    def __init__(self):
        self.image = QImage(...)  # Model (Daten)
    
    def paintEvent(self, event):     # View (Anzeige)
        painter = QPainter(self)
        painter.drawImage(0, 0, self.image)
    
    def mouseMoveEvent(self, event): # Controller (Interaktion)
        if self.drawing:
            self.draw_line(...)      # Ändert Model
            self.update()            # Triggert View-Update
```

## 8. Speicherverwaltung und Ressourcen

### 8.1 Qt's Parent-Child System

**Automatische Speicherverwaltung:**

- Parent löscht automatisch alle Child-Widgets
- Kein manuelles `delete` nötig (wie in C++)
- Python's Garbage Collector arbeitet mit Qt zusammen

```python
# Parent-Child wird automatisch gesetzt:
button = QPushButton("Text", parent_widget)
layout.addWidget(button)  # Layout wird auch Parent

# Widget wird automatisch gelöscht wenn Parent gelöscht wird
```

### 8.2 Ressourcen-Management

```python
# QPainter muss explizit beendet werden:
painter = QPainter(self.image)
try:
    painter.drawLine(...)
finally:
    painter.end()  # Ressourcen freigeben

# Oder mit Context Manager (Python 3.8+):
with QPainter(self.image) as painter:
    painter.drawLine(...)  # end() wird automatisch aufgerufen
```

## 9. Threading und GUI

### 9.1 GUI-Thread Regel

**Wichtig für Klausur:**

- Nur der Haupt-Thread darf GUI-Widgets ändern
- QThread für Hintergrund-Operationen
- Signal-Slot für Thread-sichere Kommunikation

```python
# Falsch - GUI aus anderem Thread ändern:
def background_task():
    result = heavy_computation()
    self.label.setText(result)  # FEHLER! Nicht thread-safe

# Richtig - Signal verwenden:
def background_task():
    result = heavy_computation()
    self.result_ready.emit(result)  # Signal senden

# Im GUI-Thread:
self.result_ready.connect(self.update_label)
```

## 10. Klausur-relevante Code-Patterns

### 10.1 Standard GUI-Aufbau

```python
class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        self.create_menu_bar()
        self.create_toolbar()
        self.setup_connections()
    
    def setup_ui(self):
        # Widgets erstellen und Layout zuweisen
    
    def create_menu_bar(self):
        # Menüs und Actions erstellen
    
    def setup_connections(self):
        # Signals mit Slots verbinden
```

### 10.2 Custom Widget Pattern

```python
class MyCustomWidget(QWidget):
    # Custom Signal definieren:
    value_changed = Signal(int)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
    
    def setValue(self, value):
        if self.value != value:
            self.value = value
            self.update()  # Neu zeichnen
            self.value_changed.emit(value)  # Signal senden
```

## 11. Häufige Klausur-Fallen

### 11.1 super().**init**() vergessen

```python
# FALSCH:
class MyWidget(QWidget):
    def __init__(self, parent):
        # super().__init__(parent) vergessen!
        self.setup_ui()

# RICHTIG:
class MyWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)  # Immer aufrufen!
        self.setup_ui()
```

### 11.2 Event.accept() vs. event.ignore()

```python
def closeEvent(self, event):
    if user_wants_to_save():
        self.save_file()
        event.accept()  # Schließen erlauben
    else:
        event.ignore()  # Schließen verhindern
```

### 11.3 update() nach Änderungen

```python
def modify_drawing(self):
    # Bild ändern:
    painter = QPainter(self.image)
    painter.drawLine(...)
    painter.end()
    
    self.update()  # Widget neu zeichnen lassen!
```

## 12. Prüfungstipps

### Was häufig gefragt wird:

1. **Event-Handling**: Welche Methode für welches Event?
2. **Signal-Slot**: Syntax und Konzept erklären
3. **Widget-Hierarchie**: Parent-Child Beziehungen
4. **Layout-Management**: Wie Widgets angeordnet werden
5. **QPainter**: Unterschied zwischen Widget- und Image-Painting
6. **Threading**: GUI-Thread Regeln
7. **Memory Management**: Qt's Parent-Child System

### Wichtige APIs auswendig lernen:

- `QFileDialog.getOpenFileName()`
- `QMessageBox.question()`
- `QPainter.drawLine()`, `QPainter.drawImage()`
- `QImage.save()`, `QImage.load()`
- `widget.update()`, `layout.addWidget()`
- `action.triggered.connect()`

### Code-Struktur verstehen:

- Wann erbt man von welcher Qt-Klasse?
- Wo speichert man Widget-Referenzen?
- Wie strukturiert man Event-Handler?
- Wann verwendet man Signals vs. direkte Methodenaufrufe?