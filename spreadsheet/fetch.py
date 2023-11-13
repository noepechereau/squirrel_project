import json

from scraper.scraper_wina import scrape_wina


def fetch(targets):
    scrape_wina("football")
    with open("resources/football.json", "r") as file:
        data = json.loads(file.read())

    res = []
    matches = data["matches"]
    print(len(targets["events"]))
    for match_id in matches:
        match = matches[match_id]
        for target in targets["events"]:
            name_a = match["competitor1Name"]
            name_b = match["competitor2Name"]
            if target["team1"]["name"] != name_a or target["team2"]["name"] != name_b:
                continue

            m = [data["tournaments"][str(match["tournamentId"])]["tournamentName"]]
            if name_a == target["winner"]:
                m.append(name_a)
                m.append(name_b)
                m.append(data["odds"][str(data["bets"][str(match["mainBetId"])]["outcomes"][0])])
                m.append(data["odds"][str(data["bets"][str(match["mainBetId"])]["outcomes"][2])])
                m.append(target["team1"]["odds"]["actual"])
                m.append(target["team2"]["odds"]["actual"])
            else:
                m.append(name_b)
                m.append(name_a)
                m.append(data["odds"][str(data["bets"][str(match["mainBetId"])]["outcomes"][2])])
                m.append(data["odds"][str(data["bets"][str(match["mainBetId"])]["outcomes"][0])])
                m.append(target["team2"]["odds"]["actual"])
                m.append(target["team1"]["odds"]["actual"])
            res.append(m)

    return res
