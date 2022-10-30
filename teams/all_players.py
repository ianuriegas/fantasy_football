import json

f = open('../data/all_players_info.json')
all_players = []
data = json.load(f)
for i in range(0,2734):
    firstName = (data[i]["firstName"]).lower()
    lastName = (data[i]["lastName"]).lower()
    player_id = (data[i]["id"])
    fullname = firstName+"-"+lastName
    all_players.append([fullname, player_id])
    print(fullname, player_id)

# print(all_players)
test = all_players.index("3128390")

print(all_players)