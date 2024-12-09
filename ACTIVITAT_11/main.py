from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from pydantic import BaseModel
import attemps_functs


app = FastAPI()

class Attempt(BaseModel):
    id_log: str
    letter: str
    is_correct: bool
    attemp_number: int
    
@app.get("/penjat/startButton")
async def get_button_start():
	return {"Text": "Començar partida"}


@app.post("/penjat/attemps")
async def get_attemps(attemp: Attempt):
	return attemps_functs.insertAttemp

""" @app.get("/penjat/aphabet")
async def get_attemps():
	return 

@app.get("/penjat/stats")
async def get_stats():
	return  """