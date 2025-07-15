#include <iostream>
#include <vector>
#include <chrono>
#include <random>
#include <iomanip>
#include <algorithm>

class Matrix {
private:
    int n;
    std::vector<double> data;
    
public:
    Matrix(int size) : n(size), data(size * size, 0.0) {}
    
    double get(int x, int y) const {
        if (x < 0 || x >= n || y < 0 || y >= n) {
            std::cerr << "Fehler: Index (" << x << ", " << y << ") außerhalb der Grenzen!" << std::endl;
            return 0.0;
        }
        return data[x * n + y];
    }
    
    void set(int x, int y, double value) {
        if (x < 0 || x >= n || y < 0 || y >= n) {
            std::cerr << "Fehler: Index (" << x << ", " << y << ") außerhalb der Grenzen!" << std::endl;
            return;
        }
        data[x * n + y] = value;
    }
    
    int get_dimension() const {
        return n;
    }
    
    void set_identity() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                set(i, j, (i == j) ? 1.0 : 0.0);
            }
        }
    }
    
    void set_zero() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                set(i, j, 0.0);
            }
        }
    }
    
    void set_random() {
        static std::random_device rd;
        static std::mt19937 gen(rd());
        static std::uniform_real_distribution<> dis(0.0, 1.0);
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                set(i, j, dis(gen));
            }
        }
    }
    
    Matrix multiply(const Matrix& other) const {
        Matrix result(n);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                double sum_val = 0.0;
                for (int k = 0; k < n; k++) {
                    sum_val += get(i, k) * other.get(k, j);
                }
                result.set(i, j, sum_val);
            }
        }
        return result;
    }
    
    // Optimierte Version mit direktem Datenzugriff
    Matrix multiply_optimized(const Matrix& other) const {
        Matrix result(n);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                double sum_val = 0.0;
                for (int k = 0; k < n; k++) {
                    sum_val += data[i * n + k] * other.data[k * n + j];
                }
                result.data[i * n + j] = sum_val;
            }
        }
        return result;
    }
    
    // Alternative Schleifenreihenfolge (i-k-j statt i-j-k)
    Matrix multiply_ikj(const Matrix& other) const {
        Matrix result(n);
        result.set_zero();
        for (int i = 0; i < n; i++) {
            for (int k = 0; k < n; k++) {
                for (int j = 0; j < n; j++) {
                    result.data[i * n + j] += data[i * n + k] * other.data[k * n + j];
                }
            }
        }
        return result;
    }
    
    void print_matrix() const {
        std::cout << "Matrix " << n << "x" << n << ":" << std::endl;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                std::cout << std::fixed << std::setprecision(2) << get(i, j) << "\t";
            }
            std::cout << std::endl;
        }
        std::cout << std::endl;
    }
};

void test_matrix_basics() {
    std::cout << "=== C++ Matrix-Klasse Test ===" << std::endl;
    
    Matrix m(3);
    std::cout << "Dimension: " << m.get_dimension() << std::endl;
    
    // Werte setzen
    m.set(0, 0, 1.0); m.set(0, 1, 2.0); m.set(0, 2, 3.0);
    m.set(1, 0, 4.0); m.set(1, 1, 5.0); m.set(1, 2, 6.0);
    m.set(2, 0, 7.0); m.set(2, 1, 8.0); m.set(2, 2, 9.0);
    
    m.print_matrix();
    
    std::cout << "m[1][1] = " << m.get(1, 1) << std::endl;
    std::cout << "m[0][2] = " << m.get(0, 2) << std::endl;
    std::cout << std::endl;
}

void test_matrix_multiplication() {
    std::cout << "=== Matrix-Multiplikation Test ===" << std::endl;
    
    Matrix a(2);
    Matrix b(2);
    
    // Matrix A: [[1, 2], [3, 4]]
    a.set(0, 0, 1); a.set(0, 1, 2);
    a.set(1, 0, 3); a.set(1, 1, 4);
    
    // Matrix B: [[2, 0], [1, 2]]
    b.set(0, 0, 2); b.set(0, 1, 0);
    b.set(1, 0, 1); b.set(1, 1, 2);
    
    std::cout << "Matrix A:" << std::endl;
    a.print_matrix();
    std::cout << "Matrix B:" << std::endl;
    b.print_matrix();
    
    Matrix result = a.multiply(b);
    std::cout << "A * B =" << std::endl;
    result.print_matrix();
}

