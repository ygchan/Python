import psycopg2

# Database name dq with user with the same name
conn = psycopg2.connect("dbname=dq user=dq")
conn.close()
