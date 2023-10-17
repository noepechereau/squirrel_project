from scraper.scraperSofa import get_id, get_odds
from scraper.scraperWina import scrape_wina
from translation.translation import load_translations, translate

# odds_info = {
#     "events": []
# }
# get_odds(get_id("all_id", odds_info), "json_id")
# # test()

scrape_wina("football")
