# # -*- coding: utf-8 -*-
#
# # Context Manager Protocol
# c_ MyClass:
#     ___ -e ____
#         print("Вызван метод __enter__()")
#         r_ ____
#     ___ -e ____ Type Value Trace
#         print("Вызван метод __exit__()")
#         i_ T.. i_ N...  # Если исключение не возникло
#             print("Исключение не возникло")
#         e__             # Если возникло исключение
#             print("Value =", V..
#             r_ F...  # False — исключение не обработано
#                           # True  — исключение обработано
# print("Последовательность при отсутствии исключения:")
# w___ ?
#     print("Блок внутри with")
# print("\nПоследовательность при наличии исключения:")
# w___ ? a_ obj
#     print("Блок внутри with")
#     r__ T... Исключение TypeError