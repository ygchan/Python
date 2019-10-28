# Lesson 1: Connect()
import psycopg2

# Database name dq with user with the same name
conn = psycopg2.connect("dbname=dq user=dq")
conn.close()
# -----------------------------------------------------

# Lesson 2: Cursor()
import psycopg2

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute("select * from users;")

# Fetch all rows result into a list
all_results = cur.fetchall()

conn.close()

for result in all_results:
    print(result)
# -----------------------------------------------------
