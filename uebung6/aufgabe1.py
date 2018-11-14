def summeDerQuadrate(number):
  summe = 0
  for count in range(1, number + 1):
    summe += count**2
  return summe

def main():
  number = int(input('Gebe eine Nummer ein: '))
  print(summeDerQuadrate(number))

main()