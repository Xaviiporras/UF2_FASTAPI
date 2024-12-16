import connection as conn
from pydantic import BaseModel

class Alphabet(BaseModel):
    letter: str
    lang: str

            
def insertAlphabet(alphabet: Alphabet):
    connect = conn.get_connection()

    if connect:
        try:
            cursor = connect.cursor()
            sql = f"""
                INSERT INTO ALPHABET (letter, lang)
                VALUES (%s, %s)
            """
            values = (
                alphabet.letter,
                alphabet.lang
            )

            cursor.execute(sql, values)
            connect.commit()

            return {"message": "Se ha introducido el registro correctamente"}

        except Exception as e:
            raise e
        finally:
            cursor.close()
            connect.close()
            
def read_Record(language: str) -> dict:
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

def delete_Record(tableName, idTable: int):
    connect = conn.get_connection()

    if connect:
        try:
            cursor = connect.cursor()
            allowed_tables = ['ALPHABET', 'ATTEMPT', 'LOG_RECORD', 'USUARI', 'WORDS']  # Lista de tablas permitidas para evitar sql injection
            if tableName not in allowed_tables:
                raise ValueError(f"Tabla no permitida: {tableName}")
            
            sql = f"""
            DELETE FROM {tableName}
            WHERE ID = %s;
            """
            
            cursor.execute(sql, (idTable,))

            connect.commit()

            return {"message": "Se ha borrado el registro correctamente"}

        except Exception as e:
            raise e
        finally:
            cursor.close()
            connect.close()