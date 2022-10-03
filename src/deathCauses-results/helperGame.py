def helperGamer():
  init_games = []
  index_number = 0
  def conditional(i):
    if i+1 == len(init_games):
      return index_number
    else:
      return init_games[i+1]

  with open ('src/log/index.log', 'rt') as games_list:
    for index, line in enumerate(games_list):
      index_number = index
      if 'InitGame' in line:
        init_games.append(index+1)

  results = []
  for index, _ in enumerate(init_games):
      results.append({
        "game": index+1,
        "InitGame": init_games[index]-1,
        "ShutdownGame": conditional(index)-1,
      })
  return results
