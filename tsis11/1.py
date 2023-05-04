import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    port = '5432',
    user='postgres',
    password='poiu0987uiop'
)

table = config.cursor()
def outputalldata():
    table.execute("SELECT username,number from phonebook1")
    myresult = table.fetchall()
    print('      |')
    print("NAME  |  NUMBER")
    print('------------------------------')

    for i in myresult:
        print(i[0],' | ',i[1])
outputalldata()