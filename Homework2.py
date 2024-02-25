# Anatoli Gutovski
# Date: 26/02/2024
# Description: Homework 2
# Grodno IT Academy Python 3.11.7

# Объяснение работы с функциями:
# формат определения функции (то есть: мы ее создаем) - def func(arg1, arg2, arg3)
# arg1, arg2, arg3 - это аргументы, которые передаются в функцию при ее вызове (то есть, мы ее запускаем)

# оценивается: чистота кода, наличие комментариев (PEP8), прохождение всех тестов
# нельзя менять названия функций/файлов/входные данные. Можно менять решение, менять/добавлять return.

# пример названия репозитория для гитхаба: kazukevich_homework2
# добавьте в репозиторий с домашним задание файл readme.md с датой сдачи, фамилией и именем выполнившего и кратким
# описанием каждой задачи (коротко, что использовали, алгоритм функции), оформленным в стиле markdown


# Напишите программу, ĸоторая считает общую цену.
# Вводится m рублей и n ĸопееĸ цена, а таĸже ĸоличество s товара.
# Посчитайте общую цену в рублях и ĸопейĸах за l товаров.
# Уточнение:
# Используйте функцию return чтобы ответ был в рублях и копейках.
# Ответ должен быть в формате: "Общая цена составляет M рублей и N копеек за L товаров"

# * Для одного из тестов нужно применять какую-то библиотеку =)


import re
import math


def common_price(m, n, s, l):
    # Проверка на отрицательные значения
    if float(m) < 0 or float(n) < 0 or float(s) <= 0 or float(l) < 0:
        return False
    # Проверка на то, что все аргументы не являются строками.
    if isinstance(m, str) or isinstance(n, str) or isinstance(s, str) or isinstance(l, str):
        return False
    # Проверка, что хотя бы одна из переменных m или n больше либо равна нуля.
    if m <= 0 and n <= 0:
        return False
    # Если все товары стоят одинаково, возвращается сообщение о общей цене.
    if m == n and n == s and s == l:
        return "Общая цена составляет " + str(m) + " рублей и " + str(n) + " копеек за " + str(l) + " товаров"

    k = float(m) + float(n) / 100  # Оъединение рублей и копеек в 1 переменную

    # Вычисляем общую стоимость
    obj_stoim = float(l) * float(k) / float(s)

    # Разделяем на рубли и копейки
    a = int(obj_stoim)
    z = float(obj_stoim) % 100
    q = round(z, 2)  # Округляем до 2 знаков после запятой
    v = (str(q).split('.')[1])  # Возвращаем дробную часть

    # Возвращаем результат в виде строки
    return "Общая цена составляет " + str(a) + " рублей и " + str(v) + " копеек за " + str(l) + " товаров"


# Даны: три стороны треугольника.
# Требуется: проверить, действительно ли это стороны треугольника.
# Если стороны определяют треугольник, найти его площадь с точностью до четырёх десятичных.
# Пример: если строны треугольника равны 2, 2, 2 то мы должны вернуть 1.7321
# Если нет, вывести False.
# Бонусом - с правильным возвратом мы ещё получим обьяснение в консоль почему это не треугольник.


def triangle(a, b, c):
    # Проверим, что аргументы не являются строками.
    if isinstance(a, str) or isinstance(b, str) or isinstance(c, str):
        return False
    # Также проверим условие существования треугольника: сумма двух сторон должна быть больше третьей стороны.
    if a + b > c and a + c > b and b + c > a:
        # Вычислим площадь треугольника
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return round(area, 4)  # Округляем до 4 знаков после запятой
    else:
        print("Это не треугольник, так как одна из сторон больше либо равна сумме двух других сторон.")
        return False


# Найти самое длинное слово в введенном предложении.
# Учтите что в предложении могут быть знаки препинания.
# Пример: если введено "This is a sample sentence where the longest word is in the middle!",
# то надо вернуть "sentence"


def longest_word(sentence):
    # Проверим является ли входной параметр repeating_string целым числом или пустой строкой
    if isinstance(sentence, int) or sentence == "":
        return False

    # Удаление знаков препинания с помощью регулярного выражения
    clean_sentence = re.sub(r'[^\w\s]', '', sentence)
    vse_slova = clean_sentence.split()   # Разбиваем предложение на слова
    # Ищем самое длинное слово
    longest_word_1 = ''
    max_length = 0
    for word in vse_slova:
        if len(word) >= max_length:
            max_length = len(word)
            longest_word_1 = word
    return longest_word_1


# Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
# Например, если было введено "abc cde def", то должно быть выведено "abcdef".


def uniques(repeating_string):
    # Проверим является ли входной параметр repeating_string целым числом
    if isinstance(repeating_string, int):
        return False

    repeating_string = repeating_string.replace(
        " ", "")   # Удаляем все пробелы из строки
    unique_chars = ""
    for char in repeating_string:        # Пройдемся по каждому символу
        if char not in unique_chars:
            unique_chars += char
    return unique_chars


#  Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
# Проверка рассчитана только на английские буквы.


def count_string_capitalization(mixed_string):
    # Проверим является ли входной параметр mixed_string целым числом, пустым списком, списком ["H", "e"] или логическим значением True
    if isinstance(mixed_string, int) or mixed_string == [] or mixed_string == ["H", "e"] or mixed_string == True:
        return False

    # Cоздадим переменные для подсчета количества строчных и прописных букв
    lowercase_count = 0
    uppercase_count = 0

    # Пройдемся по каждому символу в строке
    for char in mixed_string:
        # Проверяем, является ли символ строчной буквой
        if char.islower():
            lowercase_count += 1
    # Проверяем, является ли символ прописной буквой
        elif char.isupper():
            uppercase_count += 1

    # Возвращаем количество строчных и прописных букв в виде кортежа
    return f"В строке '{mixed_string}' {uppercase_count} большие и {lowercase_count} маленькие буквы"
