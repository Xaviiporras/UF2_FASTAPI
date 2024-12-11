def alphabet_schema(alphabet) -> dict:
	return {"alphabet": alphabet[0]
            }

def alphabets_schema(alphabets) -> dict:
	return[alphabet_schema(alphabet) for alphabet in alphabets]