# # -*- coding: utf-8 -*-
#
# x = [1, 2, 3, 4, 5]                  # Создали список
# # Создаем копию списка
# y = l.. ?                          # или с помощью среза: y = x[:]
#                                      # или вызовом метода copy(): y = x.copy()
# print ?
# # [1, 2, 3, 4, 5]
# print(x i_ y)                        # Оператор показывает, что это разные объекты
# # False
# y[1] = 100                           # Изменяем второй элемент
# print(x, y)                          # Изменился только список в перемеой y
# # ([1, 2, 3, 4, 5], [1, 100, 3, 4, 5])
#
#
# x = [1, [2, 3, 4, 5]]                # Создали вложенный список
# y = l.. ?                          # Якобы сделали копию списка
# print(x i_ y)                        # Разные объекты
# # False
# y 1 1 = 100                        # Изменяем элемент
# print(x, y)                          # Изменение затронуло переменную x!!!
# # ([1, [2, 100, 4, 5]], [1, [2, 100, 4, 5]])