""" Дан список чисел. Посчитайте, сколько в нем пар элементов,
   равных друг другу. Считается, что любые два элемента, равные друг другу
   образуют одну пару, которую необходимо посчитать.
   Входные данные - строка из чисел, разделенная пробелами.
   Выходные данные - количество пар.
   Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар.
"""


def func_1(string_num='1 1 2 2 3 3 3 4 4 4 4'):
    lst = string_num.split()
    pairs = 0

    numbers = {element: string_num.count(element) for element in lst}
    for key in numbers:
        num = 0
        while num < numbers[key] - 1:
            num += 1
            pairs += num
    print(pairs)


"""Дан список целых чисел. Требуется переместить все ненулевые элементы
   в левую часть списка, не меняя их порядок, а все нули - в правую часть.
   Порядок ненулевых элементов изменять нельзя, дополнительный списоки
   спользовать нельзя, задачу нужно выполнить за один проход по списку.
   Распечатайте полученный список.
"""


def func_2():
    lst_num = [-3, 0, 3, -2, 0, 2, -1, 0, 1]

    for number in lst_num:
        if number == 0:
            lst_num.remove(number)
            lst_num.append(0)
    print(lst_num)


"""Вводится строка. Требуется удалить из нее повторяющиеся символы и все
   пробелы. Например, если было введено "abc cde def", то должно быть
   выведено "abcdef".
"""


def func_3(string='abc cde def'):
    new_string = ''
    for i in string:
        if i not in new_string and i != ' ':
            new_string += i
    print(new_string)