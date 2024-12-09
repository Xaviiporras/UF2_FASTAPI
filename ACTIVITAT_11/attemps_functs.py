import connection as conn

def insertAttemp():
    connect = conn.get_connection()

    if connect:
        try:
            cursor = connect.cursor()
            sql = f"""
                INSERT INTO ATTEMPT (log_id, letter, is_correct, attempt_number)
                VALUES (%s, %s, %s, %s)
            """
            values = ()
            
            cursor.execute(sql)

            
            return {"message" : "Se ha introducido el registro correctamente"}
        
        except Exception as e:
            raise e
        finally:
            #Cerramos la conexión
            cursor.close()
            connect.close()