# -*- coding: utf-8 -*-

# Можно получать значение элемента по его индексу (номеру).
# Индексация начинается с нуля.

# Создание списка чисел
my_list = [5, 7, 9, 1, 1, 2]

# Вывод первого и второго значений
print(my_list[0])
print(my_list[1])

# Ввод индекса
index = int(input('Введите номер элемента: '))
# Получение элемента
element = my_list[index]
# # Вывод значения на экран
print(element)