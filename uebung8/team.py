class Team:

    def __init__(self, name, anzahlSpiele, punkte, erzielteTore, gegenTore):
        self._name = name
        self._anzahlSpiele = anzahlSpiele
        self._punkte = punkte
        self._erzielteTore = erzielteTore
        self._gegenTore = gegenTore
    
    def __str__(self):
        return self._name.ljust(15) + ' -- ' +  \
            'Spiele ' + str(self._anzahlSpiele) + ' : -- ' + \
            'Punkte: ' + str(self._punkte) + ' --'  + \
            'Tore: ' + str(self._erzielteTore) + ':' + str(self._gegenTore)
    
    def addGegenTore(self, gegenTore):
        self._gegenTore += gegenTore

    def addErzielteTore(self, erzielteTore):
        self._erzielteTore += erzielteTore

    def win(self):
        self._punkte += 3
    
    def draw(self):
        self._punkte += 1

    def increaseSpiele(self):
        self._anzahlSpiele += 1

if __name__ == '__main__':
    team = Team('test', 12, 12, 12, 12)
    team.addGegenTore(2)
    print(team)