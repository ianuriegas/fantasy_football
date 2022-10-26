import requests
from bs4 import BeautifulSoup

from universal.common_use import whitelist

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
team_number = 3
draft_picks = espn_draft_detail['teams'][team_number]['roster']['entries'][0]['playerId']

myTeam = []

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

        myTeam.append([first_name, last_name, position, my_team_id])

# print(myTeam)
# for info in range(0,len(myTeam)):
#     if info > 0:
#         format_name_curr = myTeam[info][0] + "-" + myTeam[info][1]
#         format_name_prev = myTeam[info-1][0] + "-" + myTeam[info-1][1]
#         output = "https://www.fantasypros.com/nfl/start/{}-{}.php".format(format_name_curr,format_name_prev)
#         print(output)