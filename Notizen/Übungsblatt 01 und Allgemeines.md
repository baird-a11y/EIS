# EiS Prüfungsvorbereitung - Komplett
**Einführung in die Softwareentwicklung (EiS) - SoSem 2025**

> [!summary] **Klausur-Kerninfos**
> - **Datum**: Do, 07. August 2025 09:00-12:00, Hörsaal RW1
> - **Format**: 7 Aufgaben, 100 Punkte, 3 Stunden
> - **Hilfsmittel**: 2 handgeschriebene A4-Blätter
> - **Bestehen**: Ab 50 Punkten
> - **Programmiersprachen**: Wahlweise Python oder Scala
> - **Wichtig**: Klausur orientiert sich eng an Übungen!

---

## Übungsblatt 01 - Musterlösung mit Erklärungen

### Aufgabe 1: Installation der Programmiersprachen (unbewertet)

> [!info] **Warum diese Aufgabe wichtig ist:**
> - **Lernziel**: Arbeitsumgebung für den gesamten Kurs vorbereiten
> - **Praxis**: Erfahrung mit verschiedenen Compiler/Interpreter-Systemen
> - **Vergleich**: Unterschiede zwischen kompilierten und interpretierten Sprachen verstehen

#### Installationsreihenfolge und Tipps

##### 1. C/C++ (gcc/g++)
```bash
sudo apt update
sudo apt install build-essential
```

> [!tip] **Warum zuerst C++?**
> - Andere Sprachen (Java, Scala) benötigen oft C-Bibliotheken
> - Grundlage für das Verständnis von Low-Level-Programmierung
> - Wichtig für Performance-kritische Teile (siehe spätere Übungen)

##### 2. Python 3 + MyPy
```bash
sudo apt install python3-dev
sudo apt install mypy
```

> [!tip] **Warum MyPy?**
> - Statische Typisierung für Python
> - Hilft beim Finden von Fehlern vor der Ausführung
> - Brücke zwischen dynamischer und statischer Typisierung

##### 3. Java (JRE + JDK)
```bash
sudo apt install default-jre default-jdk
```

> [!tip] **Warum Java?**
> - Grundlage für Scala
> - Verständnis der Java Virtual Machine (JVM)
> - Wichtig für späteren Vergleich mit C++ (Memory Management)

##### 4. Scala 3
```bash
# Besondere Installation über coursier
curl -fL https://github.com/coursier/coursier/releases/latest/download/cs-x86_64-pc-linux.gz | gzip -d > cs
chmod +x cs
./cs setup
```

> [!tip] **Warum Scala zuletzt?**
> - Benötigt Java als Grundlage
> - Modernste Sprache im Kurs
> - Vereint funktionale und objektorientierte Programmierung

---

### Aufgabe 2: Einfache Programme (70 Punkte)

#### Teil a) Count-Down in allen Sprachen (unbewertet)

> [!note] **Lernziel**: Syntax-Vergleich zwischen den Sprachen

##### Python
```python
n = 10
for i in range(n, 0, -1):
    print(i)
    if i == 8:
        print("ignition sequence start")
print("liftoff!")
```

##### C++
```cpp
#include <iostream>
using namespace std;

int main() {
    for (int i = 10; i >= 1; i--) {
        cout << i << endl;
        if (i == 8) {
            cout << "ignition sequence start" << endl;
        }
    }
    cout << "liftoff!" << endl;
    return 0;
}
```

##### Java
```java
public class CountDown {
    public static void main(String[] args) {
        for (int i = 10; i >= 1; i--) {
            System.out.println(i);
            if (i == 8) {
                System.out.println("ignition sequence start");
            }
        }
        System.out.println("liftoff!");
    }
}
```

##### Scala
```scala
object CountDown {
    def main(args: Array[String]): Unit = {
        for (i <- 10 to 1 by -1) {
            println(i)
            if (i == 8) {
                println("ignition sequence start")
            }
        }
        println("liftoff!")
    }
}
```

#### Teil b) Primzahltest (50 Punkte)

> [!note] **Lernziel**: Algorithmus-Implementation und Performance-Vergleich

##### Algorithmus-Erklärung:
```
Eingabe: Zahl n
Für jeden möglichen Teiler t von 2 bis √n:
    Wenn n % t == 0:
        return false (keine Primzahl)
return true (ist Primzahl)
```

> [!important] **Testzahl**: 10.007 × 100.003 = 1.000.700.021

