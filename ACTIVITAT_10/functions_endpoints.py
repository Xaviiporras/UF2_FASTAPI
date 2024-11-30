import insertDATA.connection as conn


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
