
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QMessageBox, QPushButton,QFrame, QMenuBar, QToolBar
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QColor, QAction, QKeySequence
from datetime import datetime

class MainWindow(QMainWindow):
    
    def show_dialog(self): 
        QMessageBox.question(self,"Informationen","Übungsblatt 02, EIS SoSem 2025, Paul",QMessageBox.Ok)

    def show_time(self): 
        print(datetime.now())

    def print_to_console(self): 
        print("42")

    def __init__(self):
        super().__init__()
        self.setWindowTitle("EiS - Vektorgrafik")
        self.setGeometry(100,100, 800, 600)
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
        self.btn_dialog = QPushButton("Hello World") 
        # connect button to method of self object 
        self.btn_dialog.clicked.connect(self.show_dialog) 
        # add the button to the UI via the layout object 
        self.my_layout.addWidget(self.btn_dialog)

        # create a button, remember in a member variable 
        self.btn_dialog = QPushButton("Show Time") 
        # connect button to method of self object 
        self.btn_dialog.clicked.connect(self.show_time) 
        # add the button to the UI via the layout object 
        self.my_layout.addWidget(self.btn_dialog)

        # create a button, remember in a member variable 
        self.btn_dialog = QPushButton("42") 
        # connect button to method of self object 
        self.btn_dialog.clicked.connect(self.print_to_console) 
        # add the button to the UI via the layout object 
        self.my_layout.addWidget(self.btn_dialog)
        
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
        file_menu.addAction(self.open_action)

        self.save_action = QAction("&Speichen Als")
        self.save_action.setShortcut(QKeySequence.StandardKey.SaveAs)
        file_menu.addAction(self.save_action)

        self.close_action = QAction("&Schließen")
        # self.close_action.setShortcut(QKeySequence.StandardKey.Close)
        self.close_action.triggered.connect(self.quit_action)  # Verbindung zur Schließen-Methode
        file_menu.addAction(self.close_action)

        # Trenner
        file_menu.addSeparator()

        file_menu = menubar.addMenu("&Hilfe")

        self.help_action = QAction("&Information")
        self.help_action.setShortcut(QKeySequence.StandardKey.HelpContents)
        self.help_action.triggered.connect(self.show_dialog)
        file_menu.addAction(self.help_action)


    
    def quit_action(self):
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

    def open_action(self):
        pass

    def create_toolbar(self):
        self.main_toolbar = self.addToolBar("ToolBar Test")

        # Öffnen-Action zur Toolbar hinzufügen
        self.main_toolbar.addAction(self.open_action)
        self.main_toolbar.addAction(self.save_action)
        self.main_toolbar.addAction(self.close_action)
        
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
