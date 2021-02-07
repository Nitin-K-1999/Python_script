# A list of cricket team is given below. Print the number of possible matches between each of them. Also print each possible match in the format team1 vs team2.

team_list = ['CSK','RCB','Sun Risers','Deccan Chargers','Mumbai Indians']
matches = []

for index in range(len(team_list)) :
    for team in team_list[index+1:] :
        matches.append('{} vs {}'.format(team_list[index],team))

print('The number of possible matches is',len(matches))
print('They are :')

for match in matches :
    print(match)
