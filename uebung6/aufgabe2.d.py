
def quadriereListeA(myList):
  '''
  Variante A:
  '''
  for index in range(0, (len(myList) -1)):
    myList[index] = myList[index]**2
  return myList


def quadriereListeB(myList):
  '''
  Variante B:
  '''
  newList = []
  for index in range(0, (len(myList) -1)):
    newList.append(myList[index]**2)
  return newList

def main():
  myList = [1,2,3,4,5,6,7,8]
  print(quadriereListeA(myList))
  
  print(quadriereListeB(myList))

main()