##### Python (mit Type Hints)
```python
import math
import time

def is_prime(n: int) -> bool:
    """
    Prüft, ob eine Zahl eine Primzahl ist.
    Verwendet naive Methode: Teste alle Teiler bis √n
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Teste ungerade Teiler von 3 bis √n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    test_number = 10007 * 100003  # 1000700021
    
    start_time = time.time()
    result = is_prime(test_number)
    end_time = time.time()
    
    print(f"Zahl: {test_number}")
    print(f"Ist Primzahl: {result}")
    print(f"Laufzeit: {(end_time - start_time) * 1000:.2f} ms")

if __name__ == "__main__":
    main()
```

##### C++
```cpp
#include <iostream>
#include <cmath>
#include <chrono>

bool is_prime(long long n) {
    if (n < 2) return false;
    if (n == 2) return true;
    if (n % 2 == 0) return false;
    
    // Teste ungerade Teiler von 3 bis √n
    for (long long i = 3; i <= sqrt(n); i += 2) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    long long test_number = 10007LL * 100003LL; // 1000700021
    
    auto start = std::chrono::high_resolution_clock::now();
    bool result = is_prime(test_number);
    auto end = std::chrono::high_resolution_clock::now();
    
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    
    std::cout << "Zahl: " << test_number << std::endl;
    std::cout << "Ist Primzahl: " << (result ? "true" : "false") << std::endl;
    std::cout << "Laufzeit: " << duration.count() / 1000.0 << " ms" << std::endl;
    
    return 0;
}
```

##### Java
```java
public class PrimeTest {
    
    public static boolean isPrime(long n) {
        if (n < 2) return false;
        if (n == 2) return true;
        if (n % 2 == 0) return false;
        
        // Teste ungerade Teiler von 3 bis √n
        for (long i = 3; i <= Math.sqrt(n); i += 2) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
    
    public static void main(String[] args) {
        long testNumber = 10007L * 100003L; // 1000700021
        
        long startTime = System.currentTimeMillis();
        boolean result = isPrime(testNumber);
        long endTime = System.currentTimeMillis();
        
        System.out.println("Zahl: " + testNumber);
        System.out.println("Ist Primzahl: " + result);
        System.out.println("Laufzeit: " + (endTime - startTime) + " ms");
    }
}
```

##### Scala
```scala
import scala.math.sqrt

object PrimeTest {
    
    def isPrime(n: Long): Boolean = {
        if (n < 2) false
        else if (n == 2) true
        else if (n % 2 == 0) false
        else {
            // Teste ungerade Teiler von 3 bis √n
            val limit = sqrt(n).toInt
            !(3 to limit by 2).exists(n % _ == 0)
        }
    }
    
    def main(args: Array[String]): Unit = {
        val testNumber: Long = 10007L * 100003L // 1000700021
        
        val startTime = System.currentTimeMillis()
        val result = isPrime(testNumber)
        val endTime = System.currentTimeMillis()
        
        println(s"Zahl: $testNumber")
        println(s"Ist Primzahl: $result")
        println(s"Laufzeit: ${endTime - startTime} ms")
    }
}
```

#### Teil c) Rekursive Implementierung (20 Punkte)

> [!note] **Lernziel**: Rekursion verstehen und ihre Grenzen erkennen

##### Python (rekursiv)
```python
import math

def is_prime_recursive(n: int, divisor: int = 3) -> bool:
    """
    Rekursive Primzahlprüfung
    ACHTUNG: Kann bei großen Zahlen zu Stack Overflow führen!
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Basisfall: Alle möglichen Teiler durchprobiert
    if divisor > math.sqrt(n):
        return True
    
    # Rekursiver Fall: Prüfe aktuellen Teiler
    if n % divisor == 0:
        return False
    
    # Rekursiver Aufruf mit nächstem ungeraden Teiler
    return is_prime_recursive(n, divisor + 2)

def main():
    # Teste mit kleiner Zahl
    small_test = 21
    print(f"21 ist Primzahl: {is_prime_recursive(small_test)}")
    
    # Teste mit großer Zahl (kann Stack Overflow verursachen!)
    try:
        large_test = 10007 * 100003
        result = is_prime_recursive(large_test)
        print(f"{large_test} ist Primzahl: {result}")
    except RecursionError:
        print("Stack Overflow! Rekursion zu tief für große Zahlen.")

if __name__ == "__main__":
    main()
```

