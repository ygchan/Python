import psycopg2

conn = psycopg2.connect("dbname=dq, user=dq")
conn.close()
