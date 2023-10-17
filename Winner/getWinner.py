import json



def calculate_team_to_bet():
    with open("resources/json_id.json") as file:
        data = json.loads(file.read().replace("\'", "\""))
    for match in data["events"]:
        if (match["team1"]["odds"] is None):
            match.update({"winner": match["team2"]["name"]})
        elif (match["team2"]["odds"] is None):
            match.update({"winner": match["team1"]["name"]})
        elif (match["team1"]["odds"]["actual"] < match["team1"]["odds"]["expected"]):
            match.update({"winner" : match["team1"]["name"]})
        elif (match["team2"]["odds"]["actual"] < match["team2"]["odds"]["expected"]):
            match.update({"winner" : match["team2"]["name"]})
    file = open("resources/json_id.json", "w")
    file.write(str(data))