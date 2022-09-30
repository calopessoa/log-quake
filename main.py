from src.helpers.game_number import *
from src.helpers.total_kills import *
from src.helpers.match_players import *
from src.helpers.player_kills import *

def main():
  results = []
  all_games = game_number()
  for game in all_games:
    all_kills = total_kills(game)
    all_players = match_players(game)
    all_frags = player_kills(game)
    results.append({
      "game": game.get('game'),
      "total_kills": all_kills,
      "players": all_players,
      "kills": all_frags,
    })
  return results

print(main())