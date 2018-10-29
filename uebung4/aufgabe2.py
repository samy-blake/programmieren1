def reverse(normalString):
    reveseString = ''

    for c in normalString:
        reveseString = c + reveseString
    return reveseString



normalString = input('Geben sie ein wort ein: ')
print(reverse(normalString))
    
