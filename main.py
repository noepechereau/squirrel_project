from scraper.scraperSofa import get_id, get_odds

odds_info = {
    "events": []
}
get_odds(get_id("all_id", odds_info), "json_id")
# test()
