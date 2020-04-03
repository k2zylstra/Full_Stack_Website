import psycopg2 as ps

try:
    connection = ps.connect("dbname='template1' user='postgres' host='localhost' password='12345678'")
except:
    print ("I am unable to connect to the database")


cursor = connection.cursor()
p = cursor.execute('select *')

print(p)

cursor.close()
connection.close()
