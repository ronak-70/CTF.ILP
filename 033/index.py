import math

nummer =[3,5,7,9,2,0]

def berechne_mittelwert(zahlen: liste) -> float:
  """
  durch sum() kann alle Zähler stimmen.
  dann teilen auf lenght liste

  """
  
  if not zahlen:
      raise ValueError("Liste darf nicht leer sein")
  
  average= sum(zahlen) / len(zahlen)
  return average;

print(berechne_mittelwert(nummer))



def berechne_standardabweichung(zahlen: liste) -> float:
  """
  Die Stichprobenstandardabweichung (oder empirische Standardabweichung) ist ein Maß dafür, wie stark die Werte in einer Stichprobe um ihren Mittelwert streuen. Sie wird berechnet, indem die Wurzel aus der Varianz der Stichprobe gezogen wird.
  """
  n = len(nummer)
  if n < 2:
    raise ValueError("Mindestens 2 Datenpunkte benötigt.")
  average = berechne_mittelwert(zahlen)
  varianz = sum(pow(x - average,2) for x in zahlen)/ (n-1)
  return math.sqrt(varianz)

s = berechne_standardabweichung(nummer)
print(f"Stichprobenstandardabweichung: {s:.2f}")


def konvertiere_temperatur(wert, einheit_von, einheit_zu):
  """
  Diese Funktion soll Temperaturwerte zwischen Celsius ('C'), Fahrenheit ('F') und Kelvin ('K') umrechnen können
  """
  if einheit_von == 'C':
        if einheit_zu == 'F':
            return wert * 9/5 + 32  # C -> F
        elif einheit_zu == 'K':
            return wert + 273.15  # C -> K
    elif einheit_von == 'F':
        if einheit_zu == 'C':
            return (wert - 32) * 5/9  # F -> C
        elif einheit_zu == 'K':
            return (wert - 32) * 5/9 + 273.15  # F -> K
    elif einheit_von == 'K':
        if einheit_zu == 'C':
            return wert - 273.15  # K -> C
        elif einheit_zu == 'F':
            return (wert - 273.15) * 9/5 + 32  # K -> F
    else:
        raise ValueError("Ungültige Einheit angegeben.")

print(konvertiere_temperatur(100 , C , F))







