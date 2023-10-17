import json


def calculate_team_to_bet():
    with open("resources/json_id.json", "r") as file:
        data = json.loads(file.read())
    for i in range(len(data["events"])):
        if data["events"][i]["team1"]["odds"] is None or data["events"][i]["team1"]["odds"]["actual"] == "NULL":
            data["events"][i].update({"winner": data["events"][i]["team2"]["name"]})
        elif data["events"][i]["team2"]["odds"] is None or data["events"][i]["team2"]["odds"]["actual"] == "NULL":
            data["events"][i].update({"winner": data["events"][i]["team1"]["name"]})
        elif data["events"][i]["team1"]["odds"]["actual"] < data["events"][i]["team1"]["odds"]["expected"]:
            data["events"][i].update({"winner": data["events"][i]["team1"]["name"]})
        elif data["events"][i]["team2"]["odds"]["actual"] < data["events"][i]["team2"]["odds"]["expected"]:
            data["events"][i].update({"winner": data["events"][i]["team2"]["name"]})
    file = open("resources/json_id.json", "w")
    file.write(json.dumps(data))
    return data
