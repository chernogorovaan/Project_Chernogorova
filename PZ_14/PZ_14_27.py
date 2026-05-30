'''
Задание 1. В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
приближенный к оригиналу (см. таблицу 1)
'''
import tkinter as tk

root = tk.Tk()
root.title("Выбор адреса")
root.geometry("550x500")
root.configure(bg="#e8e8e8")
root.resizable(False, False)

# ---------------- Заголовок ----------------

title = tk.Label(
    root,
    text="выбрать из справочника",
    fg="#3aa0dd",
    bg="#e8e8e8",
    font=("Arial", 14, "underline")
)
title.pack(pady=10)

# ---------------- Регион ----------------

tk.Label(
    root,
    text="Регион",
    bg="#e8e8e8",
    font=("Arial", 14)
).place(x=30, y=50)

regions = [
    "Не выбрано",
    "Московская область",
    "Ленинградская область",
    "Краснодарский край"
]

region_var = tk.StringVar()
region_var.set(regions[0])

region_menu = tk.OptionMenu(root, region_var, *regions)
region_menu.config(width=35, font=("Arial", 12))
region_menu.place(x=30, y=80)

# ---------------- Район ----------------

tk.Label(
    root,
    text="Район",
    bg="#e8e8e8",
    font=("Arial", 14)
).place(x=30, y=130)

districts = [
    "Выберите район",
    "Центральный",
    "Ленинский",
    "Советский"
]

district_var = tk.StringVar()
district_var.set(districts[0])

district_menu = tk.OptionMenu(root, district_var, *districts)
district_menu.config(width=35, font=("Arial", 12))
district_menu.place(x=30, y=160)

# ---------------- Город ----------------

tk.Label(
    root,
    text="Город",
    bg="#e8e8e8",
    font=("Arial", 14)
).place(x=30, y=210)

cities = [
    "Выберите город",
    "Москва",
    "Санкт-Петербург",
    "Краснодар",
    "Казань"
]

city_var = tk.StringVar()
city_var.set(cities[0])

city_menu = tk.OptionMenu(root, city_var, *cities)
city_menu.config(width=35, font=("Arial", 12))
city_menu.place(x=30, y=240)

# ---------------- Улица ----------------

tk.Label(
    root,
    text="Улица",
    bg="#e8e8e8",
    font=("Arial", 14)
).place(x=30, y=290)

streets = [
    "Выберите улицу",
    "Ленина",
    "Пушкина",
    "Гагарина",
    "Советская"
]

street_var = tk.StringVar()
street_var.set(streets[0])

street_menu = tk.OptionMenu(root, street_var, *streets)
street_menu.config(width=35, font=("Arial", 12))
street_menu.place(x=30, y=320)

# ---------------- Поля ввода ----------------

tk.Label(root, text="Дом", bg="#e8e8e8", font=("Arial", 12)).place(x=30, y=380)
house = tk.Entry(root, width=10, font=("Arial", 12))
house.place(x=80, y=380)

tk.Label(root, text="Корпус", bg="#e8e8e8", font=("Arial", 12)).place(x=180, y=380)
building = tk.Entry(root, width=10, font=("Arial", 12))
building.place(x=250, y=380)

tk.Label(root, text="Кв./Офис", bg="#e8e8e8", font=("Arial", 12)).place(x=350, y=380)
flat = tk.Entry(root, width=10, font=("Arial", 12))
flat.place(x=430, y=380)

# ---------------- Кнопки ----------------

def show_data():
    print("Регион:", region_var.get())
    print("Район:", district_var.get())
    print("Город:", city_var.get())
    print("Улица:", street_var.get())
    print("Дом:", house.get())
    print("Корпус:", building.get())
    print("Квартира:", flat.get())
    print("-" * 30)

btn_ok = tk.Button(
    root,
    text="OK",
    command=show_data,
    width=10,
    bg="white",
    fg="#3aa0dd",
    font=("Arial", 16, "bold")
)
btn_ok.place(x=100, y=440)

btn_cancel = tk.Button(
    root,
    text="ОТМЕНА",
    command=root.destroy,
    width=12,
    bg="white",
    fg="#3aa0dd",
    font=("Arial", 16, "bold")
)
btn_cancel.place(x=280, y=440)

root.mainloop()