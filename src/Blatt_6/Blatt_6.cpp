// Blatt_6.cpp
#include <iostream>
#include <vector>
using namespace std;

class Matrix {
private:
    vector<double> data;    // 1D-Vector für 2D-Matrix
    int n;                  // Dimension (n x n)

public:
    // Konstruktor: Erstellt eine n x n Matrix
    Matrix(int size) : n(size), data(size * size) {
        // data wird automatisch mit 0.0 initialisiert
        cout << "Matrix " << n << "x" << n << " erstellt" << endl;
    }
    
    // Getter: Holt Wert an Position (x, y)
    double get(int x, int y) const {
        // TODO: Implementiere Bounds-Check (optional)
        if (x < 0 || x >= n || y < 0 || y >= n) {
            cout << "Fehler: Index außerhalb der Grenzen!" << endl;
            return 0.0;
        }
        
        // 2D-Index zu 1D-Index: x * n + y
        return data[x * n + y];
    }
    
    // Setter: Setzt Wert an Position (x, y)
    void set(int x, int y, double value) {
        // TODO: Implementiere Bounds-Check (optional)
        if (x < 0 || x >= n || y < 0 || y >= n) {
            cout << "Fehler: Index außerhalb der Grenzen!" << endl;
            return;
        }
        
        // 2D-Index zu 1D-Index: x * n + y
        data[x * n + y] = value;
    }
    
    // Größenabfrage: Gibt Dimension zurück
    int getDimension() const {
        return n;
    }
    
    // Hilfsfunktion: Matrix ausgeben (für Debugging)
    void print() const {
        cout << "Matrix " << n << "x" << n << ":" << endl;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cout << get(i, j) << "\t";
            }
            cout << endl;
        }
        cout << endl;
    }

    void setEinheitsmatrix() {
        // Arbeitet mit "this" Matrix
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                set(i, j, (i == j) ? 1.0 : 0.0);
            }
        }
    }
    void setZufallMatrix() {
        // Arbeitet mit "this" Matrix
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                set(i, j, static_cast<double>(rand() % 100)); // Zufallswerte zwischen 0 und 99
            }
        }
    }

    Matrix multiply(const Matrix& other) const {
    // Erstellt neue Matrix für Ergebnis
        Matrix result(n);
        for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    double sum = 0.0;
                    for (int k = 0; k < n; k++) {
                        sum += get(i, k) * other.get(k, j);
                    }
                    result.set(i, j, sum);
                }
            }
        // Gibt diese zurück
        return result;
        
    }

};

// Testfunktion für die Matrix-Klasse
void testMatrixBasics() {
    cout << "=== Matrix-Klasse Test ===" << endl;
    
    // 1. Matrix erstellen
    Matrix m(3);
    m.setZufallMatrix();
    m.print();
    Matrix m2(3);
    m2.setZufallMatrix();
    m2.print();

    Matrix c = m2.multiply(m);
    c.print();

    cout << "Dimension: " << m.getDimension() << endl;
    
    // 2. Werte setzen
    m.set(0, 0, 1.0);
    m.set(0, 1, 2.0);
    m.set(0, 2, 3.0);
    m.set(1, 0, 4.0);
    m.set(1, 1, 5.0);
    m.set(1, 2, 6.0);
    m.set(2, 0, 7.0);
    m.set(2, 1, 8.0);
    m.set(2, 2, 9.0);
    
   
    // 3. Matrix ausgeben
    m.print();
    
    // 4. Einzelne Werte abfragen
    cout << "m[1][1] = " << m.get(1, 1) << endl;
    cout << "m[0][2] = " << m.get(0, 2) << endl;
    
    // 5. Bounds-Check testen
    cout << "Test Bounds-Check:" << endl;
    m.get(5, 5);  // Sollte Fehler ausgeben
    m.set(5, 5, 99.0);  // Sollte Fehler ausgeben
}

// Weitere Testfunktionen
void testMatrixSizes() {
    cout << "=== Verschiedene Größen Test ===" << endl;
    
    // Kleine Matrix
    Matrix small(2);
    small.set(0, 0, 1.0);
    small.set(0, 1, 2.0);
    small.set(1, 0, 3.0);
    small.set(1, 1, 4.0);
    small.print();
    
    // Große Matrix
    Matrix large(5);
    // Diagonal setzen
    for (int i = 0; i < 5; i++) {
        large.set(i, i, 1.0);
    }
    large.print();
}

void testMatrixCopy() {
    cout << "=== Copy-Test ===" << endl;
    
    Matrix original(2);
    original.set(0, 0, 1.0);
    original.set(0, 1, 2.0);
    original.set(1, 0, 3.0);
    original.set(1, 1, 4.0);
    
    cout << "Original:" << endl;
    original.print();
    
    // Copy-Konstruktor wird automatisch von vector<> bereitgestellt
    Matrix copy = original;
    cout << "Kopie:" << endl;
    copy.print();
    
    // Änderung in Kopie sollte Original nicht beeinflussen
    copy.set(0, 0, 999.0);
    cout << "Nach Änderung in Kopie:" << endl;
    cout << "Original:" << endl;
    original.print();
    cout << "Kopie:" << endl;
    copy.print();
}

int main() {
    testMatrixBasics();
    testMatrixSizes();
    testMatrixCopy();
    
    return 0;
}