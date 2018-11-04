def isCharCorrect(char, charPosition, word):
  wordCharPosition = 0
  for wordChar in word:
    
    if wordChar == char:
      
      if wordCharPosition == charPosition:
        # richtiger buchstarbe, richtige position
        return 2

      # richtiger buchstarbe, falsche position      
      return 1
    wordCharPosition += 1

  # falsche buchstarbe, falsche position
  return 0


def main():
  rightChar = 5
  choiceRight = 0

  while choiceRight < rightChar:
    result = ''
    choice = input('')

    charPosition = 0
    for choiseChar in choice:
      charCorrect = isCharCorrect(choiseChar, charPosition, word)

      
      if charCorrect == 0:
        result += choiseChar
      elif charCorrect == 1:
        # richtiger buchstarbe, falsche position
        result += '(' + choiseChar + ')'
      else:
        # richtiger buchstarbe, richtige position
        result += '[' + choiseChar + ']'
        choiceRight += 1
      
      charPosition += 1

    print('Clue:', result)



word = 'tiger'
main()