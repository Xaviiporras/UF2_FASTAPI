from fastapi import FastAPI
from typing import List
import functs as functs
from functs import Attempt
import schema

app = FastAPI()


    
@app.get("/penjat/startButton")
async def get_button_start():
	return {"Text": "Començar partida"}


@app.post("/penjat/attempts")
async def get_attempts(attempt: Attempt):
	return functs.insertAttempt(attempt)

@app.get("/penjat/alphabet/{language}", response_model=List[dict])
async def get_attemps(language: str):
	return schema.alphabets_schema(functs.get_alphabet(language))

""" @app.get("/penjat/stats")
async def get_stats():
	return  """