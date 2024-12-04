from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from pydantic import BaseModel


app = FastAPI()

class Tematic(BaseModel):
    option: str
    
@app.get("/penjat/startButton", response_model=List[dict])
async def get_button_start():
	return 

@app.get("/penjat/secretWord", response_model=List[dict])
async def get_secretWord():
	return 
@app.get("/penjat/attemps", response_model=List[dict])
async def get_attemps():
	return 

@app.get("/penjat/aphabet", response_model=List[dict])
async def get_attemps():
	return 

@app.get("/penjat/stats", response_model=List[dict])
async def get_stats():
	return 