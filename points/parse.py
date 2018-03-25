import pandas as pd
from pprint import pprint

df1 = pd.read_csv('players.csv')
df2 = pd.read_csv('sample.csv')

teams = dict()
team_names = list()

for team in df2['IPL 2018 Team']:
	team_names.append(team)
	# team_names.update(team)

team_names = list(set(team_names))

for team in team_names:
	teams[team] = list()

# print(teams)
# for teams in df2['']

for i, row1 in df1.iterrows():
	for j, row2 in df2.iterrows():
		# print(name.split()[0][1])
		try:
			if(row1['Player_Name'].split()[0][0].lower() == row2['Name'].split()[0][0].lower() and row1['Player_Name'].split()[1].lower() == row2['Name'].split()[1].lower()):
				# print(row2['Name'], row2['IPL 2018 Team'])
				teams[row2['IPL 2018 Team']].append([row2['Name'], row1['Avg_Score']])
		except:
			pass

score_dict = dict()
for team, value in teams.items():
	scores = 0
	for data in value:
		scores+=data[1]
	avg = scores/len(value)
	score_dict[team] = avg
pprint(teams)
pprint(score_dict)
