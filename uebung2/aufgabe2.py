day = int(input('Tag: '))
month = int(input('Monat: '))

if month > 12 or day > 31 or month == 0 or day == 0:
  print('Falsches Datum')

elif month == 2 and day > 28:
  print('Den Tag gibt es nicht')

elif (month <= 7 and month % 2 == 0 and month != 2) and day > 30:
  #April, Juni
  print('Den Tag gibt es einfach nicht :)')

elif (month > 7 and month % 2 != 0) and day > 30:
  #september, november
  print('Den Tag gibt es einfach nicht :)')

else:
  days = 0
  if month > 1:
    days += 31
  if month > 2:
    days += 28
  if month > 3:
    days += 31
  if month > 4:
    days += 30
  if month > 5:
    days += 31
  if month > 6:
    days += 30
  if month > 7:
    days += 31
  if month > 8:
    days += 31
  if month > 9:
    days += 30
  if month > 10:
    days += 31
  if month > 11:
    days += 30
  days += day
  print('tage seit jahres anfagn', days)
  

