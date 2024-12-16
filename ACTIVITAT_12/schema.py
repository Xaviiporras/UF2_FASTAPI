""" def sta_schema(stat) -> dict:
	return {"name": stat[0],
			"ppa": stat[1],
			"total_games": stat[2],
			"games_won": stat[3],
			"best_game_date": stat[4],
			"best_game_points": stat[5]
            }

def stats_schema(stats) -> dict:
	return[stat_schema(stat) for stat in stats] """