# Country Roads, Take Mahomes
import requests
from bs4 import BeautifulSoup

# from my_team import whitelist
from universal.common_use import whitelist

url = "https://fantasy.espn.com/apis/v3/games/ffl/seasons/2022/segments/0/leagues/898997769?rosterForTeamId=1&view=mDraftDetail&view=mLiveScoring&view=mMatchupScore&view=mPendingTransactions&view=mPositionalRatings&view=mRoster&view=mSettings&view=mTeam&view=modular&view=mNav"

espn_cookies = {"swid": "{11F62244-D8C5-462F-BA6C-F2393EF28D6E}",
                "espn_s2": "AEAUa8KsAzRddwUrL86iQvSc1IfBHH2r4BPNCamr%2FBL7ciB95qYcuj1UThlKiOq0wExF1btyTNicS6Og49oQxX%2BrIRktL8wJKR8u8hQVvwg8lSFMXsssrad09v2wMJ0i3xldRmfoAS30nXJrvVtt8Eaa6Vi9yGVvVyvG1%2BEBZw8R9iqj87%2F14XAlWPdoaF5s7n2hAkPKYfrlrAu5%2BW5AKRcoWKS3%2FExafuyZAERvLSNUGht3LHChwBquTYa0rh8aHPQoeUd6ZJusjAV6WK3D1U9O"}

headers = {
 'Connection': 'keep-alive',
 'Accept': 'application/json, text/plain, */*',
 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
}

r = requests.get(url, headers=headers, cookies=espn_cookies)
espn_raw_data = r.json()
# team_info = espn_raw_data[0]
espn_draft_detail = espn_raw_data

team_number = 0
draft_picks = espn_draft_detail['teams'][team_number]['roster']['entries'][0]['playerId']

team_0 = []

for i in range(0, 16):
    my_team_id = espn_draft_detail['teams'][team_number]['roster']['entries'][i]['playerId']

    # Defenses are negative
    if my_team_id > 0:
        temp_url = "https://www.espn.com/nfl/player/_/id/{}".format(my_team_id)
        page = requests.get(temp_url)
        soup = BeautifulSoup(page.content, "html.parser")

        first_name = ((soup.find("span", {"class": "truncate min-w-0 fw-light"})).text.strip()).lower()
        first_name = ''.join(filter(whitelist.__contains__, first_name))
        last_name = ((soup.find("span", {"class": "truncate min-w-0"})).text.strip()).lower()
        last_name = ''.join(filter(whitelist.__contains__, last_name))
        position = ((soup.find("ul", { "class" : "PlayerHeader__Team_Info list flex pt1 pr4 min-w-0 flex-basis-0 flex-shrink flex-grow nowrap"})).find_all('li')[2].text.strip()).lower()

        team_0.append([first_name, last_name, position, my_team_id])

# print(team_0)