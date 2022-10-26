import json

import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://fantasy.espn.com/apis/v3/games/ffl/seasons/2022/segments/0/leagues/898997769?rosterForTeamId=4&view=mDraftDetail&view=mLiveScoring&view=mMatchupScore&view=mPendingTransactions&view=mPositionalRatings&view=mRoster&view=mSettings&view=mTeam&view=modular&view=mNav"

espn_cookies = {"swid": "{11F62244-D8C5-462F-BA6C-F2393EF28D6E}",
                "espn_s2": "AEAVxVJq2qWDySYmzXGnfmGpIf7ebI8NnUIfu1cBw90yJ1EARDXUF6KRi74Ndcxg3oPedJvIXICsEzFOuxQYsuHVmvjMw%2B1fDGykccjnjXA40pgm3TzteY%2FAtiReh%2BBSUH1pUZ%2B8RljdCCavZI%2Fs4XfilhaR7Eoq%2FNZeAYE%2F3u9ORgJuqjGNCpDONGs0PRn6%2FtfV7WH%2B1%2Bk6mbpyBXWW%2BY0JwWoRni6t%2BWPsjGfmMjWnfLEUHMUL%2BlTdghkpm7uy70wVy7KIeR30Re9HE5zSNGRj"}

headers = {
 'Connection': 'keep-alive',
 'Accept': 'application/json, text/plain, */*',
 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
}

r = requests.get(url, headers=headers, cookies=espn_cookies)
espn_raw_data = r.json()
# team_info = espn_raw_data[0]
espn_draft_detail = espn_raw_data
draft_picks = espn_draft_detail['teams'][3]['roster']['entries'][0]['playerId']

# position_dict = { "Running Back" : "RB" , "Wide Receiver" : }

# print(draft_picks)

class Player:
    def __init__(self, first_name, last_name, position, MyTeamID):
        self.first_name = first_name.lower()
        self.last_name = last_name.lower()
        self.position = position
        self.MyTeamID = MyTeamID
    def getFirstName(self):
        return self.first_name.lower

    def getLastName(self):
        return self.last_name.lower

    def getPosition(self):
        return self.position

    def getMyTeamID(self):
        return self.MyTeamID

    def getFormattedName(self):
        return self.first_name + "-" + self.last_name

    def getInfo(self):
        return self.first_name + "\n" + self.last_name + "\n" + self.position + "\n" + str(self.MyTeamID) + "\n"


team_number = 3
myTeam = []

for i in range(0, 16):
    my_team_id = espn_draft_detail['teams'][team_number]['roster']['entries'][i]['playerId']

    # Defenses are negative
    if my_team_id > 0:
        temp_url = "https://www.espn.com/nfl/player/_/id/{}".format(my_team_id)
        page = requests.get(temp_url)
        soup = BeautifulSoup(page.content, "html.parser")


        first_name = (soup.find("span", { "class" : "truncate min-w-0 fw-light"})).text.strip()
        last_name = (soup.find("span", { "class" : "truncate min-w-0"})).text.strip()


        fullname = first_name+"_"+last_name

        position = (soup.find("ul", { "class" : "PlayerHeader__Team_Info list flex pt1 pr4 min-w-0 flex-basis-0 flex-shrink flex-grow nowrap"})).find_all('li')[2].text.strip()
        myTeam.append([first_name, last_name, position, my_team_id])
        fullname = Player(first_name, last_name, position, my_team_id)
        print(fullname.getInfo())
        print(fullname.getFormattedName())
        comparison = "https://www.fantasypros.com/nfl/start/{}-justin-herbert.php".format(fullname.getFormattedName())
        print("https://www.fantasypros.com/nfl/start/christian-mccaffrey-justin-herbert.php")
        print(comparison)
        print(myTeam[i - 1][1])
# print(myTeam)

all_players = []
# all_teams = []
leauge_size = espn_draft_detail['settings']['size']
for i in range(0,leauge_size):
    abbrev = espn_draft_detail['teams'][i]['abbrev']
# team_id = espn_draft_detail['teams']
# print(team_id)

# for team in range(0, 16):

# https://www.fantasypros.com/nfl/start/christian-mccaffrey-kenyan-drake.php
# comparison = "https://www.fantasypros.com/nfl/start/{}-{}.php".format(myTeam[0].getFirstName() + "-"+myTeam[1].test.getFormattedName())
# player = myTeam[0]
# print(player.getFirstName())