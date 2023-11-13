from scraper.scraper_sofa import get_id, get_odds
from spreadsheet.fetch import fetch
from winner.get_winner import calculate_team_to_bet

get_odds(get_id("all_id"), "json_id")
#matches = fetch(calculate_team_to_bet())
#[print(m) for m in matches]
