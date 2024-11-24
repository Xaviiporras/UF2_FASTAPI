from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel
from typing import List
import users_sch
import read

app3 = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    surname: str

@app3.get("/users", response_model=List[dict])
async def read_users():
	return users_sch.users_schema(read.read())