
import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cur.fetchall())
# Дорогой SQL, верни все столбцы всех записей из таблицы movies;
# символ * после SELECT означает "верни все поля найденных записей".
cur.execute(
# SELECT name,
# release_year
     '''
SELECT *
FROM riders_trucks

''')

# Python превращает результирующую выборку в итерируемый объект,
# который можно перебрать циклом:
for result in cur:
    print(result)
fieldnames=[f[0] for f in cur.description]
print(f"Поля в таблице riders \n {fieldnames}")
# При получении данных из таблицы коммит не нужен.
con.close()
