# Задание 1.
# Загрузите таблицу из файла advertising_1.csv и сохраните её в датафрейм
# adv1_df. Укажите в качестве индекса столбец Number. Выведите на экран
# первые десять строк.
# Подсказка № 1
# Используйте функцию pd.read_csv(), которая принимает имя файла и
# дополнительные параметры. Вам потребуется указать правильное имя файла в этой
# функции.
# Подсказка № 2
# После загрузки данных, вам нужно установить столбец 'Number' в качестве индекса
# DataFrame. Это можно сделать несколькими способами: при чтении файла, с помощью
# метода set_index(), или с использованием параметра index_col в функции
# pd.read_csv().
# Подсказка № 3
# После установки индекса, вы можете проверить, что столбец 'Number' действительно
# стал индексом. Вы можете вывести индексы DataFrame с помощью свойства index.
# Подсказка № 4
# Для просмотра первых десяти строк DataFrame используйте метод head(). По
# умолчанию он выводит 5 строк, но вы можете указать любое количество строк,
# передав параметр в метод.
# Подсказка № 5
# Если вы хотите работать с частями данных, например, выводить определенные строки,
# помните, что индекс теперь является столбцом 'Number'. Это поможет вам обращаться
# к строкам по индексу или использовать диапазоны индексов.


import pandas as pd

adv1_df = pd.read_csv('advertising_1.csv')

adv1_df = adv1_df.set_index('Number')

print(adv1_df.index)
print(adv1_df.head(10))



# Задание 2.
# Выведите размер датафрейма adv1_df и cреднее ежедневное время
# нахождения в интернете пользователя под номером 8.
# Подсказка № 1
# Чтобы узнать размер DataFrame, используйте атрибут shape. Он возвращает кортеж,
# содержащий количество строк и столбцов.
# Подсказка № 2
# Для получения значения в DataFrame по индексу (например, номеру пользователя) и
# столбцу (например, "Daily Internet Usage"), вам нужно знать, как индексированы строки
# и какие столбцы присутствуют.
# Подсказка № 3
# Для получения данных пользователя с номером 8, используйте метод .loc[], который
# позволяет обратиться к строке по её метке индекса.
# Подсказка № 4
# После того как вы получите строку для пользователя с номером 8, вам нужно выбрать
# конкретное значение столбца "Daily Internet Usage". Вы можете сделать это, указав
# название столбца в методе .loc[] или использовать метод .iloc[] для доступа по
# числовым индексам.


print(adv1_df.shape)


print(adv1_df.loc[8,'Daily Internet Usage'])



# Задание 3.
# Загрузите таблицу из файла advertising_2.csv и сохраните её в датафрейм
# adv2_df. Укажите в качестве индекса стоблец Number. Выведите на экран
# строки для пользователей с номерами с 533-го по 536-й.
# Подсказка № 1
# Для загрузки данных из CSV-файла используйте функцию pd.read_csv(). Проверьте,
# что указываете правильное имя файла и используете параметр index_col для
# установки столбца Number в качестве индекса.
# Подсказка № 2
# После загрузки данных проверьте, что столбец Number действительно стал индексом
# DataFrame и что данные корректно загружены. Это можно сделать, просмотрев первые
# несколько строк и проверив индексы.
# Подсказка № 3
# Чтобы получить строки с номерами с 533 по 536, используйте метод .loc[], который
# позволяет обращаться к строкам по меткам индекса. Помните, что .loc[] работает
# включительно, поэтому использование диапазона 533:536 включит строки с этими
# номерами.





adv2_df = pd.read_csv("advertising_2.csv")

adv2_df = adv2_df.set_index('Number')

print(adv2_df.loc[533:536])
