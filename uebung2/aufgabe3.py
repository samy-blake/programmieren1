form = input('Welche Form (kreis/quadrat/rechteck): ')
surface = 0
pi = 3.14159 # war mir nicht ganz sicher ob ich "math" schon verwenden darf

if form == 'kreis':
  print('Kreis:')
  rad = float(input('gebe den Radius ein: '))
  surface = 2 * pi * rad

elif form == 'quadrat':
  print('Quadrat:')
  a = float(input('gebe eine Länge ein: '))
  surface = a**2
  

elif form == 'rechteck':
  print('Rechteck:')
  a = float(input('gebe die Länge ein: '))
  b = float(input('gebe die Breite ein: '))
  surface = a * b
  
else:
  print('Falsche Eingabe')

surface = round(surface, 2)
print('Das Volume ist:', surface)