import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    port = '5432',
    user='postgres',
    password='poiu0987uiop'
)
table = config.cursor()
answer = input("You want to delete by name or phone? ")

if answer == 'name':
    delete = input('what user you want to delete?: ')
    table.execute(f"DELETE FROM phonebook1 WHERE username = '{delete}'")
elif answer == 'number':
    delete = input('what phone you want to delete?: ')
    table.execute(f"DELETE FROM phonebook1 WHERE number = '{delete}'")

config.commit()
table.close()
config.close()