import sys
import socket

from PySide6.QtCore import Qt 
from PySide6.QtGui import QKeySequence, QAction, QImage, QColor, QPainter, QPen
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, 
                              QVBoxLayout, QFrame, QMenuBar, QToolBar,
                              QMessageBox, QFileDialog, QLabel, QLineEdit, QPushButton, QTextEdit)


class FileRequestClient(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Minimaler Webbrowser')
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        self.label = QLabel('Welche Datei möchtest du anfordern?', self)
        layout.addWidget(self.label)

        self.filename_input = QLineEdit(self)
        layout.addWidget(self.filename_input)

        self.request_button = QPushButton('Anfordern', self)
        self.request_button.clicked.connect(self.send_request)
        layout.addWidget(self.request_button)

        self.text_display = QTextEdit(self)
        self.text_display.setReadOnly(True)
        layout.addWidget(self.text_display)

        self.setLayout(layout)

    def send_request(self):
        filename = self.filename_input.text().strip()
        if not filename:
            self.text_display.setText('Bitte gib einen Dateinamen ein.')
            return

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect(('127.0.0.1', 41337))
                sock.sendall(filename.encode("utf-8"))
                data = sock.recv(4096)
                content = data.decode("utf-8")
                self.text_display.setText(content)
        except Exception as e:
            self.text_display.setText(f'Fehler: {str(e)}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    client = FileRequestClient()
    client.show()
    sys.exit(app.exec_())