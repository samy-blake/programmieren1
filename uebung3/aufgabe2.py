zahl1 = int(input('zahl 1: '))
zahl2 = int(input('zahl 2: '))

tmpzahl = 0
ergebnis = 0

if zahl1 == 0:
    ergebnis = zahl2
else:
    while zahl2 != 0:
        if zahl1 > zahl2:
            zahl1 = zahl1 - zahl2
        else:
            zahl2 = zahl2 - zahl1
    ergebnis = zahl1

print('Ergebnis: ', ergebnis)
