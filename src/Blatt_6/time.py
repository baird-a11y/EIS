import time
import random

class Matrix:
    def __init__(self, size):
        self.n = size
        self.data = [0.0] * (size * size)  # 1D Liste wie in C++
    
    def get(self, x, y):
        if x < 0 or x >= self.n or y < 0 or y >= self.n:
            print(f"Fehler: Index ({x}, {y}) außerhalb der Grenzen!")
            return 0.0
        return self.data[x * self.n + y]
    
    def set(self, x, y, value):
        if x < 0 or x >= self.n or y < 0 or y >= self.n:
            print(f"Fehler: Index ({x}, {y}) außerhalb der Grenzen!")
            return
        self.data[x * self.n + y] = value
    
    def get_dimension(self):
        return self.n
    
    def set_identity(self):
        """Setzt die Matrix als Einheitsmatrix"""
        for i in range(self.n):
            for j in range(self.n):
                self.set(i, j, 1.0 if i == j else 0.0)
    
    def set_zero(self):
        """Setzt alle Werte auf 0"""
        for i in range(self.n):
            for j in range(self.n):
                self.set(i, j, 0.0)
    
    def set_random(self):
        """Füllt die Matrix mit Zufallswerten zwischen 0 und 1"""
        for i in range(self.n):
            for j in range(self.n):
                self.set(i, j, random.random())
    
    def multiply(self, other):
        """Matrix-Multiplikation - gleiche Logik wie C++"""
        result = Matrix(self.n)
        for i in range(self.n):
            for j in range(self.n):
                sum_val = 0.0
                for k in range(self.n):
                    sum_val += self.get(i, k) * other.get(k, j)
                result.set(i, j, sum_val)
        return result
    
    def print_matrix(self):
        """Matrix ausgeben für Debugging"""
        print(f"Matrix {self.n}x{self.n}:")
        for i in range(self.n):
            for j in range(self.n):
                print(f"{self.get(i, j):.2f}", end="\t")
            print()
        print()

def test_matrix_basics():
    """Grundlegende Tests der Matrix-Klasse"""
    print("=== Python Matrix-Klasse Test ===")
    
    # Matrix erstellen
    m = Matrix(3)
    print(f"Dimension: {m.get_dimension()}")
    
    # Werte setzen
    m.set(0, 0, 1.0)
    m.set(0, 1, 2.0)
    m.set(0, 2, 3.0)
    m.set(1, 0, 4.0)
    m.set(1, 1, 5.0)
    m.set(1, 2, 6.0)
    m.set(2, 0, 7.0)
    m.set(2, 1, 8.0)
    m.set(2, 2, 9.0)
    
    # Matrix ausgeben
    m.print_matrix()
    
    # Einzelne Werte abfragen
    print(f"m[1][1] = {m.get(1, 1)}")
    print(f"m[0][2] = {m.get(0, 2)}")
    print()

def test_matrix_multiplication():
    """Test der Matrix-Multiplikation"""
    print("=== Matrix-Multiplikation Test ===")
    
    # Zwei 2x2 Matrizen erstellen
    a = Matrix(2)
    b = Matrix(2)
    
    # Matrix A: [[1, 2], [3, 4]]
    a.set(0, 0, 1); a.set(0, 1, 2)
    a.set(1, 0, 3); a.set(1, 1, 4)
    
    # Matrix B: [[2, 0], [1, 2]]
    b.set(0, 0, 2); b.set(0, 1, 0)
    b.set(1, 0, 1); b.set(1, 1, 2)
    
    print("Matrix A:")
    a.print_matrix()
    print("Matrix B:")
    b.print_matrix()
    
    # Multiplikation
    result = a.multiply(b)
    print("A * B =")
    result.print_matrix()
    
    # Ergebnis sollte sein: [[4, 4], [10, 8]]

def performance_test():
    """Performance-Test für verschiedene Matrixgrößen"""
    print("=== Python Performance-Test ===")
    
    sizes = [10, 50, 100, 200, 500]
    
    for size in sizes:
        # Zwei Einheitsmatrizen erstellen
        a = Matrix(size)
        b = Matrix(size)
        a.set_identity()
        b.set_identity()
        
        # Zeitmessung
        start_time = time.time()
        result = a.multiply(b)
        end_time = time.time()
        
        duration_ms = (end_time - start_time) * 1000
        print(f"Size {size}x{size}: {duration_ms:.2f} ms")
        
        # Bei großen Matrizen wird es sehr langsam
        if size >= 500:
            print("  (Warnung: Sehr langsam!)")

def performance_test_detailed():
    """Detaillierte Performance-Messung mit mehreren Durchläufen"""
    print("=== Detaillierte Performance-Messung ===")
    
    sizes = [10, 50, 100, 200]
    runs = 3  # Mehrere Durchläufe für genauere Messung
    
    for size in sizes:
        times = []
        
        for run in range(runs):
            # Zufällige Matrizen für realistischeren Test
            a = Matrix(size)
            b = Matrix(size)
            a.set_random()
            b.set_random()
            
            start_time = time.time()
            result = a.multiply(b)
            end_time = time.time()
            
            times.append((end_time - start_time) * 1000)
        
        avg_time = sum(times) / len(times)
        min_time = min(times)
        max_time = max(times)
        
        print(f"Size {size}x{size}: avg={avg_time:.2f}ms, min={min_time:.2f}ms, max={max_time:.2f}ms")

def compare_algorithms():
    """Vergleich verschiedener Matrix-Multiplikationsalgorithmen"""
    print("=== Algorithmen-Vergleich ===")
    
    class MatrixOptimized(Matrix):
        def multiply_ikj(self, other):
            """Alternative Schleifenreihenfolge (i-k-j statt i-j-k)"""
            result = Matrix(self.n)
            for i in range(self.n):
                for k in range(self.n):
                    for j in range(self.n):
                        current = result.get(i, j)
                        result.set(i, j, current + self.get(i, k) * other.get(k, j))
            return result
    
    size = 100
    a = MatrixOptimized(size)
    b = MatrixOptimized(size)
    a.set_random()
    b.set_random()
    
    # Standard i-j-k
    start = time.time()
    result1 = a.multiply(b)
    time_ijk = (time.time() - start) * 1000
    
    # Alternative i-k-j
    start = time.time()
    result2 = a.multiply_ikj(b)
    time_ikj = (time.time() - start) * 1000
    
    print(f"Standard (i-j-k): {time_ijk:.2f} ms")
    print(f"Alternative (i-k-j): {time_ikj:.2f} ms")
    print(f"Speedup: {time_ijk/time_ikj:.2f}x")

if __name__ == "__main__":
    test_matrix_basics()
    test_matrix_multiplication()
    performance_test()
    performance_test_detailed()
    compare_algorithms()