def maxChar(word):
  dictObj = dict()

  '''
  Das Word wird wie eine Liste behandelt und jeder buchstarbe
  wird in einem dict gepackt
  danach wird der counter pro buchstarbe erhöht, 
  wenn der buchstarbe nochmal im word vorkommt  
  '''
  for char in word:
    if char in dictObj:
      dictObj[char] += 1
    else:
      dictObj[char] = 1
  maxChar = ''
  maxCountChar = 0

  '''
  Danach wird geschaut, welcher counter am höhstens ist
  '''
  for dic in dictObj:
    if dictObj[dic] > maxCountChar:
      maxChar = dic
      maxCountChar = dictObj[dic]
  
  return maxChar

word = input('Gebe ein wort ein: ')
char = maxChar(word)
print(char)