# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку 
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# ам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов 
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять 
# из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в 
# программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке 
# и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  

stih = 'пара-ра-рам рам-пам-папам па-ра-па-да'

def Rhythm(stih):
    stih = stih.split()
    list_1 = []

    for word in stih:
        sum_glas = 0
        for i in word:
            if i in 'ауоыиэяюёе':
                sum_glas += 1
        list_1.append(sum_glas)
        print(list_1)
    return len(list_1) == list_1.count(list_1[0])

if Rhythm(stih):
    print('Парам пам-пам')
else:
    print('Пам парам')