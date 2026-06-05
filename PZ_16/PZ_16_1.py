'''
Создайте класс «Студент», который имеет атрибуты имя, фамилия и оценки.
Добавьте методы для вычисления среднего балла и определения, является ли студент
отличником.
'''
class Student:
    def __init__(self, first_name, last_name, marks):
        self.first_name = first_name
        self.last_name = last_name
        self.marks = marks

    def info(self):
        return f"Информация о студенте: \n Имя: {self.first_name}\n Фамилия: {self.last_name}\n Оценки: {self.marks}\n"

student = Student('Анастасия', 'Черногорова', '5,5,5,5,4')
print(student.info())