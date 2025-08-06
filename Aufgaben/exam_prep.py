from PySide6.QtCore import Qt 
from PySide6.QtGui import QKeySequence, QAction, QImage, QColor, QPainter, QPen
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, 
                              QVBoxLayout, QFrame, QMenuBar, QToolBar,
                              QMessageBox, QFileDialog)
import sys



class MyPaintArea(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent)
        self.setMinimumWidth(640) # Größe des neuen Widgets muss man  
        self.setMinimumHeight(480) # unbedingt selbst einstellen! 
        self.image: QImage = QImage(640, 480, QImage.Format_RGB32) # 640x480pix 
        self.image.fill(QColor(255, 255, 255)) # mit weiß löschen

         # Zeichnen-Zustand
        self.drawing = False
        self.last_point = None
        
        # Stift-Einstellungen
        self.pen_color = QColor(0,0,0)  # Schwarz
        self.pen_width = 3

        # Mouse-Tracking aktivieren für mouseMoveEvent
        self.setMouseTracking(True)

    def paintEvent(self, event): 
        painter: QPainter = QPainter(self)
        painter.drawImage(0,0,self.image)
        painter.end() 
        # hier kann man nun auf das Widget zeichnen 
        # Sinnvoll ist z.B.  
        # painter.drawImage(<x-Koord: int>., <y-Koord: int>., <ein QImage>) 
        # oder zum Testen painter.fillRect(...), drawLine(...) o.ä. 
        # (siehe Doku der Klasse QPainter in PySide6) 
 
    # Diese Methode wird jedes Mal aufgerufen, wenn die Maus über unserem 
    # GUI-Element gedrückt wird 
    def mousePressEvent(self, event): 
        # Mit einer solchen Abfrage kann man überprüfen, welcher Knopf es war 
        if event.button() == Qt.MouseButtons.LeftButton: 
            self.drawing = True
            self.last_point = event.position().toPoint()

    # Hier das gleiche für das Loslassen von Maustasten 
    def mouseReleaseEvent(self, event): 
        if event.button() == Qt.MouseButtons.LeftButton: 
            self.drawing = False
            self.last_point = event.position().toPoint()

    # Und diese Methode wird aufgerufen, falls die Maus über unserem 
    # GUI-Element bewegt wird. Achtung: Man muss natürlich prüfen, ob die 
    # Taste gedrückt wurde... 
    def mouseMoveEvent(self, event): 
        if self.drawing and self.last_point is not None:
            current_point = event.position().toPoint()
            
            # Auf das gespeicherte Bild zeichnen
            painter = QPainter(self.image)
            pen = QPen(self.pen_color, self.pen_width, Qt.PenStyle.SolidLine, 
                      Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin)
            painter.setPen(pen)
            painter.drawLine(self.last_point, current_point)
            painter.end()
            
            # Widget neu zeichnen lassen
            self.update()
            
            # Aktuellen Punkt als letzten Punkt speichern
            self.last_point = current_point


    def set_pen_color(self, color: QColor):
        """Setzt die Stiftfarbe"""
        self.pen_color = color
    
    def set_pen_width(self, width: int):
        """Setzt die Stiftbreite"""
        self.pen_width = width

