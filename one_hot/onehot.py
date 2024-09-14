# Задание 1. one hot
# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего
# из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это
# сделать без get_dummies?


import random
import pandas as pd
import seaborn as sb 
import matplotlib.pyplot as plt

# lst = ['robot'] * 10
# lst += ['human'] * 10

# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# print(data)

# unique =data['whoAmI'].unique()
# print(unique)
# one_hot = pd.DataFrame()

# for value in unique:
#     one_hot[value] = (data['whoAmI'] == value).astype(int)


# data = pd.concat([data, one_hot],axis='columns')
# print(data.head())

