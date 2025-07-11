# Übungsblatt 02 - GUI Programmierung - Musterlösung
**Einführung in die Softwareentwicklung (EiS) - SoSem 2025**

> [!important] **Klausurrelevanz**: 
> - Ereignisorientierte Programmierung verstehen
> - GUI-Frameworks (Qt/PySide vs. Swing/AWT) vergleichen
> - Event-Handler und Callbacks implementieren
> - Grundlagen für alle späteren Vektorgrafik-Übungen

---

## Aufgabe 3: Ein sehr einfaches GUI (30 Punkte)

### Lernziele und Prüfungsrelevanz

> [!note] **Was du hier lernst:**
> - **GUI-Programmierung**: Grundlagen von Desktop-Anwendungen
> - **Event-Handler**: Wie reagiert Software auf Benutzereingaben?
> - **Layouts**: Wie organisiert man GUI-Elemente?
> - **Callbacks**: Funktionen als Parameter übergeben

> [!tip] **Prüfungsrelevante Konzepte:**
> - Warum sind GUIs ereignisorientiert?
> - Unterschied zwischen Qt (Signal/Slot) und Swing (ActionListener)
> - Callback-Funktionen vs. Polling-Mechanismen
> - Widget-Hierarchie und Layout-Management

---

### Teil a) Installation PySide6 (unbewertet)

#### Ubuntu/Debian Installation:
```bash
# Methode 1: Über apt (empfohlen für Ubuntu)
sudo apt update
sudo apt install python3-pyside6.qtcore
sudo apt install python3-pyside6.qtgui
sudo apt install python3-pyside6.qtwidgets
sudo apt install python3-pyside6.qtuitools

# Methode 2: Über pip (für andere Systeme)
pip install PySide6
```

> [!tip] **Warum PySide6?**
> - **Qt-basiert**: Professionelle GUI-Bibliothek
> - **Cross-Platform**: Windows, macOS, Linux
> - **Vollständig**: Alle GUI-Komponenten verfügbar
> - **Gut dokumentiert**: Viele Beispiele und Tutorials

---

### Teil b) Grundlegendes GUI-Programm (unbewertet)

#### Python + PySide6 Lösung:

```python
# import all the widgets
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QFrame, QMessageBox
# only needed for command line arguments
import sys

# we define our own window type to build a custom UI
class MyWindow(QMainWindow):
    def quit_app(self):
        """Beendet die Anwendung durch Schließen des Fensters"""
        # closing the last (and only) window ends the application
        self.close()
    
    def show_dialog(self):
        """Zeigt einen einfachen Dialog mit einer Nachricht"""
        # open a simple dialog window to say hello
        QMessageBox.question(self, "Some message...", "Hello World!", QMessageBox.Ok)
    
    def __init__(self, parent):
        """Konstruktor: Erstellt das GUI-Layout"""
        # call parent constructor
        super().__init__(parent)
        
        # a bit of housekeeping...
        # set a frame object (empty container) that fills the whole window
        self.frame = QFrame(self)
        # make this the content of the main window
        self.setCentralWidget(self.frame)
        
        # create a layout object
        self.my_layout = QVBoxLayout(self.frame)
        # tell the frame (just created) to use this layout
        self.frame.setLayout(self.my_layout)
        
        # make a button!
        # create a button, remember in a member variable
        self.btn_dialog = QPushButton("show dialog")
        # connect button to method of self object
        self.btn_dialog.clicked.connect(self.show_dialog)
        # add the button to the UI via the layout object
        self.my_layout.addWidget(self.btn_dialog)
        
        # same procedure again...
        self.btn_quit = QPushButton("quit")
        self.btn_quit.clicked.connect(self.quit_app)
        self.my_layout.addWidget(self.btn_quit)

# our main program starts here, Python-style
if __name__ == "__main__":
    # create an application object (needs cmd-line arguments)
    app: QApplication = QApplication(sys.argv)
    # Create the main window.
    main_window: MyWindow = MyWindow(None)
    main_window.show() 
    # Start the event loop. 
    # Ends only after closing the main window
    app.exec_()
```

#### Scala + AWT/Swing Lösung:

