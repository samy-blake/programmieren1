
def mysort(sortedList):

  for outIndex in range(len(sortedList) - 1):
    rangeForSearch = len(sortedList) - outIndex - 1
    
    for searchIndex in range(rangeForSearch):
      
      if sortedList[searchIndex] > sortedList[searchIndex + 1]:
        # vertauschen von den beiden Werten
        tmp = sortedList[searchIndex] 
        sortedList[searchIndex] = sortedList[searchIndex + 1]
        sortedList[searchIndex + 1] = tmp
  
  return sortedList


def main():
  sortedList = [5,6,1,3,7,3,0,5]
  print(mysort(sortedList))

main()