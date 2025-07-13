#include <iostream>
#include <cmath>
#include <chrono>

using namespace std;

int main() {
    int n = 11; // Zu testende Zahl
    
    // Spezialfall: Zahlen < 2 sind keine Primzahlen
    if (n < 2) {
        cout << "Not Prime\n";
        return 0;
    }
    
    // Spezialfall: 2 ist eine Primzahl
    if (n == 2) {
        cout << "Prime\n";
        return 0;
    }
    
    // Teste alle möglichen Teiler von 2 bis sqrt(n)
    int i = 2;
    while (i * i <= n) {  // Effizienter als sqrt(n)
        if (n % i == 0) {
            cout << "Not Prime\n";
            return 0;
        }
        i++;
    }
    
    cout << "Prime\n";
    return 0;
}