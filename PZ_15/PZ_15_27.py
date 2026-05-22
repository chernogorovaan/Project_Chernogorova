'''
Задание: Вариант 27
Приложение ИНТЕРНЕТ-МАГАЗИН для некоторой организации. БД должна
содержать таблицу Продажи со следующей структурой записи: ФИО покупателя, товар,
единицу измерения (штуки, килограммы, литры), количество, стоимость.
'''
import sqlite3 as sq

with sq.connect('internet_magazine.db') as con:
    cur = con.cursor()
    
    cur.execute('DROP TABLE IF EXISTS Продажи')
    cur.execute('''
        CREATE TABLE Продажи (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            фио_покупателя TEXT,
            товар TEXT,
            единица_измерения TEXT,
            количество REAL,
            стоимость REAL
        )
    ''')
    
    cur.execute("INSERT INTO Продажи (фио_покупателя, товар, единица_измерения, количество, стоимость) VALUES ('Иванов И.И.', 'Яблоки', 'кг', 2, 300)")
    cur.execute("INSERT INTO Продажи (фио_покупателя, товар, единица_измерения, количество, стоимость) VALUES ('Петрова А.С.', 'Молоко', 'л', 1, 80)")
    
    cur.execute("SELECT * FROM Продажи")
    for row in cur:
        print(row)