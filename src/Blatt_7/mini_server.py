import socket
import os

# 127.0.0.1 ist "localhost" - Verbindungen werden NUR vom eigenen Rechner akzeptiert.
# Das ist ein wichtiges Sicherheitsfeature; so kann die ganze böse Welt da draußen
# unser Spielzeug nicht so leicht angreifen. Um alle Verbindungen zu erlauben,
# nutzt man hier einen leeren String (nicht empfohlen).
#
IP: str = "127.0.0.1"

# Als Portnummer für den Server sollte man eine Zahl > 1024 nehmen, da man sonst
# u.U. Root-Rechte braucht
#
PORT: int = 41337

# Verzeichnis, in dem sich die Dateien befinden
WWW_DIR: str = "www"

# Die "with"-Anweisung in Python sorgt dafür, dass bei Exceptions der Socket trotzdem
# wieder richtig geschlossen wird (über magic-methods "__enter__" und "__exit__", die
# die Socket-Klasse unterstützt). Hier ist das kosmetisch, vereinfacht aber Syntax
# und Nutzung (man könnte auch einen "try...finally"-Block nutzen, oder Exceptions
# einfach ignorieren, da das nur ein Spielzeugprogramm ist und das OS am Ende aufräumt).
#
# with...as: in "sock" steht die Rückgabe der Funktion socket.socket(), die sockets erzeugt.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Binden des Sockets an IP-Adresse und Port
    sock.bind((IP, PORT))
    # Warten, bis jemand anklopft...
    sock.listen()
    print(f"Server hört auf {IP}:{PORT}...")
    
    while True:
        # Wir bekommen einen neuen Socket "connection" zurück und dessen IP-Adresse und Port
        connection, address = sock.accept()
        print(f"Verbunden mit {address}")
        
        # Das Gleiche wieder: die Verbindung soll im Fehlerfall zuverlässig geschlossen werden
        # (auch hier optional)
        with connection:
            while True:
                # Wir empfangen ein "raw" Byte-Array.
                # Man muss die maximale Zahl von Bytes, die auf einmal empfangen werden
                # können, angeben; laut Doku darf die wg. technischer Limits nicht beliebig groß
                # sein. Ich habe die Info gefunden, das hier 4K eine sinnvolle Obergrenze sind.
                # Will man mehr empfangen, muss man die Daten nacheinander empfangen
                # und zusammenstückeln.
                data: bytes = connection.recv(4096)
                
                # Dies beendet den Server falls der (simple) Client sich verabschiedet
                if len(data) == 0:
                    break
                
                # Wir convertieren das ganze voller Vertrauen (Hallo liebe Hacker!) in Python
                # UTF-8 Strings und geben das ganze auf der Konsole aus.
                filename: str = data.decode("utf-8").strip()
                print(f"Angeforderter Dateiname: {filename}")
                
                # Pfad zur Datei im www-Verzeichnis
                file_path: str = os.path.join(WWW_DIR, filename)
                
                try:
                    # Öffnen und Lesen der Datei
                    with open(file_path, 'r') as file:
                        content: str = file.read()
                    
                    # Senden des Dateiinhalts an den Client
                    connection.sendall(content.encode("utf-8"))
                except FileNotFoundError:
                    # Falls die Datei nicht gefunden wird, sende eine Fehlermeldung
                    error_message: str = f"Fehler: Datei '{filename}' nicht gefunden.\n"
                    connection.sendall(error_message.encode("utf-8"))
                except Exception as e:
                    # Falls ein anderer Fehler auftritt, sende eine allgemeine Fehlermeldung
                    error_message: str = f"Fehler beim Lesen der Datei '{filename}': {str(e)}\n"
                    connection.sendall(error_message.encode("utf-8"))