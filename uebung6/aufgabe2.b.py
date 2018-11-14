def middle(list):
  list.pop(0)
  list.pop(len(list) - 1)
  return list

def main():
  myList = [213,14,123,'r41',123,'12223']
  print(middle(myList))

main()