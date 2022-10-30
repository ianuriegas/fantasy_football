import requests
from bs4 import BeautifulSoup

from teams.my_team import myTeam


def get_comparison(player_1, player_2):
    # get the simple format of the calculator we want to use
    temp_url = "https://fantasyfootballcalculator.com/start/{}-or-{}".format(player_1, player_2)
    page = requests.get(temp_url)
    soup = BeautifulSoup(page.content, "html.parser")

    # find the tags that say "strong" because that is where the data is that we want
    strong_tags = soup.find_all("strong")

    # get the text, (ex: "START" or "BENCH"), from these tags
    strong_tag_1 = strong_tags[0].text.strip()
    strong_tag_2 = strong_tags[1].text.strip()

    # return data in a list
    return [strong_tag_1, strong_tag_2]


def sort_comparison(position_arr):
    # we can't compare if there is only 1 player
    if len(position_arr) == 1:
        return position_arr

    # We can if there is more than 1 player (bubble sort because we need to compare each 1 by one down a line
    # we cannot simply compare a number)

    # iterate over array
    for i in range(len(position_arr)):

        # the ending number is the position in the array up to the index that is already sorted
        for j in range(0, len(position_arr) - i - 1):

            # we don't do any more comparison on the last person since it is sorted
            if j != len(position_arr) - 1:

                # get the comparison of the two players at the given index
                # format : ["START", "BENCH"] or ["BENCH","START]
                comparison = get_comparison(position_arr[j], position_arr[j + 1])

                # if the player to the left is "START" swap the player at the left with the
                # player on the right, vice versa
                if comparison[0] == "START":
                    new_temp = position_arr[j]
                    position_arr[j] = position_arr[j + 1]
                    position_arr[j + 1] = new_temp

    # return our sorted position_arr
    return position_arr


# function to get the bare name of a player instead of the formatted name
# ex: courtland-sutton --> Courtland Sutton
def get_correct_format(name):
    # replace "-" with spaces and title capitalizes the first letters of words at
    # the beginning of a string and after spaces
    name = (name.replace("-", " ")).title()
    return name


def main():
    # initialize our empty position lists
    qb = []
    rb = []
    wr = []
    te = []
    flex = []
    k = []
    # d = []
    # while True:
    #     defense = input("enter your defenses")
    #     d.append(defense)
    #     if "done":
    #         break

    # for loop used to sort players based on positions into their given position arrays
    for i in range(0, len(myTeam)):
        temp = myTeam[i][0] + "-" + myTeam[i][1]
        if myTeam[i][2] == "quarterback":
            qb.append(temp)
        elif myTeam[i][2] == "running back":
            rb.append(temp)
        elif myTeam[i][2] == "wide receiver":
            wr.append(temp)
        elif myTeam[i][2] == "tight end":
            te.append(temp)
        else:
            k.append(temp)

    # Use sort function to get sorted position lists
    sorted_qb = sort_comparison(qb)
    sorted_rb = sort_comparison(rb)
    sorted_wr = sort_comparison(wr)
    sorted_te = sort_comparison(te)
    sorted_k = sort_comparison(k)

    # we need more than 2 RB
    if len(sorted_rb) > 2:
        flex.append(sorted_rb[len(sorted_rb) - 3])
    # we need more than 2 WR
    if len(sorted_wr) > 2:
        flex.append(sorted_wr[len(sorted_wr) - 3])
    # we need more than 1 TE
    if len(sorted_te) > 1:
        flex.append(sorted_te[len(sorted_te) - 2])

    # Use sort function to get sorted flex position list
    sorted_flex = sort_comparison(flex)

    print("Best Lineup from your current players")

    # 1 QB
    qb1 = get_correct_format(sorted_qb[len(sorted_qb) - 1])
    print("QB :", qb1)

    # 2 RB

    rb1 = get_correct_format(sorted_rb[len(sorted_rb) - 1])
    print("RB :", rb1)

    rb2 = get_correct_format(sorted_rb[len(sorted_rb) - 2])
    print("RB :", rb2)

    # 2 WR

    wr1 = get_correct_format(sorted_wr[len(sorted_wr) - 1])
    print("WR :", wr1)

    wr2 = get_correct_format(sorted_wr[len(sorted_wr) - 2])
    print("WR :", wr2)

    # 1 TE
    te1 = get_correct_format(sorted_te[len(sorted_te) - 1])
    print("TE :", te1)

    # 1 Flex (RB, WR or TE)
    flex1 = get_correct_format(sorted_flex[len(sorted_flex) - 1])
    print("FLEX :", flex1)

    # 1 K
    k1 = get_correct_format(sorted_k[len(sorted_k) - 1])
    print("K :", k1)


if __name__ == "__main__":
    main()
