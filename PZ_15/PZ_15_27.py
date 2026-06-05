"""
Вариант 27
Приложение ИНТЕРНЕТ-МАГАЗИН для некоторой организации. БД должна
содержать таблицу Продажи со следующей структурой записи: ФИО покупателя, товар,
единицу измерения (штуки, килограммы, литры), количество, стоимость.

"""

import sqlite3
import sys

try:
    from sample_data import SAMPLE_DATA
    print("Файл с данными успешно загружен")
except ImportError:
    print("Ошибка: файл sample_data.py не найден!")
    print("Убедитесь, что файл sample_data.py находится в той же папке.")
    sys.exit(1)

DB_NAME = "internet_shop.db"
TABLE_NAME = "Продажи"


def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row 
    return conn


def create_table() -> None:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fio TEXT NOT NULL,
            product TEXT NOT NULL,
            unit TEXT NOT NULL,
            quantity REAL NOT NULL,
            cost REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def insert_sample_data() -> None:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {TABLE_NAME}")
    count = cursor.fetchone()[0]
    
    if count == 0:
        cursor.executemany(f"""
            INSERT INTO {TABLE_NAME} (fio, product, unit, quantity, cost)
            VALUES (?, ?, ?, ?, ?)
        """, SAMPLE_DATA)
        conn.commit()
        print(f"Добавлено {len(SAMPLE_DATA)} начальных записей из sample_data.py.")
    else:
        print(f"В таблице уже есть {count} записей. Новые не добавлены.")
    conn.close()


def add_record() -> None:
    print("\n--- Добавление новой продажи ---")
    try:
        fio = input("ФИО покупателя: ").strip()
        product = input("Товар: ").strip()
        unit = input("Единица измерения (штуки/килограммы/литры): ").strip()
        quantity = float(input("Количество: "))
        cost = float(input("Стоимость: "))

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(f"""
            INSERT INTO {TABLE_NAME} (fio, product, unit, quantity, cost)
            VALUES (?, ?, ?, ?, ?)
        """, (fio, product, unit, quantity, cost))
        conn.commit()
        print("Запись добавлена.")
        conn.close()
    except ValueError:
        print("Ошибка: количество и стоимость должны быть числами.")
    except Exception as e:
        print(f"Ошибка при добавлении: {e}")


def search_records() -> None:
    print("\n--- Поиск записей ---")
    print("1. Поиск по ФИО покупателя")
    print("2. Поиск по товару (частичное совпадение)")
    print("3. Поиск по диапазону стоимости")

    choice = input("Выберите вариант (1-3): ").strip()
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        if choice == "1":
            fio = input("Введите ФИО для поиска: ").strip()
            cursor.execute(f"""
                SELECT * FROM {TABLE_NAME}
                WHERE fio LIKE ?
            """, (f"%{fio}%",))
        elif choice == "2":
            product = input("Введите название товара: ").strip()
            cursor.execute(f"""
                SELECT * FROM {TABLE_NAME}
                WHERE product LIKE ?
            """, (f"%{product}%",))
        elif choice == "3":
            min_cost = float(input("Минимальная стоимость: "))
            max_cost = float(input("Максимальная стоимость: "))
            cursor.execute(f"""
                SELECT * FROM {TABLE_NAME}
                WHERE cost BETWEEN ? AND ?
            """, (min_cost, max_cost))
        else:
            print("Неверный выбор.")
            conn.close()
            return

        rows = cursor.fetchall()
        if rows:
            print("\nРезультаты поиска:")
            for row in rows:
                print(f"ID:{row['id']} | {row['fio']} | {row['product']} | "
                      f"{row['quantity']} {row['unit']} | {row['cost']} руб.")
        else:
            print("Ничего не найдено.")
    except ValueError:
        print("Ошибка: введите корректные числа для стоимости.")
    except Exception as e:
        print(f"Ошибка при поиске: {e}")
    finally:
        conn.close()


