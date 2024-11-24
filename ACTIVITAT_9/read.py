import connection as conn

def read():
    #Establece la conexión
    connect = conn.get_connection()
    if connect:
        try:
            cursor = connect.cursor()
            #generamos la consulta sql
            sql = "SELECT * FROM USERS"
            
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