# # -*- coding: utf-8 -*-

# __ a_decorator_passing_arguments function_to_decorate
#     ___ a_wrapper_accepting_arguments arg1 arg2 # аргументы прибывают отсюда
#         print Смотри, что я получил:*_ ar__ ar__
#         ? ar__ ar__
#
#     r__ ?
#
#
# # Теперь, когда мы вызываем функцию, которую возвращает декоратор,
# # мы вызываем её "обёртку", передаём ей аргументы и уже в свою очередь
# # она передаёт их декорируемой функции
#
# ??
# ___ print_full_name first_name last_name
#     print Меня зовут*_ f..... l.....
#
#
# ? Питер _ Венкман
# # выведет:
# # Смотри, что я получил: Питер Венкман
# # Меня зовут Питер Венкман
# # *