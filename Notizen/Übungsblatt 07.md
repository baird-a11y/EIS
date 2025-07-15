# **CLIENT-SERVER PROGRAMMIERUNG**

## 📋 **Aufgabenüberblick**

### **Ziel:** Minimaler Webserver und Webbrowser

- **Server:** Datei-Server der Dateien aus `www/`-Verzeichnis bereitstellt
- **Client:** Einfacher Client der Dateien anfordert (CLI + GUI Version)
- **Technologie:** TCP-Sockets in Python
- **Sicherheit:** Nur localhost (127.0.0.1) für lokale Tests

---

## 🔧 **Deine Implementierung - Code-Analyse**

### **1. Mini-Server (`mini_server.py`)**

```python
# Kernfunktionalität:
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(("127.0.0.1", 41337))
    sock.listen()
    
    while True:
        connection, address = sock.accept()
        with connection:
            while True:
                data = connection.recv(4096)
                if len(data) == 0: break
                
                filename = data.decode("utf-8").strip()
                file_path = os.path.join("www", filename)
                
                try:
                    with open(file_path, 'r') as file:
                        content = file.read()
                    connection.sendall(content.encode("utf-8"))
                except FileNotFoundError:
                    error_message = f"Fehler: Datei '{filename}' nicht gefunden.\n"
                    connection.sendall(error_message.encode("utf-8"))
```

**Funktionen:**

- ✅ Socket-Erstellung und Binding an localhost:41337
- ✅ Endlosschleife für Client-Verbindungen
- ✅ Dateiname-Empfang vom Client
- ✅ Datei aus `www/`-Verzeichnis lesen
- ✅ Dateiinhalt oder Fehlermeldung zurücksenden
- ✅ Proper Exception-Handling

### **2. CLI-Client (`Blatt_7.py`)**

```python
def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(("127.0.0.1", 41337))
        
        while True:
            filename = input("Welche Datei möchtest du anfordern? (oder 'exit' zum Beenden): ").strip()
            if filename.lower() == 'exit': break
            
            sock.sendall(filename.encode("utf-8"))
            data = sock.recv(4096)
            content = data.decode("utf-8")
            print(content)
```

**Funktionen:**

- ✅ Interaktive Benutzeroberfläche
- ✅ Verbindung zum Server
- ✅ Dateiname-Eingabe und -Übertragung
- ✅ Antwort-Anzeige
- ✅ Graceful Exit mit 'exit'

### **3. GUI-Client (`gui.py`)**

```python
class FileRequestClient(QWidget):
    def send_request(self):
        filename = self.filename_input.text().strip()
        
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect(('127.0.0.1', 41337))
                sock.sendall(filename.encode("utf-8"))
                data = sock.recv(4096)
                content = data.decode("utf-8")
                self.text_display.setText(content)
        except Exception as e:
            self.text_display.setText(f'Fehler: {str(e)}')
```

**Funktionen:**

- ✅ PySide6 GUI mit QLineEdit und QTextEdit
- ✅ Button-Event-Handling
- ✅ Socket-Verbindung pro Request
- ✅ Exception-Handling für GUI
- ✅ Benutzerfreundliche Fehleranzeige

---

## 🎯 **Vorlesungsinhalte - Theoretische Grundlagen**

### **1. Client-Server Architektur** ⭐⭐⭐ **(SEHR KLAUSURRELEVANT)**

#### **Standard-Architektur:**

```
Server-Prozess (Port 80)
├── sock.listen()
├── sock.accept() → neuer Socket
├── ServerThread für jeden Client
└── Endlosschleife

Client-Prozess
├── sock.connect(server_ip, port)
├── sock.write(request)
├── sock.read(response)
└── sock.close()
```

#### **Kommunikationsmuster:**

- **Server:** Wartet passiv auf Verbindungen (`listen()` → `accept()`)
- **Client:** Initiiert aktiv Verbindung (`connect()`)
- **Threading:** Ein Thread pro Client für parallele Verarbeitung
- **Protokoll:** Anwendungsspezifische Nachrichtenformate

### **2. Socket-API** ⭐⭐⭐ **(KLAUSURRELEVANT)**

#### **Server-Kommandos:**

```python
socket()    # Socket erstellen
bind()      # IP/Port festlegen
listen()    # Auf Verbindungen warten
accept()    # Verbindung akzeptieren → neuer Socket!
recv()/send() # Daten empfangen/senden
close()     # Verbindung schließen
```

