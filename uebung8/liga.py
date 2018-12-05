class Liga:

    def __init__(self, name, teams):
        self._name = name
        self._teams = teams
    
    def nehmeTeil(self, team):
        self._teams.append(team)
    
    def spiele(self, team1, team2, toreTeam1, toreTeam2):
        team1.addGegenTore(toreTeam2)
        team2.addGegenTore(toreTeam1)
        
        team1.increaseSpiele()
        team2.increaseSpiele()
        
        team1.addErzielteTore(toreTeam1)
        team2.addErzielteTore(toreTeam2)

        if(toreTeam1 > toreTeam2):
            team1.win()
        elif(toreTeam2 > toreTeam1):
            team2.win()
        else:
            team1.draw()
            team2.draw()

    def gibTabelle(self):
        tabelle = ''
        for team in self._teams:
            tabelle += team.__str__() + '\n'
        return tabelle