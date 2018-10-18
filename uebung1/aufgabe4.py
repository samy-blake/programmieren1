# source: https://www.apotheken-umschau.de/bmi-rechner

# Aufgabe 4-a:
print('BMI Calc 4-a')

# das int fehlte
size = float(input('Geben Sie ihre Körpergröße in m ein (bsp.: 2.80): '))
mass = int(input('Geben Sie ihr Gewicht in kg ein (80): '))

bmi = mass / (size * size) 

print('ihr bmi ist {0}'.format(bmi))
print()

#######################################################
# Aufgabe 4-b
print('BMI Calc 4-b')

# das int fehlte
size = float(input('Geben Sie ihre Körpergröße in m ein (bsp.: 2.80): '))
mass = int(input('Geben Sie ihr Gewicht in kg ein (80): '))

bmi = mass / (size * size) 
bmi = round(bmi, 2)
print('ihr bmi ist {0}'.format(bmi))
print()

#######################################################
# Aufgabe 4-c
print('BMI Calc 4-c')

# das int fehlte
size = float(input('Geben Sie ihre Körpergröße in m ein (bsp.: 2.80): '))
mass = int(input('Geben Sie ihr Gewicht in kg ein (80): '))

bmi = mass / (size * size) 
bmi = round(bmi, 2)
bmitype = ''

if bmi < 25:
  bmitype = 'Normalgewicht'

elif bmi < 30:
  bmitype = 'Übergewicht'
  
elif bmi < 35:
  bmitype = 'Adipositas (Fettleibigkeit) Grad I'
elif bmi < 40:
  bmitype = 'Adipositas Grad II'
else:
  bmitype = 'Adipositas Grad III'


print('ihr bmi ist {0} und sie haben {1}'.format(bmi, bmitype))
