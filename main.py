from scraper.scraperSofa import get_id, get_odds
from winner.getWinner import calculate_team_to_bet

odds_info = get_odds(get_id("all_id"), "json_id")
calculate_team_to_bet()
