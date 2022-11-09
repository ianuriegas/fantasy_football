import requests
from bs4 import BeautifulSoup
from universal.common_use import whitelist, headers, espn_cookies, has_numbers
team_number = 3
url = "https://fantasy.espn.com/apis/v3/games/ffl/seasons/2022/segments/0/leagues/898997769?rosterForTeamId={}&view=mDraftDetail&view=mLiveScoring&view=mMatchupScore&view=mPendingTransactions&view=mPositionalRatings&view=mRoster&view=mSettings&view=mTeam&view=modular&view=mNav".format(team_number+1)

r = requests.get(url, headers=headers, cookies=espn_cookies)
espn_raw_data = r.json()
espn_draft_detail = espn_raw_data

myTeam = []

for i in range(0, 16):
    player_id = espn_draft_detail['teams'][team_number]['roster']['entries'][i]['playerId']

    # Defenses are negative
    if player_id > 0:
        temp_url = "https://www.espn.com/nfl/player/_/id/{}".format(player_id)
        page = requests.get(temp_url)
        soup = BeautifulSoup(page.content, "html.parser")

        first_name = ((soup.find("span", {"class": "truncate min-w-0 fw-light"})).text.strip()).lower()
        first_name = ''.join(filter(whitelist.__contains__, first_name))
        last_name = ((soup.find("span", {"class": "truncate min-w-0"})).text.strip()).lower()
        last_name = ''.join(filter(whitelist.__contains__, last_name))
        position = ((soup.find("ul", { "class" : "PlayerHeader__Team_Info list flex pt1 pr4 min-w-0 flex-basis-0 flex-shrink flex-grow nowrap"})).find_all('li')[2].text.strip()).lower()
        if has_numbers(position):
            position = ((soup.find("ul", {
                "class": "PlayerHeader__Team_Info list flex pt1 pr4 min-w-0 flex-basis-0 flex-shrink flex-grow nowrap"})).find_all(
                'li')[2].text.strip()).lower()
        myTeam.append([first_name, last_name, position, player_id])

# print(myTeam)
# for info in range(0,len(myTeam)):
#     if info > 0:
#         format_name_curr = myTeam[info][0] + "-" + myTeam[info][1]
#         format_name_prev = myTeam[info-1][0] + "-" + myTeam[info-1][1]
#         output = "https://www.fantasypros.com/nfl/start/{}-{}.php".format(format_name_curr,format_name_prev)
#         print(output)