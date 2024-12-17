import psycopg2


def create_server_connection():

    PGHOST = '...'
    PGDATABASE = '...'
    PGUSER = '...'
    PGPASSWORD = '...

    conn = None
    try:
        conn = psycopg2.connect(database=PGDATABASE, user=PGUSER,
                                password=PGPASSWORD, host=PGHOST, port=5432)
        print("Database conn successful")
    except Error as err:
        print(f"Error: '{err}'")

    return conn



# INSERT
""" conn = create_server_connection()

cur = conn.cursor()

cur.execute("INSERT INTO datafund_students(student_name, student_email, student_age) VALUES('Pedro','p@p.es',34)")
cur.execute("INSERT INTO datafund_students(student_name, student_email, student_age) VALUES('Anna','a@a.es',43)")
cur.execute("INSERT INTO datafund_students(student_name, student_email, student_age) VALUES('Luisa','l@l.es',54)")
cur.execute("INSERT INTO datafund_students(student_name, student_email, student_age) VALUES('Juan','j@j.es',21)")

conn.commit()
cur.close()
conn.close() """


# SELECT
conn = create_server_connection()

cur = conn.cursor()
cur.execute('SELECT student_name, student_email FROM datafund_students;')
rows = cur.fetchall()
conn.commit()
cur.close()
conn.close()

print(type(rows))

for row in rows:
    print(row)


# UPDATE
conn = create_server_connection()

cur = conn.cursor()
cur.execute("UPDATE datafund_students SET student_age = 23 WHERE student_name = 'Juan';")
conn.commit()
cur.close()
conn.close()

# DELETE
conn = create_server_connection()

cur = conn.cursor()
cur.execute("""DELETE from datafund_students WHERE student_name = 'Luisa'""");
conn.commit()
cur.close()
conn.close()



# JOIN
conn = create_server_connection()

cur = conn.cursor()
cur.execute("""SELECT DISTINCT p.customerNumber, p.checkNumber, p.paymentDate, p.amount FROM payments p 
            LEFT JOIN sales s ON s.customerNumber=p.customerNumber WHERE s.customerNumber IS NOT NULL ORDER BY p.customerNumber""")

rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()