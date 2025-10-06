team1 = ['alpha', 'bravo', 'charlie']
team2 = ['delta', 'omega']

def team_bigO(team1):
    team_count = 0
    
    for t in team1:
        print(t)
        team_count += 1

    for t2 in team2:
        print(t2)
        team_count += 1    

    print(team_count)

team_bigO(team1)