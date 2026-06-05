'''
Добавьте методы для вычисления среднего балла и определения, является ли студент
отличником.
'''
class Student:
    def __init__(self, first_name, last_name, marks):
        self.first_name = first_name
        self.last_name = last_name
        self.marks = [int(i) for i in marks.split(',')]
    
    def good_pupil(self):
        if not self.marks:
            return "Нет"
        ball = sum(self.marks)/len(self.marks)
        if ball>=4.5:
            return "Да"
        else:
            return "Нет"

    def info(self):
        return f"Информация о студенте: \n Имя: {self.first_name}\n Фамилия: {self.last_name}\n Оценки: {self.marks}\n Является ли отличником: {self.good_pupil()}"

student = Student('Анастасия', 'Черногорова', '5,5,5,5,4')
print(student.info())