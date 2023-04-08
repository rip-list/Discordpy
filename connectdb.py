import sqlite3


def fib(n):
    a, b = 0, 1

    for _ in range(n):
        yield a
        a, b = b, a + b


connection = sqlite3.connect('usr_info.db')
cursor = connection.cursor()
with connection:
    cursor.execute('''CREATE TABLE IF NOT EXISTS fib (
                            calculated_value INTEGER)''')
    cursor.executemany('INSERT INTO fib VALUES (?)',
                       [(str(x),) for x in fib(10)])

cursor.execute('SELECT * FROM fib')
print(cursor.fetchall())
