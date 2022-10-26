import csv
import time
start = time.time()
from my_team import myTeam
my_players = myTeam
with open('data/my_players.csv', 'w', encoding='UTF8', newline='') as f:
    for i in range(0, len(my_players)):
        print(i, my_players[i])
        writer = csv.writer(f)
        writer.writerow(my_players[i])

end = time.time()
print(end - start)