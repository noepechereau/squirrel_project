import json

from scraper.scraper_wina import scrape_wina


def fetch(targets):
    scrape_wina("football")
    with open("resources/football.json", "r") as file:
        data = json.loads(file.read())

    res = []
    matches = data["matches"]
    for match_id in matches:
        match = matches[match_id]
        for target in targets["events"]:
            print(target)
            name_a = match["competitor1Name"]
            name_b = match["competitor2Name"]
            if target["team1"]["name"] != name_a or target["team2"]["name"] != name_b:
                continue

            m = {"league": data["tournaments"][str(match["tournamentId"])]["tournamentName"]}
            if name_a == target["winner"]:
                m["winner"] = name_a
                m["loser"] = name_b
                m["winner_odd"] = data["odds"][str(data["bets"][str(match["mainBetId"])])][0]
                m["loser_odd"] = data["odds"][str(data["bets"][str(match["mainBetId"])])][2]
                m["winner_chance"] = target["team1"]["odds"]["actual"]
                m["loser_chance"] = target["team2"]["odds"]["actual"]
            else:
                m["winner"] = name_b
                m["loser"] = name_a
                m["winner_odd"] = data["odds"][str(data["bets"][str(match["mainBetId"])])][2]
                m["loser_odd"] = data["odds"][str(data["bets"][str(match["mainBetId"])])][0]
                m["winner_chance"] = target["team2"]["odds"]["actual"]
                m["loser_chance"] = target["team1"]["odds"]["actual"]
            res.append(m)

    return res