##### Erwartete Beobachtungen:
- **Kleine Zahlen (21)**: Funktioniert perfekt
- **Große Zahlen**: Stack Overflow in Python/Java/Scala
- **C++**: Eventuell größere Zahlen möglich (größerer Stack)
- **Performance**: Rekursion ist langsamer durch Funktionsaufrufe

---

## Vorlesung 02: Grundlagen

### Veränderlichkeit vs. Unveränderlichkeit

> [!important] **Klausurrelevanz**: Fundamentales Konzept in allen Paradigmen

#### Definitionen:
- **Veränderlich (Mutable)**: Objekte können nach der Erzeugung geändert werden
- **Unveränderlich (Immutable)**: Objekte sind nach der Erzeugung unveränderbar

#### Beispiele:
```scala
// Veränderlich
var x: Int = 5
x = 10  // Erlaubt

// Unveränderlich
val y: Int = 5
y = 10  // Compiler-Fehler!
```

> [!tip] **Prüfungsfrage**: Warum ist Unveränderlichkeit in der funktionalen Programmierung wichtig?
> **Antwort**: Keine Seiteneffekte, Thread-Sicherheit, einfacheres Debugging

### Klassen und Methoden

#### Klassen-Grundlagen:
```scala
class Rational(n: Int, d: Int) {  // Primärkonstruktor
    private val numerator: Int = n
    private val denominator: Int = d
    
    // Alternative Konstruktoren
    def this(n: Int) = this(n, 1)
    
    // Methoden
    def add(other: Rational): Rational = {
        new Rational(
            numerator * other.denominator + other.numerator * denominator,
            denominator * other.denominator
        )
    }
}
```

#### Kapselung und Zugriffskontrolle:
- **`private`**: Nur in der Klasse selbst sichtbar
- **`protected`**: In Klasse und Unterklassen sichtbar
- **`public`**: Überall sichtbar (Standard)

> [!tip] **Prüfungsfrage**: Was bedeutet Kapselung in der objektorientierten Programmierung?
> **Antwort**: Verbergen der internen Implementierung, Kontrolle über Zugriff auf Daten

### Methodenüberladung

```scala
class Calculator {
    def add(x: Int, y: Int): Int = x + y
    def add(x: Double, y: Double): Double = x + y
    def add(x: String, y: String): String = x + y
}
```

> [!note] **Wichtig**: Überladung basiert auf Parametertypen, nicht auf Rückgabetyp

### Objektreferenzen

```scala
val obj1 = new Rational(3, 4)
val obj2 = obj1  // obj2 referenziert dasselbe Objekt wie obj1
```

> [!warning] **Klausur-Fallstrick**: Unterschied zwischen Referenz-Kopie und Objekt-Kopie

---

## Übungsblatt-Übersicht mit Prüfungsfokus

### Übungsblatt 02: GUI-Programmierung (1 Woche)
> [!important] **Klausurrelevanz**: Ereignisorientierte Programmierung, GUI-Patterns

#### Prüfungsfragen-Training:
- **Warum sind GUIs ereignisorientiert?**
- **Callback-Funktionen vs. Polling erklären**
- **Qt vs. Swing - Architektur-Unterschiede**

#### Erwartete Klausuraufgaben:
- Widget-Hierarchie zeichnen
- Event-Handler-Code schreiben
- GUI-Designprinzipien erklären

### Übungsblatt 03: Vektorgraphik prozedural (2 Wochen)
> [!important] **Klausurrelevanz**: Prozedurale Programmierung, Datenstrukturen

#### Prüfungsfragen-Training:
- **Warum ist prozedurale Programmierung für Grafik geeignet?**
- **Abstrakte Datentypen vs. Primitive Datentypen**
- **Modularisierung - Vorteile und Nachteile**

#### Erwartete Klausuraufgaben:
- Geometric Primitives implementieren
- Koordinatensysteme transformieren
- Algorithmus für Collision Detection

### Übungsblatt 04: Vektorgraphik OOP (2 Wochen)
> [!important] **Klausurrelevanz**: OOP-Kernkonzepte, Vererbung, Polymorphismus

#### Prüfungsfragen-Training:
- **Wann ist OOP besser als prozedural?**
- **Virtual Methods vs. Function Pointers**
- **Kapselung, Vererbung, Polymorphismus praktisch anwenden**

#### Erwartete Klausuraufgaben:
- Klassenhierarchie entwerfen
- `draw()` Pattern implementieren
- Polymorphismus-Beispiele erklären