class MyWindow(QMainWindow):
    
    def __init__(self, parent: QWidget):
        super().__init__(parent)
        self.setWindowTitle("Exam Prep")
        self.setMinimumSize(800, 600)

        
        self.my_frame = QFrame(self)
        self.setCentralWidget(self.my_frame)

        # Layout erstellen
        self.my_layout = QVBoxLayout(self.my_frame)
        self.my_frame.setLayout(self.my_layout)

        # Paint-Area hinzufügen
        self.paint_area = MyPaintArea(self)
        self.my_layout.addWidget(self.paint_area)


        # Menüleiste erstellen
        self.create_menu_bar()
        
        # Toolbar erstellen
        self.create_toolbar()    


    def create_menu_bar(self):
        """Erstellt die Menüleiste mit allen benötigten Menüs"""
        menubar = self.menuBar()
        
        # Datei-Menü
        file_menu = menubar.addMenu("&Datei")
        
        # Öffnen - Action als Member-Variable speichern für Toolbar
        self.open_action = QAction("&Öffnen...", self)
        self.open_action.setShortcut(QKeySequence.StandardKey.Open)  # Ctrl+O
        self.open_action.triggered.connect(self.open_file)
        file_menu.addAction(self.open_action)
        
        # Speichern Als - Action als Member-Variable speichern
        self.save_as_action = QAction("Speichern &Als...", self)
        self.save_as_action.setShortcut(QKeySequence.StandardKey.SaveAs)  # Ctrl+Shift+S
        self.save_as_action.triggered.connect(self.save_file_as)
        file_menu.addAction(self.save_as_action)
        
        # Trenner
        file_menu.addSeparator()
        
        # Zusätzliche Aktionen für Zeichenfläche
        self.clear_action = QAction("&Löschen", self)
        self.clear_action.setShortcut(QKeySequence("Ctrl+L"))
        self.clear_action.triggered.connect(self.clear_canvas)
        file_menu.addAction(self.clear_action)
        
        # Beenden - Action als Member-Variable speichern
        self.quit_action = QAction("&Beenden", self)
        self.quit_action.setShortcut(QKeySequence.StandardKey.Quit)  # Ctrl+Q
        self.quit_action.triggered.connect(self.quit_app)
        file_menu.addAction(self.quit_action)
        
        # Hilfe-Menü
        help_menu = menubar.addMenu("&Hilfe")
        
        # Informationen - Action als Member-Variable speichern
        self.info_action = QAction("&Informationen...", self)
        self.info_action.setShortcut(QKeySequence("F1"))
        self.info_action.triggered.connect(self.show_info)
        help_menu.addAction(self.info_action)

        # Trenner
        file_menu.addSeparator()

        pen_menu = menubar.addMenu("&Stifte")
        
        self.pen_action = QAction("&Stift Settings...")
        self.pen_action.triggered.connect(self.pen_setting)
        pen_menu.addAction(self.pen_action)



    def create_toolbar(self):
        """Erstellt eine Toolbar mit den gleichen Aktionen wie das Menü"""
        # Haupttoolbar erstellen
        self.main_toolbar = self.addToolBar("Hauptwerkzeuge")
        
        # Die gleichen Actions zur Toolbar hinzufügen
        self.main_toolbar.addAction(self.open_action)
        self.main_toolbar.addAction(self.save_as_action)
        self.main_toolbar.addAction(self.clear_action)
        
        # Separator hinzufügen
        self.main_toolbar.addSeparator()
        
        self.main_toolbar.addAction(self.info_action)
        self.main_toolbar.addAction(self.quit_action)
        
        # Optional: Toolbar-Text für bessere Lesbarkeit
        self.open_action.setText("Öffnen")
        self.save_as_action.setText("Speichern Als")
        self.clear_action.setText("Löschen")
        self.quit_action.setText("Beenden")
        self.info_action.setText("Info")

    def open_file(self):
        pass


    def pen_setting(self):

        QMessageBox.question
        pass

    def save_file_as(self):
        pass
    
    def quit_app(self):
        # Fenster öffnen und wenn ich Bestätige soll er schließen
        reply = QMessageBox.question(
            self, 
            "Beenden bestätigen", 
            "Möchten Sie die Anwendung wirklich beenden?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No  # Standard-Button
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            self.close()
        #self.close()
    
    def clear_canvas(self):
        pass

    def show_info(self):
        QMessageBox.question(
            self,
            "Informationen",
            "Übungsblatt 02, EIS SoSem 2025 Paul Baselt",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        pass


# our main program starts here, Python-style 
if __name__ == "__main__": 
    # create an application object (needs cmd-line arguments) 
    app: QApplication = QApplication(sys.argv) 
 
    # Create the main window. 
    main_window: MyWindow = MyWindow(None) 
    main_window.show() 
 
    # Start the event loop. 
    # Ends only after closing the main window 
    app.exec()