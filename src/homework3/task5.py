""" Дан список. Выведите те его элементы, которые встречаются
   в списке только один раз. Элементы нужно выводить в том порядке,
   в котором они встречаются в списке.
"""

lst = '123456123'
for element in lst:
    lst.count(element)
    if lst.count(element) == 1:
        print(element)
