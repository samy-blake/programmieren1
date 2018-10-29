def reverse(normalString):
    reveseString = ''

    for c in normalString:
        reveseString = c + reveseString
    return reveseString



normalString = input('Geben sie ein wort ein: ')

normalString = normalString.lower()
reveseString = reverse(normalString)
reveseString = reveseString.lower()

if(normalString == reveseString):
    print('Es handelt sich um ein Palindrom: (', normalString, ',', reveseString, ')')
else:
    print('Es handelt nicht um ein Palindrom: (', normalString, ',', reveseString, ')')
