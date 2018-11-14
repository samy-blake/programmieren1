
def is_sorted(list):
  sortedList = list.copy() # kopiert die ganze liste in eine neue Variable
  sortedList.sort()
  return list == sortedList

def main():
  myList = [123,124,5123,51123,5234,123]
  myList2 = [1,2,3,4,5,6,7]
  print(is_sorted(myList))
  print(is_sorted(myList2))

main()