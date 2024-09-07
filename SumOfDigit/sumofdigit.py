# Задание 1. Сумма чисел
# Во входном файле numbers.txt записано N целых чисел, которые могут быть
# разделены пробелами и концами строк. Напишите программу, которая выводит
# сумму чисел во выходной файл answer.txt.




with open("number.txt", "r", encoding="utf-8") as file:

    total_sum = 0

    for line in file:

        numbers = [int(n) for n in line.split()]
        total_sum += sum(numbers)



# sum = open("answer.txt", "w", encoding="utf-8")

# sum.write(str(total_sum))
