import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    port = '5432',
    user='postgres',
    password='poiu0987uiop'
)

table = config.cursor()

data = {
    'dariga':'87052223456',
    'ayazhan':'87073999206',
    'alina':'87054442846',
    'baha':'21312',
    'tileuhan':'dasdad',
    '123123':'asdadas'

}

incorrect = []

def sort(data):
    for key,value in data.items():
        if key.isalpha() == False:
            incorrect.append((key,value))
            continue
        if value.isdigit() == False:
            incorrect.append((key,value))
            continue
        if len(value)!=11:
            incorrect.append((key,value))
            continue
        table.execute("INSERT INTO phonebook1 VALUES (%s,%s)",(key,value))
        config.commit()
sort(data)
print(incorrect)