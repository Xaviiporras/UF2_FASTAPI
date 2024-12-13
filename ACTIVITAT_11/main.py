from fastapi import FastAPI
from typing import List
import functs as functs
from functs import Attempt
import schema

app = FastAPI()


    
@app.get("/penjat/startButton", response_model=List[dict])
async def get_button_start():
	return schema.starts_schema(functs.get_startText())


@app.post("/penjat/attempts")
async def get_attempts(attempt: Attempt):
	return functs.insertAttempt(attempt)

@app.get("/penjat/alphabet/{language}", response_model=List[dict])
async def get_attemps(language: str):
	return schema.alphabets_schema(functs.get_alphabet(language))

@app.get("/penjat/stats/{name}", response_model=List[dict])
async def get_stats(name: str):
	return schema.stats_schema(functs.insertStats(name))