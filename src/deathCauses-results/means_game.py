from helperGame import helperGamer
from helperMeans import helperMeans

# returns all matches and within each casuses of death per game;
def means_of_death_game():
  results = []
  all_games = helperGamer()
  for game in all_games:
    all_kills = helperMeans(game)
    if all_kills == {}:
      all_kills = 'no deaths'
    results.append({
      "game": game.get('game'),
      "kills_by_means": all_kills,
    })
  return results

print(means_of_death_game())