```scala
// get all the AWT/SWING components we need
import java.awt.BorderLayout
import java.awt.Dimension
import java.awt.GridLayout
import javax.swing.JFrame
import javax.swing.JPanel
import javax.swing.JButton
import javax.swing.WindowConstants
import javax.swing.JOptionPane

object SwingHelloWorld extends App { // a fancy way of creating an application
    // some member functions, for later use
    def showSomeDialog(): Unit = {
        JOptionPane.showMessageDialog(null, "Hello World!");
    }
    
    def doQuit(): Unit = {
        mainWindow.setVisible(false)
        mainWindow.dispose()
    }
    
    // member variables to remember all the components we need
    // first, two new buttons
    var buttonDialog = new JButton("show dialog")
    var buttonQuit = new JButton("quit")
    
    // then, a panel, where the buttons are put into
    var panel = new JPanel()
    // and a layout, for the panel to arrange the buttons
    var layout = new GridLayout(2,1)
    panel.setLayout(layout)
    
    // we now add the buttons to the panel
    panel.add(buttonDialog)
    panel.add(buttonQuit)
    
    // we connect member functions as events to be called to the buttons
    buttonDialog.addActionListener(e => showSomeDialog())
    buttonQuit.addActionListener(e => doQuit())
    
    // now we create the main window (simple window via type "JFrame")
    var mainWindow = new JFrame("Scala & Swing Example")
    // it also needs a layout
    mainWindow.getContentPane.add(panel, BorderLayout.CENTER)
    // when it is closed, the whole app should quit
    mainWindow.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE)
    // set some default size, why not VGA?
    mainWindow.setSize(new Dimension(640, 480))
    // center the new window on the screen
    mainWindow.setLocationRelativeTo(null)
    // show the window
    mainWindow.setVisible(true)
}
```

---

### Teil c) Erweiterung um dritten Button (30 Punkte)

> [!note] **Aufgabe**: Füge einen dritten Button hinzu, der "42" auf der Konsole ausgibt

#### Python + PySide6 - Erweiterte Lösung:

```python
# import all the widgets
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QFrame, QMessageBox
import sys

class MyWindow(QMainWindow):
    def quit_app(self):
        """Beendet die Anwendung durch Schließen des Fensters"""
        self.close()
    
    def show_dialog(self):
        """Zeigt einen einfachen Dialog mit einer Nachricht"""
        QMessageBox.question(self, "Some message...", "Hello World!", QMessageBox.Ok)
    
    def print_answer(self):
        """Gibt die Antwort auf die Frage nach dem Leben aus"""
        print("42")
        # Optional: Auch visuelles Feedback
        print("The Answer to the Ultimate Question of Life, the Universe, and Everything!")
    
    def __init__(self, parent):
        """Konstruktor: Erstellt das GUI-Layout"""
        super().__init__(parent)
        
        # Set window title
        self.setWindowTitle("EiS - GUI Übung 02")
        
        # Create central widget and layout
        self.frame = QFrame(self)
        self.setCentralWidget(self.frame)
        self.my_layout = QVBoxLayout(self.frame)
        self.frame.setLayout(self.my_layout)
        
        # Button 1: Show dialog
        self.btn_dialog = QPushButton("Show Dialog")
        self.btn_dialog.clicked.connect(self.show_dialog)
        self.my_layout.addWidget(self.btn_dialog)
        
        # Button 2: Print 42 (NEW!)
        self.btn_answer = QPushButton("Answer to Everything")
        self.btn_answer.clicked.connect(self.print_answer)
        self.my_layout.addWidget(self.btn_answer)
        
        # Button 3: Quit
        self.btn_quit = QPushButton("Quit")
        self.btn_quit.clicked.connect(self.quit_app)
        self.my_layout.addWidget(self.btn_quit)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MyWindow(None)
    main_window.show()
    app.exec_()
```

#### Scala + AWT/Swing - Erweiterte Lösung:

