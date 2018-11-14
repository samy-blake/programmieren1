
def maxElementInList(list, smallerThan):
  tmpElement = 0
  for element in list:
    if element > tmpElement:
      tmpElement = element

      if smallerThan > 0 and element < smallerThan:
        tmpElement = element

  return tmpElement

def mysort(myList):
  resultList = []
  tmpElement = 0

  for i in range(0, (len(myList) - 1)):
    element = myList[i]
    print(maxElementInList(element, tmpElement)) 


def main():
  myList = [5,6,1,3,7,3,0,5]
  print(mysort(myList))

main()