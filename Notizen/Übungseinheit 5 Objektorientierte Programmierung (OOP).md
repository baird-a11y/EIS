### **Theorie-Aufgabe 11** (6 Punkte)

Erkläre die drei Hauptkonzepte der OOP: 
a) Was bedeutet **Kapselung** (Encapsulation)? 
Das Sachen nur innerhalb einer Klasse aufrufbar sind und darüber hinaus nicht


**Kapselung** - Teilweise richtig, aber zu kurz. Besser: "Daten und Methoden werden in einer Klasse gebündelt und der Zugriff von außen kontrolliert (private/protected/public)"

b) Was bedeutet **Vererbung** (Inheritance)? 
Das eine Unterklasse Eigenschaften und Funktionen der Oberklasse mit übergeben bekommt.
Bsp.
Klasse Lebewesen hat ein Alter, Größe etc.
Subklasse Mensch hat dann noch zusätzlich Geschlächt 
c) Was bedeutet **Polymorphie**?
Unvollständig! Richtig: "Objekte verschiedener Klassen können über eine gemeinsame Schnittstelle angesprochen werden. Gleiche Methode, unterschiedliche Implementierung."
### **Praxis-Aufgabe 11** (12 Punkte)

Implementiere folgende Klassenhierarchie in Python:

```python
# Basisklasse
class Vehicle:
    def __init__(self, brand: str, year: int):
        
		self.brand = brand
		self.year = year

        pass
    
    def get_info(self) -> str:
        return self.brand
        pass

# Unterklasse
class Car(Vehicle):
    def __init__(self, brand: str, year: int, doors: int):
        # Nutze super() für Basisklasse
        # Speichere doors zusätzlich
        pass
    
    def get_info(self) -> str:
        # Erweitere die Basisklassen-Info um "Doors: Z"
        pass


class Vehicle:

    def __init__(self, brand: str, year: int):

        self.brand = brand

        self.year = year

  

    def get_info(self) -> str:

        return f"Brand: {self.brand}, Year: {self.year}"

  

# # Unterklasse

class Car(Vehicle):

     def __init__(self, brand: str, year: int, doors: int):

         # Nutze super() für Basisklasse

         # Speichere doors zusätzlich

            super().__init__(brand, year)

            self.doors = doors

  

     def get_info(self) -> str:

         # Erweitere die Basisklassen-Info um "Doors: Z"

            base_info = super().get_info()

            return f"{base_info} Doors: {self.doors}"
```

### **Theorie-Aufgabe 12** (5 Punkte)

Was ist der Unterschied zwischen:

- **Composition** ("has-a" Beziehung)
- **Inheritance** ("is-a" Beziehung)

Bei Ineritance kann ich nur von oben nach unten weiter geben aber nicht umgekehrt.
Sie Aufgabe zu vor. Car hat ein Beziehung zu Vehicle, kann aber die Eigenschaften in Vehicle nicht ändern sondern nur auslesen


Richtige Erklärung:

- **Inheritance ("is-a")**: Auto IST EIN Fahrzeug
- **Composition ("has-a")**: Auto HAT EINEN Motor

Beispiel Composition:

python

```python
class Engine:
    pass

class Car:
    def __init__(self):
        self.engine = Engine()  # Car HAS-A Engine
```



### **Praxis-Aufgabe 12** (10 Punkte)

Übersetze diese Python-Klasse nach Scala:

```python
class Counter:
    def __init__(self, initial: int = 0):
        self._count = initial
    
    def increment(self) -> None:
        self._count += 1
    
    def get_value(self) -> int:
        return self._count
```

### **Theorie-Aufgabe 13** (8 Punkte)

Zeichne ein UML-Klassendiagramm für folgende Beschreibung:

- Klasse `Person` mit Attribut `name: String`
- Klasse `Student` erbt von `Person`, hat zusätzlich `matrikelnummer: int`
- Klasse `Kurs` hat Attribute `titel: String` und `credits: int`
- Ein `Student` kann 0 bis viele `Kurse` belegen (Assoziation)

### **Praxis-Aufgabe 13** (15 Punkte)

Implementiere eine abstrakte Klasse mit konkreten Unterklassen:

```python
# Implementiere eine abstrakte Klasse mit konkreten Unterklassen:

from abc import ABC, abstractmethod

from typing import List

import math

  

class Shape(ABC):

    @abstractmethod

    def area(self) -> float:

        pass

    @abstractmethod

    def perimeter(self) -> float:

        pass

  

# Implementiere Rectangle und Circle

class Rectangle(Shape):

    def __init__(self, width: float, height: float):

        # Deine Implementation

        self.width = width

        self.height = height

    def area(self) -> float:

        # Berechne Fläche des Rechtecks

        return self.width * self.height

    def perimeter(self) -> float:

        # Berechne Umfang des Rechtecks

        return 2 * (self.width + self.height)

  
  
  

class Circle(Shape):

    def __init__(self, radius: float):

        # Deine Implementation (nutze math.pi)

        self.radius = radius

    def area(self) -> float:

        # Berechne Fläche des Kreises

        return math.pi * (self.radius ** 2)

    def perimeter(self) -> float:

        # Berechne Umfang des Kreises

        return 2 * math.pi * self.radius

  

# Teste Polymorphie

def total_area(shapes: List[Shape]) -> float:

    # Berechne Gesamtfläche aller Shapes

    total = 0.0

    for shape in shapes:

        total += shape.area()

    return total
```

### **Bonus-Aufgabe** (10 Punkte)

Erkläre, warum dieser Code problematisch ist:

```python
class Bird:
    def fly(self):
        print("Flying high!")

class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins can't fly!")
```

Was verletzt das? Wie würdest du es besser machen?

Bei beiden fehlt der Konstruktor und ich würde das wahrscheinlich eher so schreiben

also 
```python
class Bird:

    def __init__(self, flying: bool):

        self.flying = True

    def fly(self) -> bool:

        if self.flying==True:

            return("Flying high!")

        else:

            print("Cannot Fly")

  

class Penguin(Bird):

    def __init__(self,flying: bool):

        super().__init__(flying)

    def fly(self):

        return("Penguins can't fly!")
```

---

**OOP-Merksätze für die Klausur:**

- **super()** ruft Basisklassen-Methoden auf
- **@abstractmethod** macht Methoden abstrakt
- **"is-a"** → Vererbung, **"has-a"** → Komposition
- In Scala: **extends** für Vererbung, **override** für Überschreibung
- Python: Duck Typing, Scala: Statisches Subtyping

Bearbeite die Aufgaben und achte besonders auf:

- Korrekte Verwendung von `super()`
- Type Annotations bei allen Methoden
- Saubere Vererbungshierarchien