def delete_record() -> None:
    print("\n--- Удаление записи ---")
    print("1. Удалить по ID")
    print("2. Удалить все записи с заданным товаром")
    print("3. Удалить записи с количеством меньше заданного")

    choice = input("Выберите вариант (1-3): ").strip()
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        if choice == "1":
            record_id = int(input("Введите ID записи для удаления: "))
            cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE id = ?", (record_id,))
        elif choice == "2":
            product = input("Введите название товара: ").strip()
            cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE product = ?", (product,))
        elif choice == "3":
            limit_qty = float(input("Удалить записи с количеством < ?: "))
            cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE quantity < ?", (limit_qty,))
        else:
            print("Неверный выбор.")
            conn.close()
            return

        conn.commit()
        print(f"Удалено записей: {cursor.rowcount}")
    except ValueError:
        print("Ошибка: введите корректное число.")
    except Exception as e:
        print(f"Ошибка при удалении: {e}")
    finally:
        conn.close()


def update_record() -> None:
    print("\n--- Редактирование записи ---")
    print("1. Изменить стоимость по ID")
    print("2. Изменить количество по названию товара")
    print("3. Изменить единицу измерения и цену по ФИО")

    choice = input("Выберите вариант (1-3): ").strip()
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        if choice == "1":
            record_id = int(input("ID записи: "))
            new_cost = float(input("Новая стоимость: "))
            cursor.execute(f"""
                UPDATE {TABLE_NAME}
                SET cost = ?
                WHERE id = ?
            """, (new_cost, record_id))
        elif choice == "2":
            product = input("Название товара: ")
            new_qty = float(input("Новое количество: "))
            cursor.execute(f"""
                UPDATE {TABLE_NAME}
                SET quantity = ?
                WHERE product = ?
            """, (new_qty, product))
        elif choice == "3":
            fio = input("ФИО покупателя: ")
            new_unit = input("Новая единица измерения: ")
            new_cost = float(input("Новая стоимость: "))
            cursor.execute(f"""
                UPDATE {TABLE_NAME}
                SET unit = ?, cost = ?
                WHERE fio = ?
            """, (new_unit, new_cost, fio))
        else:
            print("Неверный выбор.")
            conn.close()
            return

        conn.commit()
        print(f"Обновлено записей: {cursor.rowcount}")
    except ValueError:
        print("Ошибка: введите корректное число.")
    except Exception as e:
        print(f"Ошибка при редактировании: {e}")
    finally:
        conn.close()


def show_all() -> None:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {TABLE_NAME}")
    rows = cursor.fetchall()
    
    if rows:
        print("\n--- Все записи ---")
        for row in rows:
            print(f"ID:{row['id']} | {row['fio']} | {row['product']} | "
                  f"{row['quantity']} {row['unit']} | {row['cost']} руб.")
        print(f"\nВсего записей: {len(rows)}")
    else:
        print("Таблица пуста.")
    conn.close()


def main_menu() -> None:
    while True:
        print("\n" + "=" * 50)
        print("ИНТЕРНЕТ-МАГАЗИН - Управление продажами")
        print("1. Показать все записи")
        print("2. Добавить новую продажу")
        print("3. Поиск")
        print("4. Удалить запись(и)")
        print("5. Редактировать запись(и)")
        print("0. Выход")
        
        choice = input("Ваш выбор: ").strip()
        if len(choice) > 1:
            print("Введите только одну цифру (0-5)")
            continue

        if choice == "1":
            show_all()
        elif choice == "2":
            add_record()
        elif choice == "3":
            search_records()
        elif choice == "4":
            delete_record()
        elif choice == "5":
            update_record()
        elif choice == "0":
            print("До свидания!")
            sys.exit(0)
        else:
            print("Неверный ввод. Введите цифру от 0 до 5.")


def main() -> None:
    try:
        print("Запуск программы...")
        create_table()
        insert_sample_data()
        main_menu()
    except Exception as e:
        print(f"Критическая ошибка: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()