# Первая задача: Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X. Программа должна вывести в консоль сколько раз встречается в 
# заданном списке искомое число X, которое мы вводим с клавиатуры, либо выводим на экран, 
# максимально близкое ему по значению

import random

lengthyList = int(input('Введите длину списка: '))
myList = [random.randint(1, 100) for _ in range (lengthyList)]

print(myList)

requiredNumber = int(input('Введите искомое число от 1 до 100: '))
count = myList.count(requiredNumber)
requiredNumberNew1 = requiredNumber - 1
requiredNumberNew2 = requiredNumber + 1
stop = 0

if count > 0:
    print(count)
else:
    for i in range(lengthyList):
        if requiredNumberNew1 == myList[i] or requiredNumberNew2 == myList[i]:
            stop = requiredNumber
            print (f'Искомое число не найдено, максимально близкое ему по значению: {myList[i]}')
    else:
        requiredNumberNew1 -= 1
        requiredNumberNew2 += 1     


