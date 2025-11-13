import uuid

class Fahrzeug:
  def __init__(self, marke: str, modell: str, kennzeichen: str, 
                 kilometerstand: float = 0.0, status: str = "bereit"):
        """Konstruktor für die Fahrzeug-Klasse"""
        print("Ein neues Fahrzeug wurde initialisiert!")
        self.marke = marke
        self.modell = modell
        self.kennzeichen = kennzeichen
        self.kilometerstand = kilometerstand
        self.status = status
        self.fahrzeug_id = str(uuid.uuid4())

  def fahren(self, strecke_km: float):
        
      if self.status == "im Einsatz":
          self.kilometerstand += strecke_km
          print(f"Das Fahrzeug ist {strecke_km} km gefahren.")
      else:
          raise ValueError("Fehler: Fahrzeug ist nicht im Einsatz!") 
             
  def setze_status(self, neuer_status: str):
      
      gültige_Status = ["bereit", "im Einsatz", "in Wartung", "ausgemustert"]

      if neuer_status in gültige_Status:
          self.status = neuer_status
      else:
          print("Ungültiger Status!")

  def __str__(self):
      return (f"Fahrzeug [{self.fahrzeug_id[:8]}]: "
                f"{self.marke} {self.modell} ({self.kennzeichen}), "
                f"Status: {self.status}, KM-Stand: {self.kilometerstand}")          
  

auto1 = Fahrzeug("Mercedes", "A-Klasse", "B-AB-1234")
print(auto1)
auto1.setze_status("bereit")
auto1.fahren(100)
print(auto1)  