import connection as conn
from main import Attempt

def insertAttemp(attempt: Attempt):
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

            
            return {"message" : "Se ha introducido el registro correctamente"}
        
        except Exception as e:
            raise e
        finally:
            #Cerramos la conexión
            cursor.close()
            connect.close()