import pandas as pd
from IPython import embed

url = 'https://en.wikipedia.org/wiki/2021%E2%80%9322_Premier_League'
df = pd.read_html(url)
games = df[5]

mapping = {i:j for i,j in zip(games.columns[1:],games['Home \ Away'])}

def read_game(string):
    score = string.split('–')
    if len(score) != 2:
        return 0
        
    h = score[0]
    a = score[1]
    if h == a:
        return 1
    elif h > a: 
        return 3
    else:
        return 0
 
table = {games['Home \ Away'][i]:0 for i in range(20)}

for i, row in games.iterrows():
    team1 = row[0] 
    for team2_, game in row.iteritems():
        if team2_ != "Home \ Away":
            team2 = mapping[team2_]
            table[team1] += read_game(game)
            table[team2] += read_game(game[::-1]) # reverse score
        
tab = pd.Series(table)
print(tab.sort_values(ascending=False))
