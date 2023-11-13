from scraper.scraper_sofa import get_id, get_odds
from spreadsheet.fetch import fetch
from translation.translation import load_translations
from winner.get_winner import calculate_team_to_bet
from spreadsheet.spreadsheet import write_xlsx

load_translations()
get_odds(get_id("all_id"), "json_id")
matches = fetch(calculate_team_to_bet())
print(len(matches))
write_xlsx(matches)