void performance_test() {
    std::cout << "=== C++ Performance-Test ===" << std::endl;
    
    std::vector<int> sizes = {10, 50, 100, 200, 500};
    
    for (int size : sizes) {
        Matrix a(size);
        Matrix b(size);
        a.set_identity();
        b.set_identity();
        
        auto start = std::chrono::high_resolution_clock::now();
        Matrix result = a.multiply(b);
        auto end = std::chrono::high_resolution_clock::now();
        
        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
        double ms = duration.count() / 1000.0;
        
        std::cout << "Size " << size << "x" << size << ": " 
                  << std::fixed << std::setprecision(2) << ms << " ms" << std::endl;
    }
}

void performance_test_detailed() {
    std::cout << "=== Detaillierte Performance-Messung ===" << std::endl;
    
    std::vector<int> sizes = {10, 50, 100, 200};
    const int runs = 3;
    
    for (int size : sizes) {
        std::vector<double> times;
        
        for (int run = 0; run < runs; run++) {
            Matrix a(size);
            Matrix b(size);
            a.set_random();
            b.set_random();
            
            auto start = std::chrono::high_resolution_clock::now();
            Matrix result = a.multiply(b);
            auto end = std::chrono::high_resolution_clock::now();
            
            auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
            times.push_back(duration.count() / 1000.0);
        }
        
        double avg_time = 0;
        for (double t : times) avg_time += t;
        avg_time /= times.size();
        
        double min_time = *std::min_element(times.begin(), times.end());
        double max_time = *std::max_element(times.begin(), times.end());
        
        std::cout << "Size " << size << "x" << size << ": "
                  << "avg=" << std::fixed << std::setprecision(2) << avg_time << "ms, "
                  << "min=" << min_time << "ms, "
                  << "max=" << max_time << "ms" << std::endl;
    }
}

void compare_algorithms() {
    std::cout << "=== Algorithmen-Vergleich ===" << std::endl;
    
    const int size = 100;
    Matrix a(size);
    Matrix b(size);
    a.set_random();
    b.set_random();
    
    // Standard i-j-k
    auto start = std::chrono::high_resolution_clock::now();
    Matrix result1 = a.multiply(b);
    auto end = std::chrono::high_resolution_clock::now();
    double time_ijk = std::chrono::duration_cast<std::chrono::microseconds>(end - start).count() / 1000.0;
    
    // Optimiert mit direktem Datenzugriff
    start = std::chrono::high_resolution_clock::now();
    Matrix result2 = a.multiply_optimized(b);
    end = std::chrono::high_resolution_clock::now();
    double time_opt = std::chrono::duration_cast<std::chrono::microseconds>(end - start).count() / 1000.0;
    
    // Alternative i-k-j
    start = std::chrono::high_resolution_clock::now();
    Matrix result3 = a.multiply_ikj(b);
    end = std::chrono::high_resolution_clock::now();
    double time_ikj = std::chrono::duration_cast<std::chrono::microseconds>(end - start).count() / 1000.0;
    
    std::cout << "Standard (i-j-k): " << std::fixed << std::setprecision(2) << time_ijk << " ms" << std::endl;
    std::cout << "Optimiert (direkter Zugriff): " << time_opt << " ms" << std::endl;
    std::cout << "Alternative (i-k-j): " << time_ikj << " ms" << std::endl;
    std::cout << "Speedup Standard vs Optimiert: " << time_ijk/time_opt << "x" << std::endl;
    std::cout << "Speedup Standard vs i-k-j: " << time_ijk/time_ikj << "x" << std::endl;
}

void benchmark_comparison() {
    std::cout << "\n=== Python vs C++ Benchmark ===" << std::endl;
    std::cout << "Größe\tC++ Zeit\tPython Zeit (geschätzt)\tSpeedup" << std::endl;
    std::cout << "------------------------------------------------" << std::endl;
    
    std::vector<int> sizes = {10, 50, 100, 200, 500};
    
    for (int size : sizes) {
        Matrix a(size);
        Matrix b(size);
        a.set_random();
        b.set_random();
        
        // Beste C++ Version verwenden (i-k-j mit direktem Zugriff)
        auto start = std::chrono::high_resolution_clock::now();
        Matrix result = a.multiply_ikj(b);
        auto end = std::chrono::high_resolution_clock::now();
        
        double cpp_time = std::chrono::duration_cast<std::chrono::microseconds>(end - start).count() / 1000.0;
        
        // Geschätzte Python-Zeit basierend auf typischen Faktoren
        double estimated_python_time = cpp_time * 50; // Python ist typischerweise 50-100x langsamer
        
        std::cout << size << "x" << size << "\t"
                  << std::fixed << std::setprecision(2) << cpp_time << " ms\t"
                  << estimated_python_time << " ms\t\t"
                  << "~" << (int)(estimated_python_time / cpp_time) << "x" << std::endl;
    }
}

int main() {
    test_matrix_basics();
    test_matrix_multiplication();
    performance_test();
    performance_test_detailed();
    compare_algorithms();
    benchmark_comparison();
    
    return 0;
}