```scala
import java.awt.BorderLayout
import java.awt.Dimension
import java.awt.GridLayout
import javax.swing.JFrame
import javax.swing.JPanel
import javax.swing.JButton
import javax.swing.WindowConstants
import javax.swing.JOptionPane

object SwingHelloWorldExtended extends App {
    
    def showSomeDialog(): Unit = {
        JOptionPane.showMessageDialog(null, "Hello World!")
    }
    
    def printAnswer(): Unit = {
        println("42")
        println("The Answer to the Ultimate Question of Life, the Universe, and Everything!")
    }
    
    def doQuit(): Unit = {
        mainWindow.setVisible(false)
        mainWindow.dispose()
    }
    
    // Create buttons
    var buttonDialog = new JButton("Show Dialog")
    var buttonAnswer = new JButton("Answer to Everything")  // NEW!
    var buttonQuit = new JButton("Quit")
    
    // Create panel and layout
    var panel = new JPanel()
    var layout = new GridLayout(3, 1)  // Changed to 3 rows for 3 buttons
    panel.setLayout(layout)
    
    // Add buttons to panel
    panel.add(buttonDialog)
    panel.add(buttonAnswer)  // NEW!
    panel.add(buttonQuit)
    
    // Connect event handlers
    buttonDialog.addActionListener(e => showSomeDialog())
    buttonAnswer.addActionListener(e => printAnswer())  // NEW!
    buttonQuit.addActionListener(e => doQuit())
    
    // Create main window
    var mainWindow = new JFrame("Scala & Swing Example - Extended")
    mainWindow.getContentPane.add(panel, BorderLayout.CENTER)
    mainWindow.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE)
    mainWindow.setSize(new Dimension(640, 480))
    mainWindow.setLocationRelativeTo(null)
    mainWindow.setVisible(true)
}
```

---

## GUI-Konzepte verstehen (Prüfungsrelevant)

### Event-Driven Programming

> [!important] **Konzept**: GUIs sind ereignisorientiert
> - **Polling**: Programm fragt ständig "Wurde geklickt?" (ineffizient)
> - **Events**: System benachrichtigt bei Ereignissen (effizient)

```python
# FALSCH: Polling-Ansatz (theoretisch)
while True:
    if button_clicked():
        handle_click()
    time.sleep(0.01)  # Verschwendung von CPU-Zeit!

# RICHTIG: Event-Handler
button.clicked.connect(handle_click)  # Wird nur bei Klick aufgerufen
```

### Signal/Slot vs. ActionListener

| Aspekt | Qt (Signal/Slot) | Swing (ActionListener) |
|--------|------------------|------------------------|
| **Syntax** | `button.clicked.connect(handler)` | `button.addActionListener(e => handler())` |
| **Typsicherheit** | Typisiert | Lambda-Parameter |
| **Flexibilität** | Ein Signal → Viele Slots | Ein Event → Ein Listener |
| **Entkopplung** | Stark entkoppelt | Weniger entkoppelt |

### Widget-Hierarchie

```python
# PySide6 Hierarchie
QApplication
└── QMainWindow
    └── QFrame (Central Widget)
        └── QVBoxLayout
            ├── QPushButton
            ├── QPushButton
            └── QPushButton
```

```scala
// Swing Hierarchie
App
└── JFrame
    └── JPanel
        └── GridLayout
            ├── JButton
            ├── JButton
            └── JButton
```

---

## Prüfungsfragen-Training

### Theoretische Fragen:

1. **Warum sind GUIs ereignisorientiert?**
   > **Antwort**: Effizienz - statt kontinuierlichem Polling reagiert das System nur auf tatsächliche Ereignisse

2. **Was ist der Unterschied zwischen Qt's Signal/Slot und Swing's ActionListener?**
   > **Antwort**: Signal/Slot ist typsicher und ermöglicht 1:n Verbindungen, ActionListener ist flexibler aber weniger typsicher

3. **Welche Rolle spielt die Event-Loop?**
   > **Antwort**: Zentrale Schleife die auf Events wartet und entsprechende Handler aufruft

### Praktische Fragen:

1. **Implementiere einen Button, der die Fensterfarbe ändert:**
```python
def change_color(self):
    self.frame.setStyleSheet("background-color: lightblue;")

self.btn_color = QPushButton("Change Color")
self.btn_color.clicked.connect(self.change_color)
```

