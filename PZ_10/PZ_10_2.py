'''
Из предложенного текстового файла (text18-27.txt) вывести на экран его содержимое,
количество пробельных символов. Сформировать новый файл, в который поместить текст
в стихотворной форме предварительно поставив последнюю строку фразой введенной
пользователем.
'''
file = open('text18-27.txt', 'r')  
text = file.read()                                    
file.close() 
print(text)

spaces = 0
for i in text:
    if i == ' ' or i == '\n' or i == '\t':
        spaces+=1
print("Пробельных символов:", spaces)

sayit = input("Введи фразу: ")
strs = text.split('\n')
strs[-1] = sayit
new_text = '\n'.join(strs)

f = open('new_file.txt', 'w')
f.write(new_text)
f.close()


