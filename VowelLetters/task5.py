
# Задание 1. Гласные буквы
# Команде лингвистов понравилось качество ваших программ, поэтому они
# решили заказать функцию для анализатора текста, которая создавала бы
# список гласных букв в нём и считала бы их количество.
# Напишите программу, которая запрашивает у пользователя текст и генерирует
# список гласных букв этого материала (сама строка вводится на русском языке).
# Выведите в консоль сам список и его длину.
# Пример:
# Введите текст: Нужно отнести кольцо в Мордор!
# Список гласных букв: ['у', 'о', 'о', 'е', 'и', 'о', 'о', 'о', 'о']
# Длина списка: 9




string = input('Введите текст: ')


consonants = 'ауоыиэяюёе'


res_list=[i for i in string if i in consonants]
print(res_list)
print(len(res_list))



def analyzator(string):
    consonants = 'ауоыиэяюёе'
    res_list = []
    for i in string:
        if i in consonants:
            res_list.append(i)
    return res_list

a = analyzator(string)
print(a)
