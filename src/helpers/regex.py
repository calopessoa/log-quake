# patterns to filter...

# when a player is killed
kill_pattern = r"(?:^|\W)Kill(?:$|\W)"

# what caused(weapon or anything) that player's death
death_cause = r"((?<=by\s).*)"

# the player's name
players_pattern = r"((?<=n\\).*?(?=\\t))"

# who got the frag (player or world)
killer = r"([^ ]+)(?=\skilled)"
