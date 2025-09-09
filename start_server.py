#!/usr/bin/env python3
"""
Minikasse Production Server
Starter kassesystemet med Waitress produktionsserver
"""

from waitress import serve
from app import app
import os
import sys

def start_production_server():
    """Start the production server with Waitress"""
    
    # Set production environment
    os.environ['FLASK_ENV'] = 'production'
    app.config['ENV'] = 'production'
    app.config['DEBUG'] = False
    
    # Get local IP address
    import socket
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    
    print("=" * 70)
    print("🚀 MINIKASSE SYSTEM - PRODUKTIONSSERVER")
    print("=" * 70)
    print(f"🌐 Lokal adresse: http://127.0.0.1:8080")
    print(f"🌐 Netværksadresse: http://{local_ip}:8080")
    print(f"📱 Fra andre enheder: http://{local_ip}:8080")
    print("📝 Log niveau: INFO")
    print("⚡ Server type: Waitress (Produktionsklar)")
    print("🔥 Firewall: Åbn port 8080 hvis nødvendigt")
    print("=" * 70)
    print("✅ Serveren kører nu og er tilgængelig på netværket!")
    print("💡 Tryk Ctrl+C for at stoppe serveren")
    print("=" * 70)
    
    try:
        # Start Waitress server
        serve(
            app, 
            host='0.0.0.0',  # Tillader forbindelser fra alle IP-adresser
            port=8080,       # Produktionsport
            threads=6,       # Antal tråde til at håndtere requests
            connection_limit=1000,  # Maksimalt antal samtidige forbindelser
            cleanup_interval=30,    # Oprydningsinterval i sekunder
            channel_timeout=120,    # Timeout for kanaler
            log_untrusted_proxy_headers=False,  # Sikkerhedsindstilling
            clear_untrusted_proxy_headers=True  # Ryd usikre proxy headers
        )
    except KeyboardInterrupt:
        print("\n" + "=" * 60)
        print("🛑 Serveren blev stoppet af brugeren")
        print("👋 Tak for at bruge Minikasse System!")
        print("=" * 60)
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ FEJL: Kunne ikke starte serveren: {e}")
        print("💡 Kontroller om port 8080 allerede er i brug")
        sys.exit(1)

if __name__ == "__main__":
    start_production_server()