#### **Client-Kommandos:**

```python
socket()    # Socket erstellen
connect()   # Mit Server verbinden
send()/recv() # Daten senden/empfangen
close()     # Verbindung schließen
```

### **3. HTTP-Protokoll Grundlagen** ⭐⭐ **(KLAUSURRELEVANT)**

#### **HTTP-Request Format:**

```
GET /index.html HTTP/1.1
Host: localhost:41337
User-Agent: Mozilla/5.0 (...)
Accept: text/html,application/xhtml+xml
Connection: keep-alive
```

#### **HTTP-Response Format:**

```
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1234

<html>...</html>
```

### **4. Nebenläufige Architekturen** ⭐⭐ **(KLAUSURRELEVANT)**

#### **Threading-Modell:**

```python
# Pro Client ein Thread
while True:
    client_socket, address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
```

#### **Message-Passing:**

- **Synchron:** Client wartet auf Antwort
- **Asynchron:** Client kann weitermachen
- **Queues:** Nachrichten-Puffering zwischen Prozessen

---

## 🔥 **Klausurrelevante Themen**

### **Sehr wahrscheinlich (90%):**

#### **1. Socket-Programmierung implementieren**

```python
# Typische Aufgabe: Simple Echo-Server
def echo_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', 8080))
        s.listen()
        while True:
            conn, addr = s.accept()
            with conn:
                data = conn.recv(1024)
                conn.sendall(data)  # Echo zurück
```

#### **2. Client-Server Kommunikationsprotokoll**

```python
# Protokoll definieren: COMMAND:DATA
def handle_request(connection):
    request = connection.recv(1024).decode()
    command, data = request.split(':', 1)
    
    if command == "GET":
        response = get_file(data)
    elif command == "PUT":
        response = save_file(data)
    
    connection.sendall(response.encode())
```

#### **3. HTTP-Request/Response verstehen**

- **Request-Line:** `GET /path HTTP/1.1`
- **Headers:** `Host:`, `User-Agent:`, `Accept:`
- **Response-Status:** `200 OK`, `404 Not Found`
- **Content-Type:** `text/html`, `application/json`

### **Wahrscheinlich (70%):**

#### **4. Exception-Handling in Netzwerkcode**

```python
try:
    sock.connect(('server.com', 80))
    sock.sendall(b'GET / HTTP/1.1\r\n\r\n')
    response = sock.recv(4096)
except ConnectionRefusedError:
    print("Server nicht erreichbar")
except socket.timeout:
    print("Timeout")
finally:
    sock.close()
```

#### **5. Threading für Multi-Client Support**

```python
import threading

def handle_client(client_socket, address):
    try:
        while True:
            data = client_socket.recv(1024)
            if not data: break
            # Process request
            client_socket.sendall(response)
    finally:
        client_socket.close()

# Server-Loop
while True:
    client_sock, addr = server_sock.accept()
    thread = threading.Thread(target=handle_client, args=(client_sock, addr))
    thread.daemon = True
    thread.start()
```

### **Mögliche Fragen (40%):**

#### **6. Sicherheitsaspekte**

- **Localhost-Binding:** `127.0.0.1` vs `0.0.0.0`
- **Input-Validation:** Dateipfad-Injection verhindern
- **Buffer-Overflow:** Sichere `recv()`-Größen
- **Firewall:** Nur lokale Verbindungen erlauben

#### **7. Performance-Optimierungen**

- **Connection-Pooling:** Verbindungen wiederverwenden
- **Asynchrone I/O:** `asyncio` für viele Clients
- **Caching:** Häufige Dateien im Speicher
- **Compression:** Gzip für große Dateien

---

## 📝 **Typische Klausuraufgaben**

### **Aufgabe 1: Socket-Server erweitern (15 Punkte)**

```python
# Gegeben: Basic Echo Server
# Erweitern Sie zu einem File-Server der:
# - Dateien aus einem Verzeichnis liest
# - HTTP-ähnliche Responses sendet
# - Fehlerbehandlung für fehlende Dateien
# - Logging von Client-Requests

def enhanced_file_server():
    # Ihre Implementierung hier...
```

### **Aufgabe 2: Client-Protocol implementieren (10 Punkte)**

```python
# Implementieren Sie einen Client der:
# - Verbindung zum Server aufbaut
# - Mehrere Dateien nacheinander anfordert
# - Responses parst und anzeigt
# - Graceful disconnect bei Fehlern

def smart_client():
    # Ihre Implementierung hier...
```

