from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from pydantic import BaseModel
import schema
import functions_endpoints as functs


app = FastAPI()

class Tematic(BaseModel):
    option: str


@app.get("/penjat/tematica/opcions", response_model=List[dict])
async def get_options():
	return schema.themes_schema(functs.get_options())