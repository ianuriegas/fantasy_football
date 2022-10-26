import csv
import time

start = time.time()
from teams.team0 import team_0
from teams.team1 import team_1
from teams.team2 import team_2
from teams.team3 import team_3
from teams.team4 import team_4
from teams.team5 import team_5
from teams.team6 import team_6
from teams.team7 import team_7
from teams.team8 import team_8
from teams.team9 import team_9
from teams.team10 import team_10
from teams.team11 import team_11
from teams.team12 import team_12
from teams.team13 import team_13

unavailable_players = team_0+team_1+team_2+team_3+team_4+team_5+team_6+team_7+team_8+team_9+team_10+team_11+team_12+team_13
# print(len(unavailable_players))

with open('data/unavailable_players.csv', 'w', encoding='UTF8', newline='') as f:
    for i in range(0, len(unavailable_players)):
        print(i, unavailable_players[i])
        writer = csv.writer(f)
        writer.writerow(unavailable_players[i])


end = time.time()
print(end - start)