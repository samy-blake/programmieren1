
class Fachbereich:

  def __init__(self, name, vorlesungen):
    self.__name = name
    self.__vorlesungen = vorlesungen

    
  def addVorlesung(self, vorlesung):
    self.__vorlesungen.append(vorlesung)

  def getVorlesungen(self):
    return self.__vorlesungen