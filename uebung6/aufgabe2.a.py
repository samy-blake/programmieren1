def chop():
  myList.pop(0)
  myList.pop(len(myList) - 1)

myList = [1,2,3,4,5,6]
print(myList)
chop()
print(myList)
