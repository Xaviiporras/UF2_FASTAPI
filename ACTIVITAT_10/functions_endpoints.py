import insertDATA.connection as conn
import random


def get_options():
    #Establece la conexión
    connect = conn.get_connection()

    if connect:
        try:

            cursor = connect.cursor()
            #generamos la consulta sql
            sql = "SELECT DISTINCT THEME FROM WORDS"
            
            cursor.execute(sql)
            #Se obtienen todos los registros en una lista de tuplas
            records = cursor.fetchall()
            return records
        
        except Exception as e:
            raise e
        finally:
            #Cerramos la conexión
            cursor.close()
            connect.close()
            
def get_random_word(option: str) -> dict:
    connect = conn.get_connection()
    
    if connect:
        try:
            cursor = connect.cursor()
            sql = """
            SELECT WORD
            FROM WORDS
            WHERE THEME = %s
            ORDER BY RANDOM() LIMIT 1;
            """
            
            cursor.execute(sql, (option,))
            
            record = cursor.fetchall()
            
            if not record:
                return {"option": None}
            else:
                return record
        
        except Exception as e:
            raise e
        finally:
            cursor.close()
            connect.close()
