competitions = [
["HTML","C#"],
["C#","PYTHON"],
["PYTHON","HTML"]
]

results = [0,0,1]
HOME_WIN = 1
def tournamentWinner(competitions,results):
    bestTeam = ""
    scores = {bestTeam:0}
    for idx,competition in enumerate (competitions):
        result = results[idx]
        #print(result)
        home,away = competition
        winningTeam = home if result == HOME_WIN else away
        #print(winningTeam)
        updateScores(winningTeam,3,scores)
        if scores[winningTeam] > scores[bestTeam]:
            bestTeam = winningTeam
    print(scores)
    return bestTeam

def updateScores(team,points,scores):
    if team not in scores:
        scores[team] = 0

    scores[team] +=points

print(tournamentWinner(competitions,results))
