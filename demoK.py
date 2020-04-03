import psycopg2 as ps





connection = ps.connect("dbname='weatherdb' host='localhost' user='postgres' password='Kieran'")
cursor = connection.cursor()
cursor.execute('select * from daily_weather;')
print(cursor.fetchall())
connection.commit()


cursor.close()
connection.close()
