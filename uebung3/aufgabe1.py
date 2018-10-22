zahl = int(input('Zahl eingeben: '))

zeile = 0
zeichen = 0
text = ''

while zeile < zahl:
    text = ''
    zeichen = 0
    while zeichen <= zeile:
        text = text + 'x'
        zeichen += 1

    print(text)
    zeile += 1
    
