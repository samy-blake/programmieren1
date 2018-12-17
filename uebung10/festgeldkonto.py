from konto import Konto

class Festgeldkonto(Konto):

  def __init__(self, kontoinhaber, kontostand):
    super().__init__(kontoinhaber, kontostand)
    self._zinssatz = 0.03

  def verzinsen(self):
    self._kontostand += self._zinssatz * self._kontostand


if __name__ == "__main__":
    festgeldkonto = Festgeldkonto('Sören', 20.50)
    festgeldkonto.zahleEin(15.4)
    print(festgeldkonto)
    festgeldkonto.verzinsen()
    print(festgeldkonto)
    festgeldkonto.verzinsen()
    print(festgeldkonto)