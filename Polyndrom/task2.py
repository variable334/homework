# Задача 2. Палиндром

# Пользователь вводит строку. Необходимо написать программу, которая
# определяет, существует ли у этой строки перестановка, при которой она станет
# палиндромом. Затем она должна выводить соответствующее сообщение.

# Пример 1
# Введите строку: aab
# Можно сделать палиндромом

# Пример 2
# Введите строку: aabc
# Нельзя сделать палиндромом



text = input('Введите слово: ')


char_count = {}

for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print(char_count)

c = 0

for value in char_count.values():
    if value % 2 == 1:
        print(value)
        c +=1

print(c)
        
if c >= 2:
    print('нельзя сделать полиндромом')
else:
    print('можно сделать полиндромом')    

