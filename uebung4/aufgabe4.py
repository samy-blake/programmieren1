def reverse(normalString):
    reveseString = ''

    for c in normalString:
        reveseString = c + reveseString
    return reveseString


def intToDual(intenger):
    resultString = ''

    while(intenger > 0):
        mod = intenger % 2
        resultString = str(mod) + resultString
        intenger = intenger / 2
        intenger = int(intenger)
        
    return resultString


def dualToInt(string):
    resultIntenger = 0
    reverseString = reverse(string)
    exponential = 0
    
    for c in reverseString:
        intenger = int(c)
        resultIntenger = resultIntenger + (intenger * 2**exponential)
        exponential += 1
        
    return resultIntenger

intZahl = int(input('Gebe eine Intenger Zahl ein: '))
dualZahl = input('Gebe eine Dual Zahl ein: ')

print(intToDual(intZahl))

print(dualToInt(dualZahl))
