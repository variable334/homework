# Задание 1. Новые списки
# Даны три списка:

# 1. floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
# 2. names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
# 3. numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

# Напишите код, который создаёт три новых списка. Вот их содержимое:
# 1. Каждое число из списка floats возводится в третью степень и округляется
# до трёх знаков после запятой.
# 2. Из списка names берутся только имена минимум из пяти букв.
# 3. Из списка numbers берётся произведение всех чисел.


from functools import reduce


#      #1
lists = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
listname = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]


rounds =list(map(lambda x: round(x ** 3,3), lists))
print(rounds)


#       #2

def filters(listname):
    return len(listname) > 4

filt = filter(filters,listname)
print(list(filt))

#       #3

Listint = [22, 33, 10, 6894, 11, 2, 1]

funcComposition = reduce(lambda num1,num2:num1*num2,Listint)
print(funcComposition)