# -*- coding: utf-8 -*-

lambda x: x + 1
print((lambda x: x + 1)(2))

add_one = lambda x: x + 1
add_one(2)
# 3

# Вышеупомянутая лямбда-функция эквивалентна написанию этого:

def add_one(x):
    return x + 1


full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
print(full_name('guido', 'van rossum'))
# 'Full name: Guido Van Rossum'

# ругой шаблон, используемый в других языках, таких как JavaScript, – это немедленное выполнение лямбда-функции Python.
# Это называется выражением немедленного вызова функции (IIFE –  Immediately Invoked Function Expression,
# произносится «iffy»). Вот пример:

(lambda x, y: x + y)(2, 3)
# 5

# Лямбда-функции часто используются с функциями более высокого порядка, которые принимают одну или несколько функций
# в качестве аргументов или возвращают одну или несколько функций.
#
# Лямбда-функция может быть функцией более высокого порядка, принимая функцию (нормальную или лямбда-функцию)
# в качестве аргумента, как в следующем надуманном примере:

high_ord_func = lambda x, func: x + func(x)
high_ord_func(2, lambda x: x * x)
# 6
high_ord_func(2, lambda x: x + 3)
# 7

# Модуль dis предоставляет функции для анализа байт-кода Python, сгенерированного компилятором Python:

import dis
add = lambda x, y: x + y
type(add)

# class 'function'>

dis.dis(add)
# 1 0 LOAD_FAST  0(x)
# 2 LOAD_FAST    1(y)
# 4 BINARY_ADD
# 6 RETURN_VALUE

add
# < function <lambda > at 0x7f30c6ce9ea0 >

# Вы можете видеть, что dis() предоставляет читаемую версию байт-кода Python,
# позволяющую проверять низкоуровневые инструкции, которые интерпретатор Python будет использовать
# при выполнении программы.
#
# Теперь посмотрим на обычный объект функции:

import dis
def add(x, y): return x + y
type(add)
# <class 'function'>
dis.dis(add)
  # 1           0 LOAD_FAST                0 (x)
  #             2 LOAD_FAST                1 (y)
  #             4 BINARY_ADD
  #             6 RETURN_VALUE
add
# <function add at 0x7f30c6ce9f28>