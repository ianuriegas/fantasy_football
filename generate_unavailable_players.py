import csv
import time

start = time.time()
from teams.teams import unavailable_players

with open('data/unavailable_players.csv', 'w', encoding='UTF8', newline='') as f:
    for i in range(0, len(unavailable_players)):
        print(i, unavailable_players[i])
        writer = csv.writer(f)
        writer.writerow(unavailable_players[i])

end = time.time()
print(end - start)
