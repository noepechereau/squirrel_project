from scraper.scraper import scrape
import json
from scraper.scraper import get_sofascore_page

if __name__ == "__main__":

    website = "sofascore"
    endpoint = "gold"
    print(get_sofascore_page("https://www.sofascore.com/betting-tips-today/football"))
    # scrape(website, endpoint)
    # file = open("resources/football.json")
    # data = json.load(file)
    #
    # for match in data["sports"]["1"]["matches"]:
    #     if data["matches"][str(match)]["competitor1Name"] is not None and data["matches"][str(match)]["competitor2Name"] is not None:
    #         print(data["matches"][str(match)]["competitor1Name"], end="")
    #         print(" VS ", end="")
    #         print(data["matches"][str(match)]["competitor2Name"])
    #
    # file.close()
