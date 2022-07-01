list_1 = input('Введите элементы 1-го списка через запятую: ')
list_2 = input('Введите элементы 2-го списка через запятую: ')
list_1 = list_1.split(',')
list_2 = list_2.split(',')
for i in list_1:
    if i in list_2:
        list_1.remove(i)
print(','.join(list_1))
