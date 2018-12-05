from liga import Liga
from team import Team

team1 = Team('Hannover 96', 0, 0, 0, 0)
team2 = Team('Dortmund', 0, 0, 0, 0)
team3 = Team('Schalke', 0, 0, 0, 0)

liga = Liga('Bundesliga', [team1])
liga.nehmeTeil(team2)
liga.nehmeTeil(team3)

liga.spiele(team1, team2, 4, 2)
print(liga.gibTabelle())
