# Задача 4. Уникальный шифр
# Напишите функцию, которая принимает строку и возвращает количество
# уникальных символов в строке. Используйте для выполнения задачи
# lambda-функции и map и/или filter.
# Сделайте так, чтобы алгоритм НЕ был регистрозависим: буквы разного
# регистра должны считаться одинаковыми.
# Пример:
# message = "Today is a beautiful day! The sun is shining and the birds are
# singing."
# unique_count = count_unique_characters(message)
# print("Количество уникальных символов в строке:", unique_count)
# Вывод: количество уникальных символов в строке — 5.


message = "Today is a beautiful day! The sun is shining and the birds are singing.".lower()


# res = list(map(lambda x: mes.get(x,0) + 1,mes))

res = list(filter(lambda x:message.count(x) == 1, message))

print(res)
print(len(res))