'''
Задание 2. Разработать программу с применением пакета tk, взяв в качестве условия одну
любую задачу из ПЗ №№ 1 – 9.
'''
from tkinter import *

def calculate_seconds():
    try:
        n = int(entry.get())
        seconds_hour = 3600
        seconds_last_hour = n % seconds_hour
        result_label.config(text=f"Секунд за последний час: {seconds_last_hour}", fg="green")
    except ValueError:
        result_label.config(text="Ошибка! Введите целое число", fg="red")

def clear_fields():
    entry.delete(0, END)
    result_label.config(text="")

# Создание окна
window = Tk()
window.title("Подсчет секунд за последний час")
window.geometry("400x250")
window.resizable(False, False)

# Заголовок
title_label = Label(window, text="Подсчет секунд за последний час", 
                    font=("Arial", 12, "bold"))
title_label.pack(pady=15)

# Описание
desc_label = Label(window, text="Введите количество секунд, прошедших за день:", 
                   font=("Arial", 10))
desc_label.pack(pady=5)

# Поле ввода
entry = Entry(window, width=30, font=("Arial", 11), justify="center")
entry.pack(pady=10)

# Фрейм для кнопок
button_frame = Frame(window)
button_frame.pack(pady=10)

# Кнопка расчета
calc_button = Button(button_frame, text="Рассчитать", command=calculate_seconds,
                     bg="#4CAF50", fg="white", padx=20, pady=5)
calc_button.pack(side=LEFT, padx=5)

# Кнопка очистки
clear_button = Button(button_frame, text="Очистить", command=clear_fields,
                      bg="#f44336", fg="white", padx=20, pady=5)
clear_button.pack(side=LEFT, padx=5)

# Метка для вывода результата
result_label = Label(window, text="", font=("Arial", 11), wraplength=350)
result_label.pack(pady=20)

# Запуск приложения
window.mainloop()