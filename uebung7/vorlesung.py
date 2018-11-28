class Vorlesung:

  def __init__(self, title, teilnehmer):
    self.__title = title
    self.__teilnehmer = teilnehmer
  
  def __str__(self):
    return 'title: ' + self.__title + ' teilnehmer: ' + str(self.__teilnehmer)

  def schreibeEin(self, name):
    self.__teilnehmer.append(name)
  
  def schreibeAus(self, name):
    self.__teilnehmer.remove(name)

  def anzahlTeilnehmer(self):
    return len(self.__teilnehmer)
  
  def getTeilnehmer(self):
    sortTeilnehmer = self.__teilnehmer.copy()
    sortTeilnehmer.sort()
    return sortTeilnehmer
