from PyQt5.QtSql import QSqlDatabase, QSqlQuery
con = QSqlDatabase.addDatabase("QSQLITE")
con.setDatabaseName('db.sqlite')
con.open()

query = QSqlQuery()
print(query.exec("SELECT FIO, passport_number, by_whom_and_when_was_the_passport_issued FROM riders"))
print(con.isOpen())
# query.first()
# for result in query:
#     print(result)
# field_names = [f[0] for f in query.description]
# print(f"Поля в таблице riders \n {field_names}")
FIO, passport_number, by_whom_and_when_was_the_passport_issued, license_number, license_date, in_the_state = range(6)
# query.value(FIO)
while query.next():
    print(query.value(FIO), query.value(passport_number), query.value(by_whom_and_when_was_the_passport_issued))
con.close()
QSqlDatabase.removeDatabase(QSqlDatabase.database().connectionName())
print(QSqlDatabase.connectionNames())
print(con.isOpen())


# import sqlite3

# con = sqlite3.connect('db.sqlite')
# cur = con.cursor()
# cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
# print(cur.fetchall())
# # Дорогой SQL, верни все столбцы всех записей из таблицы movies;
# # символ * после SELECT означает "верни все поля найденных записей".
# cur.execute(
# # SELECT name,
# # release_year
#      '''
# SELECT *
# FROM riders

# ''')

# # Python превращает результирующую выборку в итерируемый объект,
# # который можно перебрать циклом:
# for result in cur:
#     print(result)
# field_names = [f[0] for f in cur.description]
# print(f"Поля в таблице riders \n {field_names}")
# # При получении данных из таблицы коммит не нужен.
# con.close()
