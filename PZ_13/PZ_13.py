'''
Из исходного текстового файла (Dostoevsky.txt) выбрать блок информации за 1857
год и поместить ее в новый текстовый файл.
'''
import re
with open('Dostoevsky.txt', 'r' , encoding='utf-8') as file:
    text = file.read()

pattern = r'(?:^|\n)(.*?1857.*?)(?=\n\d{4}|\Z)'


pattern2 = r'(?:^|\n)([^\n]*1857[^\n]*(?:\n[^\n\d]+)*)'

match = re.search(pattern2, text, re.DOTALL | re.MULTILINE)

if match:
    with open('Dostoevsky_1857.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(match.group(1))
    print("Блок за 1857 год успешно сохранен в файл 'Dostoevsky_1857.txt'")
else:
    print("Информация за 1857 год не найдена")