# all teams in the league
import requests
from bs4 import BeautifulSoup
from universal.common_use import whitelist, headers, espn_cookies, has_numbers

unavailable_players = []
teams_in_league = 14
for team_number in range(0,teams_in_league):
    url = "https://fantasy.espn.com/apis/v3/games/ffl/seasons/2022/segments/0/leagues/898997769?rosterForTeamId={}&view=mDraftDetail&view=mLiveScoring&view=mMatchupScore&view=mPendingTransactions&view=mPositionalRatings&view=mRoster&view=mSettings&view=mTeam&view=modular&view=mNav".format(team_number+1)

    r = requests.get(url, headers=headers, cookies=espn_cookies)
    espn_raw_data = r.json()
    espn_draft_detail = espn_raw_data

    for i in range(0, 16):
        player_id = espn_draft_detail['teams'][team_number]['roster']['entries'][i]['playerId']

        # Defenses player id's are negative
        if player_id > 0:
            temp_url = "https://www.espn.com/nfl/player/_/id/{}".format(player_id)
            page = requests.get(temp_url)
            soup = BeautifulSoup(page.content, "html.parser")

            first_name = ((soup.find("span", {"class": "truncate min-w-0 fw-light"})).text.strip()).lower()
            first_name = ''.join(filter(whitelist.__contains__, first_name))
            last_name = ((soup.find("span", {"class": "truncate min-w-0"})).text.strip()).lower()
            last_name = ''.join(filter(whitelist.__contains__, last_name))
            position = ((soup.find("ul", {
                "class": "PlayerHeader__Team_Info list flex pt1 pr4 min-w-0 flex-basis-0 flex-shrink flex-grow nowrap"})).find_all(
                'li')[1].text.strip()).lower()

            # for some reason james robinson messed up
            if has_numbers(position):
                position = ((soup.find("ul", {
                    "class": "PlayerHeader__Team_Info list flex pt1 pr4 min-w-0 flex-basis-0 flex-shrink flex-grow nowrap"})).find_all(
                    'li')[2].text.strip()).lower()
            unavailable_players.append([first_name, last_name, position, player_id])

# print(unavailable_players)