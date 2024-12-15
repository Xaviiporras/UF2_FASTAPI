import psycopg2

def get_connection():
    try:
        # Establece la conexión con la base de datos
        conn = psycopg2.connect(
            database="postgres",
            user='user_postgres',
            password='pass_postgres',
            host='localhost',
            port='5432'
        )
        # Devuelve la conexión
        return conn
    except Exception as e:
        #En caso de que no se pueda establecer la conexión mostrara el error
        print(f"No se ha podido establecer la conexión: {e}")