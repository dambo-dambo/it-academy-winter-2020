""" #1 Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
"""

list1 = ['a', 'b', 'c']
tpl1 = tuple(list1)
print(tpl1)


""" #2 Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
"""

tpl2 = ('a', 'b', 'c')
list2 = list(tpl2)
print(list2)


""" #3 Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’
"""
a, b, c = 'a', 'b', 'python'
print(a, b, c)


""" #4 Создайте кортеж из одного элемента, чтобы при итерировании
   по этому элементы последовательно выводились значения 1, 2, 3.
   Убедитесь что len() исходного кортежа возвращает 1.
"""

tpl4 = ('1, 2, 3',)
for element in tpl4:
    print(element)

print(len(tpl4))