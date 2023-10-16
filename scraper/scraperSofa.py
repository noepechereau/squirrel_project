import json
import requests
import datetime

headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0',
        'Accept': '*/*',
        'Accept-Language': 'en-CA,en-US;q=0.7,en;q=0.3',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.sofascore.com/',
        'Origin': 'https://www.sofascore.com',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'If-None-Match': 'W/"9abd3b46f3"',
        'Cache-Control': 'max-age=0',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
}

headers['If-Modified-Since'] = 'Tues, 18 Jul 2023 00:00:00 GMT'
tomorrow = datetime.date.today() + datetime.timedelta(days=2)
tomorrow_str = tomorrow.strftime("%Y-%m-%d")
print(tomorrow_str)
endpoint = {
        "all_id": "https://api.sofascore.com/api/v1/sport/football/scheduled-events/" + tomorrow_str,
}

def get_id(endpoints, odds_info):
    data = json.loads((requests.get(endpoint[endpoints], headers=headers)).text)
    #print(data)
    for event in data["events"]:
        team1_name = event["homeTeam"]["name"]
        team2_name = event["awayTeam"]["name"]
        id = event["id"]

        event_info = {
            "team1": {
                "name": team1_name,
            },
            "team2": {
                "name": team2_name,
            },
            "id": id
        }
        odds_info["events"].append(event_info)
    return odds_info

def get_odds(odds_info, file):
    odds_final = {
        "events": []
    }
    #print(odds_info["events"])
    for id in odds_info["events"]:
        req = requests.get("https://api.sofascore.com/api/v1/event/" + str(id["id"]) + "/provider/1/winning-odds", headers=headers)
        if (req.status_code == 200):
            data = json.loads(req.text)
            if (data["home"] != None):
                actual1 = data["home"]["actual"]
                expected1 = data["home"]["expected"]
            else:
                actual1 = "NULL"
                expected1 = "NULL"
            if (data["away"] != None):
                actual2 = data["away"]["actual"]
                expected2 = data["away"]["expected"]
            else:
                actual2 = "NULL"
                expected2 = "NULL"
            if (actual1 == "NULL" or actual2 == "NULL") or (actual1 > expected1 and actual2 < expected2) or (actual1 < expected1 and actual2 > expected2):
                odds1 = {
                    "odds": {
                        "actual": actual1,
                        "expected": expected1,
                    }
                }
                odds2 = {
                    "odds": {
                        "actual": actual2,
                        "expected": expected2
                    }
                }
                #print(id)
                id["team1"].update(odds1)
                id["team2"].update(odds2)
                odds_final["events"].append(id)
    file = open("resources/" + file + ".json", "w")
    file.write(str(odds_final))


def test():
    req = requests.get("https://api.sofascore.com/api/v1/event/10752533/provider/1/winning-odds",
                       headers=headers)
    print(req.status_code)
