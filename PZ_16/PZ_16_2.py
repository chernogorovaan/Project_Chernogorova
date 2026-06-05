'''
Создайте класс "Автомобиль", который содержит информацию о марке, модели и
годе выпуска. Создайте класс "Грузовик", который наследуется от класса
"Автомобиль" и содержит информацию о грузоподъемности. Создайте класс
"Легковой автомобиль", который наследуется от класса "Автомобиль" и содержит
информацию о количестве пассажиров.
'''
class Auto:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def info(self):
        return f"Марка:{self.brand} \n Модель: {self.model} \n Год выпуска: {self.year}\n"

class Truck(Auto):
    def __init__(self, brand, model, year, load_capacity):
        super().__init__(brand, model, year)
        self.load_capacity = load_capacity
    def info(self):
        return f"Грузовик: \n Марка:{self.brand} \n Модель: {self.model} \n Год выпуска: {self.year}\n Грузоподъемность: {self.load_capacity}"

class Car(Auto):
    def __init__(self, brand, model, year, passengers):
        super().__init__(brand, model, year)
        self.passengers = passengers
    def info(self):
        return f"Легковой автмобиль: \n Марка:{self.brand} \n Модель: {self.model} \n Год выпуска: {self.year}\n Пассажиры: {self.passengers} человек"

car = Car('Toyota', 'Camry', 2020, 5)
truck = Truck("Volvo", "FH16", 2019, 25)
auto = Auto('Toyota', 'Camry', 2020)

print(car.info())
print(' ')
print(truck.info())
print(' ')
print(auto.info())