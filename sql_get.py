import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

# Дорогой SQL, верни все столбцы всех записей из таблицы movies;
# символ * после SELECT означает "верни все поля найденных записей".
cur.execute(
# SELECT name,
# release_year
     '''
SELECT gross,
       type,
       name,
       release_year
FROM movies
ORDER BY type DESC, name
LIMIT 12 OFFSET 0
;''')


# Python превращает результирующую выборку в итерируемый объект,
# который можно перебрать циклом:
for result in cur:
    print(result)

# При получении данных из таблицы коммит не нужен.
con.close()
