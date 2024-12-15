def start_schema(text) -> dict:
	return {"text": text[0]
            }

def starts_schema(texts) -> dict:
	return[start_schema(text) for text in texts]

def attempt_schema(attempt) -> dict:
	return {"attempts": attempt[0]
            }

def attempts_schema(attempts) -> dict:
	return[attempt_schema(attempt) for attempt in attempts]

def alphabet_schema(alphabet) -> dict:
	return {"alphabet": alphabet[0]
            }

def alphabets_schema(alphabets) -> dict:
	return[alphabet_schema(alphabet) for alphabet in alphabets]


def stat_schema(stat) -> dict:
	return {"name": stat[0],
			"ppa": stat[1],
			"total_games": stat[2],
			"games_won": stat[3],
			"best_game_date": stat[4],
			"best_game_points": stat[5]
            }

def stats_schema(stats) -> dict:
	return[stat_schema(stat) for stat in stats]