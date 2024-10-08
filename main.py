spis=input("Введите строку для определения кол-ва гласных:")# вывод строки для ввода данных
# инициализация данных
vse_sgl = "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"

index = []
sgl = 0

for i in range(len(spis)):
    char = spis[i].lower()
    if char in vse_sgl:
        index.append(i)
        sgl += 1

print('Количество согласных:',sgl)
print('Индексы согласных',index)