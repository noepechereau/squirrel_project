import requests

from scraper.scraper import scrape
import json

from spreadsheet.spreadsheet import workbook_to_json

# scrape("football")
# file = open("resources/football.json")
# data = json.load(file)
# for match in data["sports"]["1"]["matches"]:
#     if data["matches"][str(match)]["competitor1Name"] is not None and data["matches"][str(match)]["competitor2Name"] is not None:
#         print(data["matches"][str(match)]["competitor1Name"], end="")
#         print(" VS ", end="")
#         print(data["matches"][str(match)]["competitor2Name"])
#
# file.close()

# headers = {
#     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0',
#     'Accept': '/',
#     'Accept-Language': 'en-CA,en-US;q=0.7,en;q=0.3',
#     # 'Accept-Encoding': 'gzip, deflate, br',
#     'Referer': 'https://www.sofascore.com/',
#     'Origin': 'https://www.sofascore.com/',
#     'DNT': '1',
#     'Connection': 'keep-alive',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'same-site',
#     'If-None-Match': 'W/"9abd3b46f3"',
#     'Cache-Control': 'max-age=0',
#     # Requests doesn't support trailers
#     # 'TE': 'trailers',
# }

# headers['If-Modified-Since'] = 'Tues, 18 Jul 2023 00:00:00 GMT'
#
# endpoints = {
#     "tournaments": "https://api.sofascore.com/api/v1/category/ID/unique-tournaments"
# }
#
#
# def get_tournaments():
#     tournaments = []
#     url = endpoints["tournaments"]
#     for i in [1, 7, 11, 19]:
#         data = json.loads((requests.get(url.replace("ID", str(i)), headers=headers)).text)
#         if "groups" in data:
#             tournaments += data["groups"][0]["uniqueTournaments"][:2]
#     for i in range(len(tournaments)):
#         tournaments[i] = tournaments[i]["id"]
#     return tournaments
#
# print(get_tournaments())

workbook_to_json('workbooks/languages.xlsx', 274)