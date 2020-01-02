# -*- coding: utf-8 -*-

d = dict() ; print(d)                 # Создаем пустой словарь
# {}
d = dict(a=1, b=2) ; print(d)
# {'a': 1, 'b': 2}
d = dict({'a':1, 'b': 2}) ; print(d)     # Словарь
# {'a': 1, 'b': 2}
d = dict([('a', 1), ('b', 2)]) ; print(d) # Список кортежей
# {'a': 1, 'b': 2}
d = dict([['a', 1], ['b', 2]]); print(d) # Список списков
# {'a': 1, 'b': 2}


k = ["a", "b"]                           # Список с ключами
v = [1, 2]                               # Список со значениями
print(list(zip(k, v)))                   # Создание списка кортежей
# # [('a', 1), ('b', 2)]
d = dict(zip(k, v)); print(d)           # Создание словаря
# {'a': 1, 'b': 2}


d = {}; print(d)                         # Создание пустого словаря
# {}
d = { "a": 1, "b": 2 }; print(d)
# {'a': 1, 'b': 2}

d = {}                                   # Создаем пустой словарь
d["a"] = 1                               # Добавляем элемент1 (ключ "a")
d["b"] = 2                               # Добавляем элемент2 (ключ "b")
print(d)
# {'a': 1, 'b': 2}


d = dict.fromkeys(("a", "b", "c"))
print(d)
# {'a': None, 'c': None, 'b': None}
d = dict.fromkeys(["a", "b", "c"], 0)     # Указан список
print(d)
# {'a': 0, 'c': 0, 'b': 0}
d = dict.fromkeys(("a", "b", "c"), 0)     # Указан кортеж
print(d)
# # {'a': 0, 'c': 0, 'b': 0}
#
#
d1 = d2 = {'a': 1, 'b': 2}              # Якобы создали два объекта
d2["b"] = 10
print(d1, d2)                              # Изменилось значение в двух переменных !!!
# ({'a': 1, 'b': 10}, {'a': 1, 'b': 10})


d1, d2 = {"a": 1, "b": 2}, {"a": 1, "b": 2}
d2["b"] = 10
print(d1, d2)
# ({'a': 1, 'b': 2}, {'a': 1, 'b': 10})
