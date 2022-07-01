seq = []
iteration = input('Введите количество элементов: ')
iterration = float(iteration)

counter = 0

while counter <= iterration - 1:
    counter = counter + 1
    element = input('Введите ' + str(counter) + ' элемент: ')
    seq.append(element)

seq.sort()
print('[' + ', '.join(seq)+ ']')