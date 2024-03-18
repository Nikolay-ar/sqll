import sqlite3

# Если в текущей директории нет файла db.sqlite -
# он будет создан; сразу же будет создано и соединение с базой.
# Если файл существует, функция connect просто подключится к базе.
con = sqlite3.connect('db.sqlite')

# Создаём специальный объект cursor для работы с БД.
# Вся дальнейшая работа будет вестись через методы этого объекта.
cur = con.cursor()

# Готовим SQL-запросы.
# Для читаемости кода запрос обрамлён в тройные кавычки и разбит построчно.

# cur.execute('''
# CREATE TABLE IF NOT EXISTS directors(
#     id INTEGER PRIMARY KEY,
#     name TEXT,
#     birthday_year INTEGER
# );
# ''')
# cur.execute('''
# CREATE TABLE IF NOT EXISTS movies(
#     id INTEGER PRIMARY KEY,
#     name TEXT,
#     type TEXT,
#     release_year INTEGER
# );
# ''')

# cur.executescript('''
# ALTER TABLE trucks ADD COLUMN truck_num INTEGER;
# ALTER TABLE trailers ADD COLUMN trailer_num INTEGER;
# ''')

# ALTER TABLE riders FOREIGN KEY(truck_id) REFERENCES trucks(id);

# ALTER TABLE riders FOREIGN KEY(trailer_id) REFERENCES trailers(id);
cur.execute('''
CREATE TABLE IF NOT EXISTS riders(
    id INTEGER PRIMARY KEY,
            
    FIO TEXT,
    passport_number INTEGER,
    by_whom_and_when_was_the_passport_issued INTEGER,
    license_number INTEGER,
    license_date INTEGER,
    truck_id INTEGER,
    trailer_id INTEGER,
    FOREIGN KEY (truck_id) REFERENCES trucks (id),
    FOREIGN KEY (trailer_id) REFERENCES trailers (id)
);
''')

# cur.execute('''
# CREATE TABLE IF NOT EXISTS trucks(
#     id INTEGER PRIMARY KEY,
#     truck_name TEXT
#     truck_number INTEGER);
# ''')
# cur.execute('''
# CREATE TABLE IF NOT EXISTS trailers(
#     id INTEGER PRIMARY KEY,
#     trailer_name TEXT
#     trailer_number INTEGER);
# ''')

# cur.execute('''
# DROP TABLE IF EXISTS riders;
# ''')

# Применяем запросы.
# Запросы, переданные в cur.execute(), не будут выполнены до тех пор,
# пока не вызван метод commit().
con.commit()
# Закрываем соединение с БД.
con.close()
