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

  '''
  Danach wird geschaut, welcher counter am höhstens ist
  '''
  maxChar = []
  maxCountChar = 0
  
  for dic in dictObj:
    if dictObj[dic] > maxCountChar:
      maxChar = [dic]
      maxCountChar = dictObj[dic]
  
  for dic in dictObj:
    if dictObj[dic] == maxCountChar and not maxChar.__contains__(dic):
      maxChar.append(dic)
    
  return maxChar, maxCountChar

word = input('Gebe ein wort ein: ')
char = maxChar(word)
print(char)