### Übungsblatt 05: Funktionale Programmierung (2 Wochen)
> [!important] **Klausurrelevanz**: Expression Problem, Funktionszeiger, Immutability

#### Prüfungsfragen-Training:
- **Expression Problem erklären**
- **Funktional vs. OOP - Vor-/Nachteile**
- **Lazy Evaluation - Anwendungsbeispiele**

#### Erwartete Klausuraufgaben:
- Pattern Matching implementieren
- Funktionszeiger verwenden
- Map/Filter/Reduce Operationen

### Übungsblatt 06: Hardwarenahe Programmierung (1 Woche)
> [!important] **Klausurrelevanz**: Zeiger, Speicherverwaltung, Performance

#### Prüfungsfragen-Training:
- **C++ Zeiger vs. Python Referenzen - Sicherheit**
- **Stack vs. Heap - Wann was verwenden?**
- **Memory Leaks vermeiden**

#### Erwartete Klausuraufgaben:
- Zeiger-Arithmetik
- Manual Memory Management
- Performance-Optimierungen

### Übungsblatt 07: Client-Server (2 Wochen)
> [!important] **Klausurrelevanz**: Nebenläufigkeit, Architekturen, Netzwerk

#### Prüfungsfragen-Training:
- **Server-Pattern vs. Microservices**
- **TCP vs. UDP - Anwendungsgebiete**
- **Concurrency Problems (Race Conditions)**

#### Erwartete Klausuraufgaben:
- Socket-Programmierung
- HTTP-Protocol implementieren
- Nebenläufigkeits-Konzepte

---

## Wichtige Erkenntnisse und Tipps

### 1. **Performance-Unterschiede verstehen**
```
Erwartete Reihenfolge (schnell → langsam):
C++ > Java ≈ Scala >> Python
```

> [!tip] **Warum?**
> - **C++**: Direkte Maschinencode-Kompilierung
> - **Java/Scala**: JVM-Optimierung, aber Bytecode-Interpretation
> - **Python**: Interpretiert, dynamische Typisierung

### 2. **Programmierparadigmen-Vergleich**

| Paradigma | Stärken | Schwächen | Anwendung |
|-----------|---------|-----------|-----------|
| **Prozedural** | Einfach, direkt | Schwer erweiterbar | Algorithmen, Grafik |
| **OOP** | Modular, erweiterbar | Komplexer | GUI, große Systeme |
| **Funktional** | Keine Seiteneffekte | Lernkurve | Datenverarbeitung |

### 3. **Speicher-Management**
- **C++**: Manuell (new/delete) → Kontrolle, aber fehleranfällig
- **Java/Scala/Python**: Garbage Collection → Sicher, aber weniger Kontrolle

### 4. **Compilation vs. Interpretation**
- **Kompiliert**: C++, Java, Scala → Schneller zur Laufzeit
- **Interpretiert**: Python → Langsamer, aber flexibler

### 5. **Rekursion vs. Iteration**
- **Rekursion**: Elegant, aber Stack-begrenzt
- **Iteration**: Effizienter, unbegrenzt

---

## Prüfungsoptimierte Lernstrategie

### **Für jedes Übungsblatt zusätzlich bearbeiten:**

#### **📖 Theorie-Vertiefung:**
- **Paradigmen-Vergleich**: Warum ist [Paradigma] für [Problem] geeignet?
- **Architektur-Patterns**: Welche Patterns werden verwendet und warum?
- **Sprachen-Konzepte**: Wie löst [Sprache] [Problem] anders als [andere Sprache]?

#### **🔍 Prüfungsfragen entwickeln:**
- **Vor-/Nachteile**: Jedes Konzept hat Pros und Cons
- **Anwendungsbeispiele**: Wo wird X in der Praxis eingesetzt?
- **Fehlerquellen**: Was kann schiefgehen und wie vermeidet man es?

#### **💡 Transferaufgaben:**
- **Umwandlungen**: Prozedural → OOP → Funktional
- **Optimierungen**: "Wie würdest du das effizienter machen?"
- **Erweiterungen**: "Wie fügt man Feature X hinzu?"

---

## Klausur-Cheatsheet Vorbereitung

