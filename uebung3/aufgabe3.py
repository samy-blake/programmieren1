c = 0
while c <= 0:
  c = int(input('gebe c ein: '))

a = c
b = 1

while (a**2 + b**2 != c**2) and a > 1:
  a -= 1
  b = 1
  while (a**2 + b**2 != c**2) and b < c:
    b += 1

if a**2 + b**2 == c**2:
  print(a, '² (', a**2 , ') +', b, '² (', b**2, ') =', c, '² (', c**2, ')' )
else:
  print('fuer c (', c ,') gibt es kein a und b !')
