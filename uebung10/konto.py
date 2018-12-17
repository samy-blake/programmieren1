class Konto:
  def __init__(self, kontoinhaber, kontostand):
    self._kontoinhaber = kontoinhaber
    self._kontostand = kontostand

  def zahleEin(self, betrag):
    if betrag > 0:
      self._kontostand += betrag

  def hebeAb(self, betrag):
    if self._kontostand - betrag > 0:
      self._kontostand -= betrag

  def __str__(self):
    return 'Kontostand: ' + str(self._kontostand)