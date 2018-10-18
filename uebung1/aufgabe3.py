# Aufgabe 3-a:
print('Hello MDI!!')

# das int fehlte
tipp = int(input('Erraten sie eine Zahl: '))

if tipp == 3:
  print('Gewonnen!')
else:
  print('Verloren')

print('Das Spiel ist aus.')

#######################################################
# Aufgabe 3-b

print('Hello MDI!!')

tipp = int(input('Erraten sie eine Zahl: '))

if tipp == 3:
  print('Gewonnen!')
else if tipp < 3:
  print('zu klein')
else if tipp > 3:
  print('zu groß')

print('Das Spiel ist aus.')