import socket

# Server-IP und -Port
IP: str = "127.0.0.1"
PORT: int = 41337

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Verbindung zum Server herstellen
        sock.connect((IP, PORT))
        print(f"Verbunden mit Server auf {IP}:{PORT}")

        while True:
            # Benutzer auffordern, einen Dateinamen einzugeben
            filename: str = input("Welche Datei möchtest du anfordern? (oder 'exit' zum Beenden): ").strip()
            
            if filename.lower() == 'exit':
                break
            
            # Dateinamen an den Server senden
            sock.sendall(filename.encode("utf-8"))
            
            # Antwort des Servers empfangen
            data: bytes = sock.recv(4096)
            content: str = data.decode("utf-8")
            
            # Antwort auf der Konsole ausgeben
            print(content)

if __name__ == "__main__":
    main()