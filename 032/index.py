


while True:
  i = 0
  zahl = None
  while zahl == None:
    nummer = input("Bitte fügen sie ein Nummer ein: ")

    if nummer.isdigit() == False:
      i += 1
      print(f"leider hast du ungültige Nummer eingegeben!Du kannst nur mehr {3-i} mal versuchen")

      if i >= 3:
        print("program ist am Ende!" )
        exit()
      continue

    zahl = int(nummer)

    if zahl < 1 or zahl> 1000:
      print("Zahl muss zwieschen 1-1000 sein!")
      zahl = None;
      continue

  if zahl % 2 == 0:
     print("Die Zahl ist grade")
  else:
     print("Die Zahl ist ungerade")

  if zahl % 7 and zahl % 13 == 0:
     print("Die Zahl ist ein Vielfaches von 7 UND 13!")   
  elif zahl < 50:
     print("Die Zahl ist kleiner als 50")
  elif 50 <= zahl <= 500:
     print("Die Zahl liegt zwischen 50 und 500")
  else:
     print("Die Zahl ist größer als 500")

    continue

  nochmal = input("Möchten Sie nochmal eine Nummer einfügen?(ja/nein)")
  if nochmal != ja :
     print("Program ist beendet")
     break     

       


 



    
 




