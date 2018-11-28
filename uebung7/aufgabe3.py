from fachbereich import Fachbereich
from vorlesung import Vorlesung

def main():
  teilnehmer1 = ['ich', 'du', 'noch einer']
  teilnehmer2 = ['hans', 'peter', 'kram']
  vorlesung1 = Vorlesung('Programmieren1', teilnehmer1)
  vorlesung2 = Vorlesung('GDI', teilnehmer2)
  
  print(vorlesung1)
  
  print(vorlesung1.getTeilnehmer())
  print(vorlesung2.getTeilnehmer())


  fbi = Fachbereich('fbi', [vorlesung1])
  mediendesign = Fachbereich('mediendesign', [vorlesung2])

  fbi.addVorlesung(vorlesung2)
  print(fbi.getVorlesungen())

  print(mediendesign.getVorlesungen())

main()