# Задача 3. Палиндром
# Используя модуль collections, реализуйте функцию can_be_poly, которая
# принимает на вход строку и проверяет, можно ли получить из неё палиндром.
# Пример кода:
# print(can_be_poly('abcba'))
# print(can_be_poly('abbbc'))
# Результат:
# True
# False


from collections import Counter

# string ='abcba'
string ='abbbc'

def can_be_poly(string):
    
    return Counter(string)

a = can_be_poly(string)

res = list(filter(lambda x:x==1,a.values()))

if len(res)<2:
    print('может стать полиндромом')
else:
    print('не может стать полиндромом')

