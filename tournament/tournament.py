# Задача 3. Турнир
# В файле first_tour.txt записано число K и данные об участниках турнира по
# настольной игре «Орлеан»: фамилии, имена и количество баллов, набранных в
# первом туре. Во второй тур проходят участники, которые набрали более K
# баллов в первом туре.
# Напишите программу, которая выводит в файл second_tour.txt данные всех
# участников, прошедших во второй тур, с нумерацией.
# В первой строке нужно вывести в файл second_tour.txt количество участников
# второго тура. Затем программа должна вывести фамилии, инициалы и
# количество баллов всех участников, прошедших во второй тур, с нумерацией.
# Имя нужно сократить до одной буквы. Список должен быть отсортирован по
# убыванию набранных баллов.




with open("first_tour.txt", "r") as file:
    lines = file.readlines()

    k = int(lines[0])

    names = dict()
    victory = dict()
    с = 1


for ln in lines[1:]:

    d = ln.split()
    
    n= f"{d[0]}.{d[1][0]}"

    names[n]=d[-1]
    


for key,val in names.items():
    if int(val) > k:
        victory[key]= val


finisch = dict(sorted(victory.items(), key=lambda x: x[0]))


# with open("second_tour.txt","w",encoding="utf-8") as file:
#     file.write(f"{len(finisch)}\n")

#     for i,(key,value) in enumerate(finisch.items(),start=1):
#         file.write(f"{i}) {key} {value} \n")
