import json
from collections import Counter
from src.deathCauses.means_game import means_of_death_game
from src.helpers.game_number import *
from src.helpers.total_kills import *
from src.helpers.match_players import *
from src.helpers.player_kills import *
from src.helpers.decrement_kills import *

def main():
  results = []
  all_games = game_number()
  for game in all_games:
    all_kills = total_kills(game)
    all_players = match_players(game)
    frags = player_kills(game)
    penalties = decrement_kills(game)
    scoreOp = {key: frags[key] + penalties.get(key, 0) for key in frags}
    score = Counter(scoreOp).most_common()
    results.append({
      "game": game.get('game'),
      "total_kills": all_kills,
      "players": all_players,
      "kills": dict(score),
    })

    death_causes = means_of_death_game()

  with open('front-end/src/dataJson/matches.json', 'w+') as file:
    json.dump(results, file)

  with open('front-end/src/dataJson/meansOfDeath.json', 'w+') as file:
    json.dump(death_causes, file)

print(f'Relatório gerado! Arquivos json criados em front-end/src/dataJson')
print(main())


