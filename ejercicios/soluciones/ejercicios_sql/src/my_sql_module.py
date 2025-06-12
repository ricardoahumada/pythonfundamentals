import psycopg2


def create_server_connection(PGHOST, PGDATABASE, PGUSER, PGPASSWORD):

    conn = None
    try:
        conn = psycopg2.connect(database=PGDATABASE, user=PGUSER,
                                password=PGPASSWORD, host=PGHOST, port=5432)
        print("Database conn successful")
    except Exception as err:
        print(f"Error: '{err}'")

    return conn
