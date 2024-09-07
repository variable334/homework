# Задача 5*. «Война и мир»
# Мало кто не знает знаменитый роман Л. Н. Толстого «Война и мир». Это
# довольно объёмное произведение лежит в архиве voina-i-mir.zip. Напишите
# программу, которая подсчитывает статистику по буквам (не только русского
# алфавита) в этом романе и выводит результат на экран (или в файл). Результат
# должен быть отсортирован по частоте встречаемости букв (по возрастанию или
# убыванию). Регистр символов имеет значение.
# Архив можно распаковать вручную, но, если хотите, можете изучить
# документацию по модулю zipfile (можно использовать и другой модуль) и
# попробовать написать код, который будет распаковывать архив за вас.


import zipfile


with zipfile.ZipFile( r"C:\Users\vlvna\Downloads\voina-i-mir.zip","r") as zip_file:

    zp=zip_file.namelist()

    print(zp)
    
    for fn in zp:
        if fn.endswith('.txt'):
            print(f"Найден текстовый файл: {fn}")
            frequency = dict()
            with zip_file.open(fn) as file:
                content = file.read().decode('utf-8')    
            for string in content:
                if not string.isalpha():
                   continue
                if string in frequency:
                    frequency[string]+=1
                else:
                    frequency[string]=1
                      
           
    sorteds = dict(sorted(frequency.items(),key=lambda x: (-x[1],x[0])))       
   
   
with open("frequency.txt","w",encoding="utf-8") as file:
    for key,value in sorteds.items():
        file.write(f" {key} : {value} ")



