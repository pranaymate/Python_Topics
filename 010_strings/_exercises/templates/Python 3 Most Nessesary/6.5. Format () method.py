# # -*- coding: utf-8 -*-
#
# print("Символы {{ и }} — @".f...("специальные"))
# # Символы { и } — специальные
#
#
# print("@ — @ — @".f... 10 12.3 "string"      # Индексы
# # '10 — 12.3 — string'
# arr = [10, 12.3, "string"]
# print("@ — @ — @".f... $?                    # Индексы
# # '10 — 12.3 — string'
# print(" model — color ".f... c.._ red , m.._ BMW # Ключи
# # 'BMW — red'
# d = "color" "red" "model" "BMW"
# print(" m.. — c..".f... $$?                  # Ключи
# # 'BMW — red'
# print(" c.. — @".f... 2015 c.._ red         # Комбинация
# # 'red — 2015'
#
#
# arr = [10, [12.3, "string"]]
# print(" 0 0 — 0 1 0 — 0 1 1".f... ?    # Индексы
# # '10 — 12.3 — string'
# print("? 0 — ? 1 1".f...(a.._a..       # Индексы
# '10 — string'
#
#
# c_ Car:
#     color, model _ "red", "BMW"
#
#
# car = C..
# print(" 0.m.. — 0.c..".f... ?             # Атрибуты
# # 'BMW — red'
#
#
# print("@ — @ — @ — n".f... 1, 2, 3, n_4  # "{0} — {1} — {2} — {n}"
# # '1 — 2 — 3 — 4'
# print("@ — @ — n — @".f... 1, 2, 3, n_4  # "{0} — {1} — {n} — {2}"
# # '1 — 2 — 4 — 3'
#
#
# print("_$$_".f...("строка"                  # str()
# # строка
# print(" $$_".f...("строка"))                   # repr()
# # 'строка'
# print(" $$_".f...("строка"                   # ascii()
# # '\u0441\u0442\u0440\u043e\u043a\u0430'
#
# print("' 0:10 ' ' 1 3'".f... 3, "string"
# # "'         3' 'string'"
#
# print("' 0 1 '".f...(3, 10 # 10 — это ширина поля
# # "'         3'"
#
# print("' 0 <10' ' 1 >10' ' 2 ^10'".f... 3, 3, 3
# # "'3         ' '         3' '    3     '"
#
#
# print("' 0 _10' ' 1 _10'".f... -3 3
# # "'-        3' '         3'"
#
#
# print("' 0 _010' ' 1 _010'".f... -3, 3
# # "'-000000003' '0000000003'"
#
#
# print("' 0 0_10 ' ' 1 0_10 '".f... -3 3
# # "'-000000003' '0000000003'"
# print("' 0 *<10' '1 +>10 ' ' 2 .^10 '".f... 3, 3, 3
# # "'3*********' '+++++++++3' '....3.....'"
#
#
# print("' 0 + ' ' 1 + ' ' 0 - ' ' 1 - '".f... 3, -3
# # "'+3' '-3' '3' '-3'"
# print("' 0 ' ' 1  '".f... 3, -3       # Пробел
# # "' 3' '-3'"
#
# print("' 0 b ' ' 0 #b'".f... 3
# # "'11' '0b11'"
#
# print("' 0 c'".f... 100
# # "'d'"
#
# _______ lo___
# print(lo___.setlocale lo___.LC_NUMERIC, 'Russian_Russia.1251'
# # 'Russian_Russia.1251'
# print(" 0 n ".f...(100000000).re.. "\uffa0", " "
# # 100 000 000
#
# _______ lo___
# print(lo___.setlocale(lo___.LC_NUMERIC, "Russian_Russia.1251"))
# # 'Russian_Russia.1251'
# print(print(lo___.f...("%d", 100000000, grouping _ T...
# # 100 000 000
# print(lo___.localeconv()["thousands_sep"])
# # '\xa0'
#
# print(" 0 ,d ".f... 100000000
# # 100,000,000
#
# print("' 0 d ' ' 0 o ' ' 0 #o '".f... 511
# # "'511' '777' '0o777'"
#
# print("' 0 x ' ' 0 #x '".f... 255
# # "'ff' '0xff'"
#
# print("' 0 X ' ' 0 #X '".f... 255
# # "'FF' '0XFF'"
#
# print("' 0 f ' ' 1 f ' ' 2 f '".f... 30, 18.6578145, -2.5
# # "'30.000000' '18.657815' '-2.500000'"
#
# print("' 0 .7f ' ' 1 .2f '".f... 18.6578145, -2.5
# # "'18.6578145' '-2.50'"
#
# print("' 0 e ' ' 1 e '".f... 3000, 18657.81452
# # "'3.000000e+03' '1.865781e+04'"
#
# print("' 0 E ' ' 1 E '".f... 3000, 18657.81452
# # "'3.000000E+03' '1.865781E+04'"
#
# print("' 0 .2e ' ' 1 .2E '".f... 3000, 18657.81452
# # "'3.00e+03' '1.87E+04'"
#
# print("' 0 g ' ' 1 g '".f... 0.086578, 0.000086578
# # "'0.086578' '8.6578e-05'"
#
# print("' 0 G ' ' 1 G '".f... 0.086578, 0.000086578
# # "'0.086578' '8.6578E-05'"
#
# print("' 0 % ' ' 1 .4% '".f... 0.086578, 0.000086578
# # "'8.657800%' '0.0087%'"