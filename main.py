import time
import requests
import json


eveBaseURL = "https://esi.evetech.net/latest/universe/ids/"
eveKeys = {"universe": "universe/", "id": "ids/"}

def evetesting(names: list) -> dict:
    response = requests.post(eveBaseURL, json=names)
    content = response.content.decode('utf8').replace("'", '"')
    data = json.loads(content)
    return data

zkillboardBaseURL = "https://zkillboard.com/api/"
zkillboardStats = "stats/characterID/"
zkillboardKillmail = "kills/characterID/"

def zkillboardCharactertesting(characterid):
    url = zkillboardBaseURL + zkillboardStats + f"{characterid}/"
    response = requests.get(url)
    content = response.content.decode('utf8')
    zdata = json.loads(content)
    return zdata

def zkillboardKillmailtesting(characterid):
    url = zkillboardBaseURL + zkillboardKillmail + f"{characterid}/"
    response = requests.get(url)
    content = response.content.decode('utf8')
    zdata = json.loads(content)
    return zdata

IDs = evetesting(["", "", ""])
characters: list = IDs.get("characters")
characterIDs = []
for item in characters:
    characterIDs.append(item["id"])

for item in characterIDs:
    try:
        zkilldata = zkillboardCharactertesting(item)
        zkillmail = zkillboardKillmailtesting(item)
    except Exception as e:
        print(e)
        continue
    time.sleep(1)
    continue