### **Aufgabe 3: HTTP-Request Parser (10 Punkte)**

```python
# Parsen Sie HTTP-Requests:
# "GET /index.html HTTP/1.1\r\nHost: localhost\r\n\r\n"
# Extrahieren Sie: Method, Path, Headers

def parse_http_request(request_string):
    # Ihre Implementierung hier...
    return method, path, headers
```

### **Aufgabe 4: Multi-Threading (10 Punkte)**

```python
# Erweitern Sie den Server um Threading:
# - Ein Thread pro Client
# - Shared-State für Statistiken
# - Thread-sichere Logging-Funktion

def threaded_server():
    # Ihre Implementierung hier...
```

### **Aufgabe 5: Fehlerbehandlung (5 Punkte)**

```python
# Welche Exceptions können auftreten?
# - ConnectionRefusedError
# - socket.timeout
# - FileNotFoundError
# - UnicodeDecodeError
# Implementieren Sie entsprechende try/except Blöcke
```

---

## 🎓 **Klausur-Checkliste**

### **Auswendig können:**

- [ ] **Socket-API:** `socket()`, `bind()`, `listen()`, `accept()`, `connect()`
- [ ] **HTTP-Format:** Request-Line, Headers, Response-Status
- [ ] **Python-Syntax:** `with socket.socket() as s:`, `s.recv(4096)`
- [ ] **Exception-Types:** `ConnectionRefusedError`, `socket.timeout`
- [ ] **Threading:** `threading.Thread(target=func, args=())`

### **Verstehen und erklären:**

- [ ] **Client-Server Architektur:** Rollen, Kommunikationsmuster
- [ ] **TCP vs UDP:** Zuverlässigkeit, Verbindungsorientierung
- [ ] **Port-Binding:** Localhost vs. alle Interfaces
- [ ] **Multi-Threading:** Parallelität, Shared-State Probleme
- [ ] **Sicherheitsaspekte:** Input-Validation, Firewall

### **Implementieren können:**

- [ ] **Basic Socket-Server:** Listen, Accept, Receive, Send
- [ ] **Basic Socket-Client:** Connect, Send, Receive
- [ ] **File-Server:** Datei lesen, Inhalt senden
- [ ] **HTTP-Parser:** Request-Line und Headers extrahieren
- [ ] **Exception-Handling:** Try/except für Netzwerk-Errors
- [ ] **Threading:** Multi-Client Support

---

## 📊 **Bewertung deiner Lösung**

### **Stärken:**

- ✅ **Vollständige Implementierung** aller Anforderungen
- ✅ **Proper Exception-Handling** für FileNotFoundError
- ✅ **Saubere Code-Struktur** mit type hints
- ✅ **GUI-Integration** mit PySide6
- ✅ **Sichere Konfiguration** (localhost-only)
- ✅ **Resource-Management** mit `with`-Statements

### **Verbesserungsmöglichkeiten:**

- ⚠️ **Threading:** Kein Multi-Client Support (nur ein Client gleichzeitig)
- ⚠️ **HTTP-Protokoll:** Keine echten HTTP-Responses
- ⚠️ **Input-Validation:** Keine Pfad-Injection Schutz
- ⚠️ **Logging:** Keine Aktivitäts-Logs
- ⚠️ **Graceful Shutdown:** Keine Signal-Handler

### **Erweiterungen für Bonuspunkte:**

```python
# HTTP-Response Headers
def send_http_response(connection, content, status=200):
    response = f"HTTP/1.1 {status} OK\r\n"
    response += "Content-Type: text/plain\r\n"
    response += f"Content-Length: {len(content)}\r\n\r\n"
    response += content
    connection.sendall(response.encode())

# Threading Support
def handle_client(client_socket, address):
    print(f"Client {address} connected")
    # ... existing logic

# Im Server:
while True:
    connection, address = sock.accept()
    thread = threading.Thread(target=handle_client, args=(connection, address))
    thread.start()
```

---

## 🏆 **Fazit**

Deine Lösung ist **solide und funktional** mit allen Grundanforderungen erfüllt. Für die Klausur bist du gut vorbereitet, da du die wichtigsten Konzepte (Socket-API, Client-Server Pattern, Exception-Handling) praktisch implementiert hast.

**Klausur-Tipp:** Übe das schnelle Implementieren von Basic Socket-Code auswendig, da dies oft als Grundlage für weitere Aufgaben dient!