import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    port = '5432',
    user='postgres',
    password='poiu0987uiop'
)

table = config.cursor()
name = input("input your name: ")
number = input("input your number: ")

def update(name,number):

    table.execute("SELECT username FROM phonebook1 WHERE username = %s",(name,))
    myresult = table.fetchone()

    if myresult:
        table.execute("UPDATE phonebook1 SET number = %s WHERE username = %s",(number,name))

    else:
        table.execute("INSERT INTO phonebook1 VALUES (%s,%s)",(name,number))
    config.commit()

update(name,number)