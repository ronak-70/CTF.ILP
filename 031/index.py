
#preis = float(input("bitte füge Preis:  EuR  "))
def wecsGeld(preis): #name von function
  wecs = preis * 1.08  #macht preis mal US-Dollar  
  wecs2 = preis * 165.25 #macht preis (eru) mal Japanischen Yen (JPY)
  
  return wecs , wecs2



#print(wecsGeld(float(input("bitte füge Preis: EuR  ")))) #man kann preis einfügen

name = input("fügen sie bitte Ihre Name: ")
alter =input("fügen sie bitte Ihrer Alter: ")
wohnort =input("fügen sie bitte Ihrer Wohnort : ")
bruf = input("fügen sie bitte Ihre Beruf: ")
interesse = input("Bist du an Python-Programmierung interessiert? (ja/nein)")

def interessetype(interesse):
  if interesse.lower() == "ja" :
    return "True"
  else:
    return "False"

def alterskategurie(alter):
  if alter < 25:
    return "Young Enthusiast"
  else:
    return "Experienced Professional"


print(f"Hallo, {name},\n") 
print(f"Du bist {alter} Jahre alt und gehörst zur Kategorie: {alterskategurie(int(alter))}")  
print(f"Dein Wohnort:{wohnort}")  
print(f"Dein Bruf:{bruf}")  
print(f"Interessiert an Python: {interessetype(interesse)}")  





