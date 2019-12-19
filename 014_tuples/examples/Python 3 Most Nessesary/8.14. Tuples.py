tuple()                # Создаем пустой кортеж
# ()
tuple("String")        # Преобразуем строку в кортеж
# ('S', 't', 'r', 'i', 'n', 'g')
print(tuple([1, 2, 3, 4, 5])) # Преобразуем список в кортеж
# (1, 2, 3, 4, 5)


t1 = ()        # Создаем пустой кортеж
t2 = (5,)      # Создаем кортеж из одного элемента
t3 = (1, "str", (3, 4)) # Кортеж из трех элементов
t4 = 1, "str", (3, 4)   # Кортеж из трех элементов
print(t1, t2, t3, t4)
# ((), (5,), (1, 'str', (3, 4)), (1, 'str', (3, 4)))

t = (5); print(type(t))      # Получили число, а не кортеж!
# <class 'int'>
t = ("str"); print(type(t))  # Получили строку, а не кортеж!
# <class 'str'>


t = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(t[0])                  # Получаем значение первого элемента кортежа
# 1
print(t[::-1])               # Изменяем порядок следования элементов
# (9, 8, 7, 6, 5, 4, 3, 2, 1)
print(t[2:5])                # Получаем срез
# (3, 4, 5)
print(8 in t, 0 in t)        # Проверка на вхождение
# (True, False)
print((1, 2, 3) * 3)         # Повторение
# (1, 2, 3, 1, 2, 3, 1, 2, 3)
print((1, 2, 3) + (4, 5, 6)) # Конкатенация
# (1, 2, 3, 4, 5, 6)


t = (1, 2, 3)         # Создаем кортеж
print(t[0])                  # Получаем элемент по индексу
# 1
# t[0] = 50             # Изменить элемент по индексу нельзя!
# Traceback (most recent call last):
#   File "<pyshell#95>", line 1, in <module>
#     t[0] = 50             # Изменить элемент по индексу нельзя!
# TypeError: 'tuple' object does not support item assignment


t = (1, 2, 3)          # Создаем кортеж
print(len(t))                 # Получаем количество элементов
# 3
t = (1, 2, 1, 2, 1)
print(t.index(1), t.index(2)) # Ищем элементы в кортеже
# (0, 1)