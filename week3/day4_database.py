import psycopg2

connection = psycopg2.connect("dbname=my_first_user")

cursor = connection.cursor()

cursor.execute("SELECT * FROM person_data WHERE first_name = %s;", (first_name,))
results = cursor.fetchall()
print(results)

cursor.close()
connection.close()
