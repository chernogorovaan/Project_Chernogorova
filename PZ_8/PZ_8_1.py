"""
Удалите ключи ["name", "salary"] из sample_dict.
"""
try:
    my_dict = {
    "небо": "sky", "земля": "earth", "море": "sea", "река": "river",
    "гора": "mountain", "лес": "forest", "поле": "field", "цветок": "flower",
    "дерево": "tree", "трава": "grass"
    }

    translator = input("Введите слово: ")
    print(f"Перевод: {my_dict.get(translator, 'нет в словаре')}")
except AttributeError:
    print("ошибка! у объекта нет такого атрибута или метода")