import json

from scraper.scraperWina import scrape_wina


def fetch(targets):
    scrape_wina("football")
    data = None
    with open("resources/football.json", "r") as file:
        data = json.loads(file.read())

    res = []
    matches = data["matches"]
    for match_id in matches:
        match = matches[match_id]
        for target in targets["events"]:
            name_a = match["Competitor1Name"]
            name_b = match["Competitor2Name"]
            if target["team1"]["name"] != name_a or target["team2"]["name"] != name_b:
                continue

    return res
