data = input('Введите любые цифры через запятую, точку с запятой или слэш: ')
data = data.replace('/', ',').replace(';', ',')
num = data.split(',')

uniques = []
for n in num:
    if num.count(n) == 1:
        uniques.append(n)

print(', '.join(uniques))
#4,6,8,6,4,7,2,7,1,5,9