from konto import Konto

class Girokonto(Konto):

  def __init__(self, kontoinhaber, kontostand, dispokredit):
    super().__init__(kontoinhaber, kontostand)
    self._dispokredit = dispokredit * (-1)

  def hebeAb(self, betrag):
    if self._kontostand - betrag > self._dispokredit:
      self._kontostand -= betrag



if __name__ == "__main__":
    girokonto = Girokonto('Sören', 1000, 1000)
    girokonto.zahleEin(200)
    girokonto.hebeAb(1500)
    print(girokonto)
