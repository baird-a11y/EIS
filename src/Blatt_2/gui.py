#!/usr/bin/env python3
"""
Übungsblatt 02 - GUI mit Menüleiste
EIS SoSem 2025
"""

from PySide6.QtCore import Qt 
from PySide6.QtGui import QKeySequence, QAction, QImage, QColor, QPainter, QPen
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, 
                              QVBoxLayout, QFrame, QMenuBar, QToolBar,
                              QMessageBox, QFileDialog)
import sys


class MyPaintArea(QWidget):
    """Widget für Zeichenfunktionen mit Maus-Unterstützung"""
    
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        
        # Mindestgröße festlegen
        self.setMinimumSize(640, 480)
        
        # Bild erstellen und mit weiß füllen
        self.image = QImage(640, 480, QImage.Format.Format_RGB32)
        self.image.fill(QColor(255, 255, 255))  # Weiß
        
        # Zeichnen-Zustand
        self.drawing = False
        self.last_point = None
        
        # Stift-Einstellungen
        self.pen_color = QColor(0, 0, 0)  # Schwarz
        self.pen_width = 3
        
        # Mouse-Tracking aktivieren für mouseMoveEvent
        self.setMouseTracking(True)
    
    def paintEvent(self, event):
        """Wird aufgerufen wenn das Widget neu gezeichnet werden muss"""
        painter = QPainter(self)
        
        # Das gespeicherte Bild auf das Widget zeichnen
        painter.drawImage(0, 0, self.image)
        
        painter.end()
    
    def mousePressEvent(self, event):
        """Wird aufgerufen wenn eine Maustaste gedrückt wird"""
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = True
            self.last_point = event.position().toPoint()
    
    def mouseReleaseEvent(self, event):
        """Wird aufgerufen wenn eine Maustaste losgelassen wird"""
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = False
            self.last_point = None
    
    def mouseMoveEvent(self, event):
        """Wird aufgerufen wenn die Maus bewegt wird"""
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
    
    def clear_image(self):
        """Löscht das Bild (füllt es mit weiß)"""
        self.image.fill(QColor(255, 255, 255))
        self.update()
    
    def save_image(self, file_path: str) -> bool:
        """Speichert das aktuelle Bild in eine Datei"""
        return self.image.save(file_path)
    
    def load_image(self, new_image: QImage):
        """Lädt ein neues Bild in die Zeichenfläche"""
        # Skaliere das Bild auf die Größe der Zeichenfläche
        if new_image.size() != self.image.size():
            new_image = new_image.scaled(self.image.size(), Qt.AspectRatioMode.KeepAspectRatio, 
                                       Qt.TransformationMode.SmoothTransformation)
        
        # Erstelle ein neues weißes Bild in der richtigen Größe
        self.image.fill(QColor(255, 255, 255))
        
        # Zeichne das geladene Bild zentriert darauf
        painter = QPainter(self.image)
        x = (self.image.width() - new_image.width()) // 2
        y = (self.image.height() - new_image.height()) // 2
        painter.drawImage(x, y, new_image)
        painter.end()
        
        # Widget neu zeichnen
        self.update()
    
    def set_pen_color(self, color: QColor):
        """Setzt die Stiftfarbe"""
        self.pen_color = color
    
    def set_pen_width(self, width: int):
        """Setzt die Stiftbreite"""
        self.pen_width = width


class MyWindow(QMainWindow):
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
                self.paint_area.load_image(loaded_image)
                print(f"Bild geladen: {file_path}")
                
            except Exception as e:
                QMessageBox.critical(self, "Fehler", f"Fehler beim Laden der Datei:\n{str(e)}")
    
    def save_file_as(self):
        """Speichern Als Dialog - speichert das gezeichnete Bild als PNG"""
        file_path, _ = QFileDialog.getSaveFileName(
            self, 
            "Bild speichern", 
            "zeichnung.png", 
            "PNG Files (*.png);;JPEG Files (*.jpg);;Alle Dateien (*.*)"
        )
        
        if file_path:
            try:
                # Stelle sicher, dass die Datei eine .png Endung hat
                if not file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                    file_path += '.png'
                
                # Bild speichern
                success = self.paint_area.save_image(file_path)
                
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
            self.paint_area.clear_image()
    
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


def main():
    """Hauptprogramm"""
    app = QApplication(sys.argv)
    
    # Hauptfenster erstellen und anzeigen
    main_window = MyWindow()
    main_window.show()
    
    # Event-Loop starten
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())