### **Blatt 1: Syntax & Grundlagen**
```
Python:
- for i in range(10): print(i)
- def func(x: int) -> int: return x * 2
- class MyClass: pass

Scala:
- for (i <- 1 to 10) println(i)
- def func(x: Int): Int = x * 2
- class MyClass(x: Int)

Java:
- for (int i = 0; i < 10; i++) System.out.println(i);
- public static int func(int x) { return x * 2; }
- public class MyClass { }

C++:
- for (int i = 0; i < 10; i++) cout << i;
- int func(int x) { return x * 2; }
- class MyClass { public: int x; };
```

### **Blatt 2: Patterns & Architekturen**
```
Observer Pattern:
- Subject verwaltet Liste von Observers
- notify() ruft update() auf allen Observers auf

Factory Pattern:
- Objekterzeugung abstrahiert
- Verschiedene Implementierungen möglich

MVC Pattern:
- Model: Daten
- View: Darstellung
- Controller: Logik
```

---

## Häufige Klausurfehler vermeiden

### **1. Syntax-Fehler**
```scala
// FALSCH:
val x: Int = "Hello"  // Typfehler

// RICHTIG:
val x: String = "Hello"
```

### **2. Konzeptfehler**
```python
# FALSCH: Objektreferenzen verwechseln
list1 = [1, 2, 3]
list2 = list1  # Referenz-Kopie, nicht Objekt-Kopie!

# RICHTIG:
list2 = list1.copy()  # Echte Kopie
```

### **3. Paradigmen-Vermischung**
```scala
// FALSCH: Imperativer Stil in funktionaler Programmierung
var sum = 0
for (i <- 1 to 10) sum += i

// RICHTIG: Funktionaler Stil
val sum = (1 to 10).sum
```

---

## Beispiel-Klausurfragen

### **Theorie-Fragen (Freitext)**

1. **Nennen Sie zwei Vorteile von unveränderlichen Objekten mit kurzer Begründung.**
   - Thread-Sicherheit (keine Race Conditions)
   - Einfacheres Debugging (keine versteckten Änderungen)

2. **Erklären Sie das Expression Problem.**
   - Schwierigkeit neue Datentypen UND neue Operationen hinzuzufügen
   - OOP gut für neue Datentypen, schlecht für neue Operationen
   - Funktional umgekehrt

3. **Warum sind C++ Zeiger gefährlicher als Python Referenzen?**
   - C++: Zeigerarithmetik, manuelle Speicherverwaltung
   - Python: Keine direkten Speicherzugriffe, Garbage Collection

### **Praktische Aufgaben**

1. **Implementieren Sie eine Klasse `Rectangle` in Scala mit:**
   - Unveränderlichen Feldern `width` und `height`
   - Methode `area()` zur Flächenberechnung
   - Methode `scale(factor: Double)` die neues Rectangle zurückgibt

2. **Schreiben Sie eine Python-Funktion, die prüft ob eine Liste palindromisch ist:**
   - Rekursive Lösung
   - Iterative Lösung
   - Vergleichen Sie Vor-/Nachteile

3. **Zeigen Sie den Unterschied zwischen:**
   ```python
   # Shallow Copy
   list2 = list1.copy()
   
   # Deep Copy
   import copy
   list2 = copy.deepcopy(list1)
   ```

---

## Wichtige Formeln und Algorithmen

### **Primzahltest (Optimiert)**
```python
def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0: return False
    return True
```

### **Fibonacci (Rekursiv vs. Iterativ)**
```python
# Rekursiv (exponentiell!)
def fib_rec(n):
    if n <= 1: return n
    return fib_rec(n-1) + fib_rec(n-2)

# Iterativ (linear)
def fib_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

### **Sortieralgorithmen (Komplexität)**
- **Bubble Sort**: O(n²)
- **Quick Sort**: O(n log n) durchschnittlich
- **Merge Sort**: O(n log n) garantiert

---

## Zusammenfassung

> [!summary] **Prüfungserfolg-Strategie**
> 1. **Übungen selbstständig lösen** - Klausur orientiert sich eng daran
> 2. **Paradigmen verstehen** - Wann welches Paradigma verwenden?
> 3. **Sprachen-Konzepte** - Unterschiede zwischen Python/Scala/Java/C++
> 4. **Patterns erkennen** - Wiederkehrende Lösungsmuster
> 5. **Praxis vor Theorie** - Erst implementieren, dann verstehen

> [!tip] **Letzte Woche vor Klausur**
> - Alte Klausuren durchgehen
> - Cheatsheet vervollständigen
> - Übungsaufgaben nochmal lösen
> - Konzepte mit Kommilitonen diskutieren

**Viel Erfolg bei der Prüfung! 🎯**