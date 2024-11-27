import connection as conn

def create_table():
    
    connection = conn.get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            sql = f"""CREATE TABLE WORDS(
                id SERIAL PRIMARY KEY,
                word VARCHAR(60),
                theme VARCHAR(60)
                );
            """
            
            cursor.execute(sql)
            connection.commit()
        except Exception as e:
            print(f"Error al crear la tabla: {e}")
        finally:
            cursor.close()
            connection.close()

def insert_record(pos, data):
    
    connect = conn.get_connection()
    if connect:
        try:
            cursor = connect.cursor()
            # Creo la consulta sql
            sql = f"""
                INSERT INTO WORDS (word, theme)
                VALUES (%s, %s)
            """
            values = ((data.get("WORD")[pos], data.get("THEME")[pos]))
            #Ejecuto la consulta sql con los valores que se han pasado por parametros
            cursor.execute(sql, values)
            # Guarda los cambios en la base de datos
            connect.commit()
        except Exception as e:
            raise e
        
        finally:
            #Cerramos la conexión
            cursor.close()
            connect.close()

