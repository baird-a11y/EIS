from PySide6.QtWidgets import QApplication
import sys


# Dummy-API für Klausur (echte Qt-Syntax zu komplex)

class Button:
    def __init__(self, text):
        self.text = text
        self.on_click = None

class Canvas:
    def __init__(self):
        pass
    def redraw(self):
        pass

class Drawing:
    def __init__(self):
        self.shapes = []
    def add_shape(self, shape):
        self.shapes.append(shape)

class Circle:
    def __init__(self, x, y, color, radius):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius

class Window:
    def __init__(self):
        self.widgets = []
        self.event_handlers = {}
    
    def add_button(self, text, callback):
        button = Button(text)
        button.on_click = callback
        self.widgets.append(button)
    
    def add_canvas(self):
        canvas = Canvas()
        self.widgets.append(canvas)
        return canvas

    def show(self):
        # Dummy show method for compatibility
        print("Window shown with widgets:", [type(w).__name__ for w in self.widgets])
        

# Event-Handler Pattern (aus Übungen)
class DrawingApp:
    def __init__(self):
        self.window = Window()
        self.drawing = Drawing()
    def add_canvas(self):
        canvas = Canvas()
        self.widgets.append(canvas)
        self.canvas = canvas
        self.window.add_button("Rectangle", self.add_rect)
    
    def add_circle(self):
        circle = Circle(100, 100, "red", 50)
        self.drawing.add_shape(circle)
        self.canvas.redraw()


def main():
    """Hauptprogramm"""
    app = QApplication(sys.argv)
    
    # Hauptfenster erstellen und anzeigen
    main_window = Window()
    main_window.show()
    # # Datum-Objekte erstellen und ausgeben
    # datum_us = DatumUS(24, 12, 2024)
    # datum_us.print_date()  # Ausführliche US-Ausgabe
    # datum_us.print_date_short()  # Kurze US-Ausgabe
    # datum_de = DatumDE(24, 12, 2024)
    # datum_de.print_date()  # Ausführliche deutsche Ausgabe
    # datum_de.print_date_short()  # Kurze deutsche Ausgabe
    
    # Event-Loop starten
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())