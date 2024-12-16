from fastapi import FastAPI
from typing import List
import functs_crud as functs
from functs_crud import Alphabet

app = FastAPI()


#TAULA ALPHABET
@app.post("/penjat/createAlphabet")
async def insert_alphabet(alphabet: Alphabet):
	return functs.insertAlphabet(alphabet)

@app.get("/penjat/readAlphabet")

@app.delete("/penjat/delete_alphabet/{idTable}")
async def delete_alphabet(idTable: int):
	return (functs.delete_Record('ALPHABET', idTable))

#TAULA ATTEMPT

#TAULA LOG_RECORD

#TAULA USUARI

#TAULA WORDS