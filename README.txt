# Kassesystem med Lager, Profit og Fortryd Salg

## Installation (Windows 10)
1. Installer Python fra: https://www.python.org/downloads/ (husk at sætte flueben i "Add to PATH").
2. Pak zip-filen ud i en mappe.
3. Åbn kommandoprompt i mappen (Shift + højreklik → "Åbn kommandovindue her").
4. Installer afhængigheder:
   pip install -r requirements.txt
5. Start serveren:
   python app.py
6. Åbn browseren på:
   http://127.0.0.1:5000/

## Roller og funktioner
- **Leder (kofod / alexLA)**: Kan se/ændre lager, tilføje varer, se profit og diagrammer.
- **Kontrollør (kontrollor1 / check123)**: Kan se lager og alle salg.
- **Kassearbejdere**: Kan lave salg og fortryde sidste salg i op til 30 sekunder.

## Data
- Lager, salg og profit gemmes i data.json så alt huskes til næste gang.
