# # -*- coding: utf-8 -*-
#
# c_ Class1
#     ___ func x     # Абстрактный метод
#         # Возбуждаем исключение с помощью raise
#         r_ N..("Необходимо переопределить метод")
#
# c_ Class2 ?     # Наследуем абстрактный метод
#     ___ func x     # Переопределяем метод
#         print ?
#
# class Class3 ?      # Класс не переопределяет метод
#     p..
#
# c2 = Class2()
# c2.func(50)                # Выведет: 50
# c3 = Class3()
# try:                       # Перехватываем исключения
#     c3.func(50)            # Ошибка. Метод func() не переопределен
# except NotImplementedError as msg:
#     print(msg)             # Выведет: Необходимо переопределить метод