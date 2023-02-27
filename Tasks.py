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

if count > 0:
    print(count)
else:
    requiredNumberNew1 = requiredNumber - 1
    requiredNumberNew2 = requiredNumber + 1
    for item in myList:
        if requiredNumberNew1 == item or requiredNumberNew2 == item:
            print (item)
    else:
        requiredNumberNew1 -= 1
        requiredNumberNew2 += 1

