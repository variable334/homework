# Задание 1. Поиск элемента
# Пользователь вводит искомый ключ. Если он хочет, то может ввести
# максимальную глубину — уровень, до которого будет просматриваться
# структура.
# Напишите функцию, которая находит заданный пользователем ключ в словаре
# и выдаёт значение этого ключа на экран. По умолчанию уровень не задан. В
# качестве примера можно использовать такой словарь:

# Пример 1

# Введите искомый ключ: head
# Хотите ввести максимальную глубину? Y/N: n
# Значение ключа: {'title': 'Мой сайт'}
# Пример 2

# Введите искомый ключ: head
# Хотите ввести максимальную глубину? Y/N: y
# Введите максимальную глубину: 1
# Значение ключа: None



site = {'html': {'head':{'title': 'Мой сайт'},'body': {'h2': 'Здесь будет мой заголовок','div': 'Тут, наверное, какой-то блок','p': 'А вот здесь новый абзац'}}}


def search_values(n_dict, key1, current_depth=0, max_depth=None):
 
    if max_depth is not None and current_depth >= max_depth:
        return print("None")

    for key, value in n_dict.items():
        if key == key1:
            print(f"Значение ключа '{key1}': {value}")

        if isinstance(value, dict):
            search_values(value, key1, current_depth + 1, max_depth)


m = input("Введите ключ: ")


user_input = input('Хотите ввести глубину? (y/n): ')

if user_input == 'y':
    max_depth = int(input('Введите глубину: '))
    search_values(site, m, max_depth=max_depth)
else:
    search_values(site, m)
