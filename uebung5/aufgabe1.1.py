def maxChar(word):
  maxChar = ''
  for char in word:
    if maxChar < char:
      maxChar = char
    
  return maxChar

word = input('Gebe ein wort ein: ')
char = maxChar(word)
print(char)