2. **Erstelle ein Menü mit File → Exit:**
```python
def create_menu(self):
    menubar = self.menuBar()
    file_menu = menubar.addMenu('File')
    exit_action = file_menu.addAction('Exit')
    exit_action.triggered.connect(self.quit_app)
```

---

## Erweiterte Übungen (Optional)

### 1. Menüleiste hinzufügen:

```python
def create_menu_bar(self):
    """Erstellt eine Menüleiste mit File-Menü"""
    menubar = self.menuBar()
    
    # File Menu
    file_menu = menubar.addMenu('File')
    
    # Exit Action
    exit_action = file_menu.addAction('Exit')
    exit_action.setShortcut('Ctrl+Q')
    exit_action.triggered.connect(self.quit_app)
    
    # Help Menu
    help_menu = menubar.addMenu('Help')
    about_action = help_menu.addAction('About')
    about_action.triggered.connect(self.show_about)

def show_about(self):
    """Zeigt About-Dialog"""
    QMessageBox.about(self, "About", "EiS GUI Übung 02\nVersion 1.0")
```

### 2. Input-Dialog hinzufügen:

```python
from PySide6.QtWidgets import QInputDialog

def get_user_input(self):
    """Fragt Benutzer nach Input"""
    text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
    if ok and text:
        QMessageBox.information(self, "Hello", f"Hello {text}!")
        print(f"User entered: {text}")
```

### 3. Tastatur-Shortcuts:

```python
def keyPressEvent(self, event):
    """Behandelt Tastatureingaben"""
    if event.key() == Qt.Key_Escape:
        self.quit_app()
    elif event.key() == Qt.Key_Space:
        self.print_answer()
    super().keyPressEvent(event)
```

---

## Häufige Fehler und Lösungen

### 1. **Event-Handler vergessen zu verbinden**
```python
# FALSCH:
button = QPushButton("Click me")
# Handler nie verbunden!

# RICHTIG:
button = QPushButton("Click me")
button.clicked.connect(self.handle_click)
```

### 2. **Layout vergessen**
```python
# FALSCH:
widget.addWidget(button)  # Kein Layout!

# RICHTIG:
layout = QVBoxLayout()
layout.addWidget(button)
widget.setLayout(layout)
```

### 3. **App.exec_() vergessen**
```python
# FALSCH:
app = QApplication(sys.argv)
window = MyWindow()
window.show()
# Programm beendet sich sofort!

# RICHTIG:
app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()  # Event-Loop starten!
```

---

## Vorbereitung auf Übungsblatt 03

> [!tip] **Nächste Schritte**: 
> Diese GUI-Grundlagen werden in Übungsblatt 03 erweitert um:
> - **Custom Widgets**: Eigene Zeichenflächen erstellen
> - **Mouse Events**: Mausklicks und -bewegungen verarbeiten
> - **Graphics**: 2D-Grafiken mit QPainter zeichnen
> - **Canvas**: Interaktive Zeichenbereiche programmieren

### Wichtige Konzepte für später:
```python
# Custom Widget für Zeichenfläche
class DrawingWidget(QWidget):
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawLine(0, 0, 100, 100)
        
    def mousePressEvent(self, event):
        print(f"Clicked at: {event.pos()}")
```

---

## Zusammenfassung

> [!summary] **Gelernte Konzepte:**
> - **Event-Driven Programming**: Reaktion auf Benutzereingaben
> - **GUI-Frameworks**: Qt/PySide vs. Swing/AWT
> - **Layout-Management**: Widgets organisieren
> - **Callbacks**: Funktionen als Event-Handler
> - **Cross-Platform**: Plattformunabhängige GUIs

> [!tip] **Für die Klausur merken:**
> - GUIs sind ereignisorientiert (nicht polling-basiert)
> - Event-Loop ist zentral für GUI-Anwendungen
> - Layouts organisieren Widget-Hierarchien
> - Signal/Slot vs. ActionListener Unterschiede
> - Widget-Lifecycle: Erstellen → Verbinden → Anzeigen → Event-Loop

**Weiter zu Übungsblatt 03: Vektorgrafik mit diesem GUI-Grundwissen! 🎨**