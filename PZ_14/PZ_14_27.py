'''
Задание 1. В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
приближенный к оригиналу (см. таблицу 1)
'''
from tkinter import *

window = Tk()
window.title('Окно №1')
window.geometry("400x350")
window.resizable(False, False)

# Основной фрейм
main_frame = Frame(window)
main_frame.pack(pady=20, padx=20)

# Заголовок
title = Label(main_frame, text="выбрать из справочника", font=("Arial", 10))
title.grid(row=0, column=0, columnspan=4, sticky="w", pady=(0, 15))

# Регион
Label(main_frame, text="Регион", width=10, anchor="w").grid(row=1, column=0, sticky="w")
region_entry = Entry(main_frame, width=25)
region_entry.grid(row=1, column=1, columnspan=3, sticky="w", padx=(0, 0))
region_entry.insert(0, "[ не выбрано ]")

# Район
Label(main_frame, text="Район", width=10, anchor="w").grid(row=2, column=0, sticky="w", pady=(10, 0))
district_entry = Entry(main_frame, width=25)
district_entry.grid(row=2, column=1, columnspan=3, sticky="w", padx=(0, 0), pady=(10, 0))
district_entry.insert(0, "Выберите район")

# Город
Label(main_frame, text="Город", width=10, anchor="w").grid(row=3, column=0, sticky="w", pady=(10, 0))
city_entry = Entry(main_frame, width=25)
city_entry.grid(row=3, column=1, columnspan=3, sticky="w", padx=(0, 0), pady=(10, 0))
city_entry.insert(0, "Выберите город")

# Улица
Label(main_frame, text="Улица", width=10, anchor="w").grid(row=4, column=0, sticky="w", pady=(10, 0))
street_entry = Entry(main_frame, width=25)
street_entry.grid(row=4, column=1, columnspan=3, sticky="w", padx=(0, 0), pady=(10, 0))
street_entry.insert(0, "Выберите улицу")

# Дом и Корпус
Label(main_frame, text="Дом", width=10, anchor="w").grid(row=5, column=0, sticky="w", pady=(10, 0))
house_entry = Entry(main_frame, width=10)
house_entry.grid(row=5, column=1, sticky="w", padx=(0, 0), pady=(10, 0))

Label(main_frame, text="Корпус", width=6, anchor="w").grid(row=5, column=2, sticky="w", pady=(10, 0))
building_entry = Entry(main_frame, width=8)
building_entry.grid(row=5, column=3, sticky="w", padx=(0, 0), pady=(10, 0))

# Стр./Вл. и Кв./Офис
Label(main_frame, text="Стр./Вл.", width=10, anchor="w").grid(row=6, column=0, sticky="w", pady=(10, 0))
structure_entry = Entry(main_frame, width=10)
structure_entry.grid(row=6, column=1, sticky="w", padx=(0, 0), pady=(10, 0))

Label(main_frame, text="Кв./Офис", width=8, anchor="w").grid(row=6, column=2, sticky="w", pady=(10, 0))
apartment_entry = Entry(main_frame, width=8)
apartment_entry.grid(row=6, column=3, sticky="w", padx=(0, 0), pady=(10, 0))

# Кнопки
button_frame = Frame(main_frame)
button_frame.grid(row=7, column=0, columnspan=4, pady=25)

ok_button = Button(button_frame, text="OK", width=8)
ok_button.pack(side=LEFT, padx=5)

cancel_button = Button(button_frame, text="ОТМЕНА", width=8)
cancel_button.pack(side=LEFT, padx=5)

window.mainloop()