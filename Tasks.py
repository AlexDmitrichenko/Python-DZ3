# Первая задача: Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X. Программа должна вывести в консоль сколько раз встречается в 
# заданном списке искомое число X, которое мы вводим с клавиатуры, либо выводим на экран, 
# максимально близкое ему по значению

# import random

# lengthyList = int(input('Введите длину списка: '))
# myList = [random.randint(1, 100) for _ in range (lengthyList)]

# print(myList)

# requiredNumber = int(input('Введите искомое число от 1 до 100: '))
# count = myList.count(requiredNumber)
# requiredNumberNew = myList[0]

# if count > 0:
#     print(count)
# else:
#     for item in myList:
#         if abs(item - requiredNumberNew) < abs(requiredNumberNew - requiredNumber):
#             requiredNumberNew = item

#     print (f'Искомое число не найдено, максимально близкое ему по значению: {requiredNumberNew}')        
    
#******************************************************************************************
# Вторая задача: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае 
# с английским алфавитом очки распределяются так: A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка;
# B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, 
# что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы. 
# ноутбук     12

# myDictEnglish = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP', 4:'FHVWY', 5:'K', 8:'JX', 10:'QZ'}
# myDictRussian = {1:'АВЕИНОРСТ', 2:'ДКЛМПУ', 3:'БГЁЬЯ', 4:'ЙЫ', 5:'ЖЗХЦЧ', 8:'ШЭЮ', 10:'ФЩЪ'}
# text = input('Введите слово: ').upper()

# myDictNew = {} 
# for k, v in myDictEnglish.items():
#     if text[0] == v:
#         myDictNew = myDictEnglish
#     else:
#         myDictNew = myDictRussian

# sum = 0
# for i in text:
#     for k, v in myDictNew.items():
#         if i in v:
#             sum += k

# print(sum) 



