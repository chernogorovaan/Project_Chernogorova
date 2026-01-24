"""
Удалите ключи ["name", "salary"] из sample_dict.
"""
try:
  sample_dict = { 
  "name": "Kelly", 
  "age": 25, 
  "salary": 8000, 
  "city": "New york" 
  }
  del sample_dict["name"]
  del sample_dict["salary"]
  print(sample_dict)
except AttributeError:

  print("ошибка! у объекта нет такого атрибута или метода")
