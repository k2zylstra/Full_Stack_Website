import psycopg2 as ps





connnection = ps.connect('dbname=weatherdb, user=postgres, password=Kieran')
cursor = connection.cursor()
p = cursor.execute('select * from daily_weather')

print(p)

cursor.close()
connection.close()
