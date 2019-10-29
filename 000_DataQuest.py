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

# Lesson 3: Execute(), create table SQL
import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")

cur = conn.cursor()
cur.execute("""
    create table employees(
        id integer primary key,
        email text ,
        name text ,
        address text 
    );    
""")
# -----------------------------------------------------

# Lesson 4: Begin, Commit
import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")

cur = conn.cursor()
cur.execute("""
   select * from users;
""")
# -----------------------------------------------------

# Lesson 5: query_string and commit

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
query_string = """
    CREATE TABLE users(
        id integer PRIMARY KEY, 
        email text,
        name text,
        address text
    );
"""

cur = conn.cursor()
cur.execute(query_string)
conn.commit()
conn.close()
# -----------------------------------------------------

# Lesson 6: Different state
import psycopg2
conn1 = psycopg2.connect("dbname=dq user=dq")
cur1 = conn1.cursor()
cur1.execute("delete from users")
conn1.commit()

cur1.execute("INSERT INTO users VALUES (%s, %s, %s, %s);", (1, 'alice@dataquest.io', 'Alice', '99 Fake Street'))
conn2 = psycopg2.connect("dbname=dq user=dq")
cur2 = conn2.cursor()
# add your code here

query_string = "select * from users;"

cur1.execute(query_string)
view1_before = cur1.fetchall()

cur2.execute(query_string)
view2_before = cur2.fetchall()

conn1.commit()

cur2.execute(query_string)
view2_after = cur2.fetchall()
# -----------------------------------------------------

# Lesson 7: update string format
import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")

cur = conn.cursor()
# Try to use a list for single item, tuple for multiple
# or (1,) for a single tuple.
cur.execute("insert into users values(%s, %s, %s, %s);",
            (2, "George@Gmail.com", "George", "123, Fake Street"))

conn.commit()
conn.close()
# -----------------------------------------------------
