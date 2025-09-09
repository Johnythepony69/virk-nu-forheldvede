# 🌐 MINIKASSE SYSTEM - NETVÆRKSADGANG

## 📋 Sådan giver du andre computere adgang til kassesystemet

### 1. **🔥 Konfigurer Windows Firewall (VIGTIGT!)**

**Automatisk måde:**
1. Højreklik på `setup_firewall.bat`
2. Vælg "Kør som administrator"
3. Følg instruktionerne i scriptet

**Manuel måde:**
1. Åbn Windows Sikkerhed
2. Gå til "Firewall og netværksbeskyttelse"
3. Klik på "Tillad en app gennem firewall"
4. Tilføj undtagelse for port 8080

### 2. **🚀 Start serveren**
```
python start_server.py
```
eller dobbeltklik på `start_minikasse.bat`

### 3. **📱 Find din IP-adresse**
Din computers IP-adresse er: **192.168.0.39**

Serveren viser automatisk de rigtige adresser når den starter.

### 4. **🌐 Tilslut andre enheder**

**Fra andre computere på samme netværk:**
- Åbn webbrowser
- Gå til: `http://192.168.0.39:8080`

**Fra telefoner/tablets:**
- Åbn webbrowser
- Gå til: `http://192.168.0.39:8080`

## 🔧 Tekniske detaljer

- **Server type:** Waitress (produktionsklar)
- **Port:** 8080
- **Max forbindelser:** 1000 samtidigt
- **Tråde:** 6
- **IP binding:** 0.0.0.0 (alle netværksgrænseflader)

## 🛠️ Fejlfinding

**Problem:** Andre computere kan ikke tilslutte sig

**Løsninger:**
1. **Kontroller firewall** - Kør `setup_firewall.bat` som administrator
2. **Kontroller netværk** - Sørg for at alle enheder er på samme WiFi/netværk
3. **Test forbindelse** - Ping computeren: `ping 192.168.0.39`
4. **Genstart router** - Nogle routere blokerer intern trafik

**Problem:** IP-adressen har ændret sig

**Løsning:**
- Serveren viser automatisk den aktuelle IP når den starter
- Eller kør: `ipconfig | findstr "IPv4"`

## 🔒 Sikkerhed

- Systemet kører kun på dit lokale netværk (ikke internettet)
- Alle brugere skal stadig logge ind med brugernavn/adgangskode
- Kun lederen kan ændre brugerkoder og tilføje varer
- Data gemmes lokalt på din computer

## 📞 Support

Hvis du har problemer:
1. Kontroller at Windows Firewall tillader port 8080
2. Sørg for at alle enheder er på samme netværk
3. Prøv at genstarte routeren
4. Kontakt din IT-support hvis problemerne fortsætter
