import connection as conn
from pydantic import BaseModel

class Attempt(BaseModel):
    id_log: str
    letter: str
    is_correct: bool
    attemp_number: int

def insertAttempt(attempt: Attempt):
    connect = conn.get_connection()

    if connect:
        try:
            cursor = connect.cursor()
            sql = f"""
                INSERT INTO ATTEMPT (log_id, letter, is_correct, attempt_number)
                VALUES (%s, %s, %s, %s)
            """
            values = (attempt.id_log, attempt.letter, attempt.is_correct, attempt.attemp_number)
            
            cursor.execute(sql, values)
            connect.commit()
            
            return {"message" : "Se ha introducido el registro correctamente"}
        
        except Exception as e:
            raise e
        finally:
            #Cerramos la conexión
            cursor.close()
            connect.close()

def get_alphabet(language: str) -> dict:
    connect = conn.get_connection()
    
    if connect:
        try:
            cursor = connect.cursor()
            sql = """
            SELECT LETTER
            FROM ALPHABET
            WHERE LANG = %s;
            """
            
            cursor.execute(sql, (language,))
            
            record = cursor.fetchall()
            
            return record
        
        except Exception as e:
            raise e
        finally:
            cursor.close()
            connect.close()