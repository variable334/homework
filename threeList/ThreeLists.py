# Задание 1. Три списка
# Даны три списка.

# array_1 = [1, 5, 10, 20, 40, 80, 100]
# array_2 = [6, 7, 20, 80, 100]
# array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

# Нужно выполнить две задачи:
# 1. найти элементы, которые есть в каждом списке;
# 2. найти элементы из первого списка, которых нет во втором и третьем
# списках.

# Каждую задачу нужно выполнить двумя способами:
# 1. без использования множеств;
# 2. с использованием множеств.

# Пример выполнения на других данных:
# array_1 = [1, 2, 3, 4]
# array_2 = [2, 4]
# array_3 = [2, 3]

# Вывод:
# Задача 1:
# Решение без множеств: 2
# Решение с множествами: 2

# Задача 2:
# Решение без множеств: 1
# Решение с множествами: 1



# без множеств


# array_1 = [1, 5, 10, 20, 40, 80, 100]

# array_2 = [6, 7, 20, 80, 100]

# array_3 = [3, 4, 15, 20, 30, 70, 80, 120]



# def NumberOfIntersections(array_1,array_2,array_3):
#     c,x,z = 0,0,0
#     c1,c2= 0,0
#     for i in array_1:
    
#         if i in array_2:
#             c+=1
#         if i not in array_2:
#             c1+=1
#         if i in array_3:
#             x +=1
#         if i not in array_3:
#             c2+=1    
#         for i in array_2:
#             if i in array_3:
#                 z +=1
#     return c,x,z,c1,c2


# c, x, z,c1,c2 = NumberOfIntersections(array_1, array_2, array_3)
# print(f"Пересечения между array_1 и array_2: {c}")
# print(f"Пересечения между array_1 и array_3: {x}")
# print(f"Пересечения между array_2 и array_3: {z}")

# print(f"количество элементов которых есть в array_1,но нету в array_2: {c1}")
# print(f"количество элементов которых есть в array_1,но нету в array_3: {c2}")


# # с множествами

# a =set()

# for i in array_1:
#     a.add(i)


# b =set()

# for i in array_2:
#     b.add(i)


# c =set()

# for i in array_3:
#     c.add(i)

# i = a.intersection(b)
# k = a.intersection(c)
# g = b.intersection(c)
# x = a.difference(b)
# c = a.difference(c)

# print(f"Пересечения между array_1 и array_2:{len(i)}")

# print(f"Пересечения между array_1 и array_3:{len(k)}")

# print(f"Пересечения между array_2 и array_3:{len(g)}")


# print(f"колличество элементов которые есть в множестве a,но нету в множестве b:{len(x)}")

# print(f"колличество элементов которые есть в множестве a,но нету в множестве с:{len(c)}")







# без множеств

# all_elems = array_1 + array_2 + array_3 
# new_elems_1 = []
# for elem in all_elems:


#     if elem not in new_elems_1 and all(elem in array for array in [array_1, array_2, array_3]):
#             new_elems_1.append(elem)
# print("Решение без множеств:", new_elems_1)



# с множествами

# new_elems_1_set = set(array_1) & set(array_2) & set(array_3) 

# print("Решение с множествами:", new_elems_1_set)

