import psycopg2

connection = psycopg2.connect(
host="localhost",
database="postgres",
user="postgres",
password="123"
) 

cur = connection.cursor()

cur.execute("SELECT score FROM scores WHERE name = 'denis'")
data = cur.fetchone()
print(type(data[0]))