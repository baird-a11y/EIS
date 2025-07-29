## **Theorie-Aufgabe 8** (4 Punkte)

Kreuze an, was richtig ist:

- [ ] Python wird kompiliert
- [ ] Scala wird interpretiert
- [ ] MyPy prüft Typen zur Laufzeit
- [x] isinstance() prüft Typen zur Laufzeit
- [x] Type Annotations werden von Python ignoriert
- [ ] C++ hat einen Garbage Collector

### **Praxis-Aufgabe 7** (8 Punkte)

Korrigiere die Syntax-Fehler in diesem Python-Code:

```python
def count_even[numbers: list] -> int
    count == 0
    for i in range(numbers):
        if numbers(i) % 2 = 0
            count++
    return Count
    
    
# Korrigiert
def count_even(numbers: List[int]) -> int
    count == 0
    for i in range(numbers):
        if numbers[i] % 2 = 0
            count++
    return count
```

### **Theorie-Aufgabe 9** (6 Punkte)

Vervollständige die Sätze: 
a) Um in Python eine Exception zu werfen, nutzt man das Keyword raise 
b) Die Länge einer Liste erhält man mit dem Befehl len()
c) Auf ein Listenelement greift man mit [] Klammern zu 
d) Das Tool zum Type Checking in Python heißt MyPy
e) In Scala nutzt man Option[T] mit Some/None statt null 
f) Python ist dynamisch typisiert, Scala ist statisch typisiert

### **Praxis-Aufgabe 8** (10 Punkte)

Schreibe eine einfache Funktion mit Type Annotations:

```python
from typing import List

def find_first_negative(numbers: List[int]) -> Optional[int]:
    """
    Findet die erste negative Zahl in der Liste.
    Gibt die Zahl zurück oder None wenn keine gefunden.
    """
    # Deine Implementierung (ohne isinstance!)
    for i in range(len(numbers)):
	    if numbers[i]<0:
		    return numbers[i]
		else:
			return None
    pass
```

### **Praxis-Aufgabe 9** (12 Punkte)

Implementiere diese beiden Funktionen:

```python
# a) Zähle Vokale (a,e,i,o,u) in einem String

def count_vowels(text: str) -> int:

    count = 0

    for char in text:

        if char.lower() in "aeiou":

            count += 1

    return count    


# b) Prüfe ob eine Zahl gerade ist
def is_even(n: int) -> bool:

    if n%2==0:

        return True

    else:

        return False
```

### **Theorie-Aufgabe 10** (5 Punkte)

Was gibt dieser Code aus? Erkläre warum:

```python
def test(x: str) -> str:
    return x + x

print(test(5))  # Was passiert?

```

a) Bei normaler Python-Ausführung? 
Er ignoriert die Typ Anotation und addiert die beiden Zahlen, da er sie als Int erkennt und nicht als str.
b) Was würde MyPy sagen?
MyPy würde einen Fehler werfen, da ein String erwartet wird, aber ein Int übergeben wird.

### **Praxis-Aufgabe 10** (10 Punkte)

Übersetze diesen Python-Code nach Scala:

```python
def absolute_value(n: int) -> int:
    if n < 0:
        return -n
    else:
        return n
```

### **MINI-AUFGABEN zum Syntax üben** (je 2 Punkte)

1. Wie greift man auf das 3. Element einer Liste `my_list` zu?
    
    ```python
    element = my_list[2]
    ```
    
2. Wie erhält man die Länge einer Liste `my_list`?
    
    ```python
    length = len(my_list)
    ```
    
3. Wie wirft man eine ValueError Exception mit der Nachricht "Fehler"?
    
    ```python
    raise "Fehler"
    ```
    
4. Schreibe eine for-Schleife von 10 bis 1 (rückwärts):
    
    ```python
    for i in (10,1,-1):
        print(i)
    ```
    
5. Wie prüft man, ob eine Variable `x` ein Integer ist?
    
    ```python
    if isinstance(x,int):
        print("x ist ein Integer")
    ```
    

---

**WICHTIGE REGELN ZUM MERKEN:**

- **raise** Exception, nicht return
- **len(liste)**, nicht range(liste)
- **liste[i]**, nicht liste(i)
- **i += 1**, nicht i++
- **def funktion():** mit Doppelpunkt!

Löse diese Aufgaben Schritt für Schritt. Bei Unsicherheiten: Lieber einfach anfangen als gar nicht!