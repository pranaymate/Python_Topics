# # -*- coding: utf-8 -*-
#
# # Методы, которые являются общими для класса и всех экземпляров класса
# # и не имеют доступ к данным экземпляров классов, называются
# # статическими методами.
# #
# # Для создания статических методов используется декоратор
# # staticmethod.
# #
# # Декоратор – это специальная функция, которая изменяет поведение
# # функции или класса. Для применения декоратора следует перед
# # соответствующим объявлением указать символ @, имя необходимого
# # декоратора и список его аргументов в круглых скобках.
# # Если передача параметров декоратору не требуется, скобки не указываются.
#
#
# c_ MyClass
#     # Объявление атрибута класса
#     class_attribute _ 8
#
#     # Конструктор
#     ___ - ____
#         ____.data_attribute _ 42
#
#     # Статический метод. Обратите внимание, что у него нет параметра
#     # ____, поскольку он не связан ни с одним из экземпляров класса
#     # не имеет доступа к атрибутам-данным
#     0s..
#     ___ static_method
#         print ?.c...
#
#     # Обычный метод
#     ___ instance_method ____
#         print ____.d..
#
#
# __ ____ __ _________
#     # Вызов статического метода
#     ?.s..
#     # Инстанцирование объекта
#     obj = ?
#     # Вызов метода
#     ?.i..
#     # Аналогично атрибутам класса, доступ ко статическим методам
#     # можно получить и через экземпляр класса
#     ?.s..