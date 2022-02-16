from bs4 import BeautifulSoup as bs
import requests

url = "https://www.espn.com/tennis/rankings"
data = requests.get(url).text
soup = bs(data, "html.parser")

ths = soup.find_all("th")
trs = soup.find_all("tr")

player_info_list = []


def get_player_info(url):
    data = requests.get(full_url).text
    soup = bs(data, "html.parser")

    table = soup.find(class_="infobox vcard")
    rows = soup.find_all("tr")

    player = {}

    for index, row in enumerate(rows):
        if index <= 1:
            continue
        elif len(row) == 1:
            continue
        elif index <= 12:
            try:
                dict_key = row.find("th").get_text().replace("\xa0", " ").replace("\n", " ")
                dict_value = row.find("td").get_text().replace("\xa0", " ").replace("\n", " ")
                player[dict_key] = dict_value

            except Exception as e:
                print(index)
                print(e)
        else:
            continue

    return player


for index, tr in enumerate(trs):
    player_info = {}

    if index == 0:
        continue
    else:
        tds = tr.find_all("td")
        row = [td.get_text() for td in tds]

        player_info["Rank"] = row[0]
        player_name = row[2]
        player_info["Name"] = player_name
        player_info["Points"] = row[3]

        wiki_url = "https://en.wikipedia.org/wiki/"
        relative_url = player_name.replace(" ", "_")
        full_url = wiki_url + relative_url

        player = get_player_info(full_url)
        for k, v in player.items():
            player_info[k] = v

    player_info_list.append(player_info)


import json

def save_data(title, data):
    with open(title, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

save_data("ATP_Player_Info_List.json", player_info_list)

import pandas as pd

df=pd.DataFrame(player_info_list)

df.to_excel("ATP_Player_List.xlsx", index=False, sheet_name="Top150_ATP_02_14_22")