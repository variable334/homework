# Задача 4. Частотный анализ
# Есть файл text.txt, который содержит текст. Напишите программу, которая
# выполняет частотный анализ, определяя долю каждой буквы английского
# алфавита в общем количестве английских букв в тексте, и выводит результат в
# файл analysis.txt. Символы, не являющиеся буквами английского алфавита,
# учитывать не нужно.
# В файл analysis.txt выводится доля каждой буквы, встречающейся в тексте, с
# тремя знаками в дробной части. Буквы должны быть отсортированы по
# убыванию их доли. Буквы с равной долей должны следовать в алфавитном
# порядке.
# Пример:
# Содержимое файла text.txt:
# Mama myla ramu.
# Содержимое файла analysis.txt:
# a 0.333
# m 0.333
# l 0.083
# r 0.083
# u 0.083
# y 0.083


with open("text.txt","r",encoding="utf-8") as file:

    files = file.read().lower()
    files = files.replace(' ','')
    files = files.replace('.','')
    print(files)


    count = len(files)
    print(count)
    my_dict = dict()


for i in files:
    if i in my_dict:
        my_dict[i]+=1

    else:
        my_dict[i]=1




fin_dict = dict()

for k,v in my_dict.items():
    fin_dict[k]=round(v/count,3)


fin_dict=(fin_dict)




sorted_dict = dict(sorted(fin_dict.items(), key=lambda x: (-x[1], x[0])))




with open('analysis.txt','w',encoding='utf-8') as file:


    for key,value in fin_dict.items():

        file.write(f" {key} {value} \n")

