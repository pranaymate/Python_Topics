# -*- coding: utf-8 -*-

# У нас для вас хорошие новости: f-строки вступают в дело, чтобы помочь с форматированием. Также известные
# как «форматированные строковые литералы», f-strings являются строковыми литералами с «f» в начале и фигурные скобки,
# содержащие выражения, которые в дальнейшем будут заменены своими значениями. Выражения оцениваются по мере выполнения
# и затем форматируются при помощи протокола __format__ . Как всегда, документация Python может помочь,
# если хотите узнать больше.

name = "Eric"
age = 74

print(f'Hello, {name}. You are {age}.')
# Вывод: 'Hello, Eric. You are 74.'
#
# capital letter
print(F"Hello, {name}. You are {age}.")
# Вывод: 'Hello, Eric. You are 74.'

# Произвольные выражения
#
# Так как f-строки оцениваются по мере выражения, вы можете внести любую или все доступные выражения Python в них.
# Это позволит вам делать интересные вещи, например следующее:

print(f"{2 * 37}")
# Вывод: '74'


def to_lowercase(input):
    return input.lower()

name = "Eric Idle"

print(f"{to_lowercase(name)} is funny.")
# # Вывод: 'eric idle is funny.'

print(f"{name.lower()} is funny.")
# # Вывод: 'eric idle is funny.'

class Comedian:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f'{self.first_name} {self.last_name} is {self.age} .'

    def __repr__(self):
        return f"{self.first_name} {self.last_name} is {self.age} . Surprise!"

new_comedian = Comedian("Eric", "Idle", "74")

print(f"{new_comedian}")
# Вывод: 'Eric Idle is 74.'

# Методы __str__() и __repr__() работают с тем, как объекты отображаются в качестве строк, так что вам нужно убедиться
# в том, что вы используете один из этих методов в вашем определении класса. Если вы хотите выбрать один, попробуйте __
# repr__(), так как его можно использовать вместо __str__().

# Строка, которая возвращается __str__() является неформальным строковым представлением объекта и должна быть читаемой.
# Строка, которую вернул __str__() — это официальное выражение и должно быть однозначным. При вызове str() и repr(),
# предпочтительнее использовать __str__() и __repr__() напрямую.
#
# По умолчанию, f-строки будут использовать __str__(), но вы должны убедиться в том, что они используют __repr__(),
# если вы включаете флаг преобразования !r:

print(f"{new_comedian}")
# Вывод: 'Eric Idle is 74.'

print(f"{new_comedian!r}")
# Вывод: 'Eric Idle is 74. Surprise!'

# Многострочные F-Strings
#
# У вас могут быть многострочные f-strings:

name = "Eric"
profession = "comedian"
affiliation = "Monty Python"

message = (
    f"Hi {name}. "
    f"You are a {profession}. "
    f"You were in {age} ."
)

print(message)
# # Вывод: 'Hi Eric. You are a comedian. You were in Monty Python.'
#
# # Однако помните о том, что вам нужно разместить f вначале каждой строки. Следующий код не будет работать:
#
# message _
#     _"Hi n_. "
#     "You are a p___ . "
#     "You were in a___ ."
#
#
# print ?
# # Вывод: 'Hi Eric. You are a {profession}. You were in {affiliation}.'
#
# # Если вы не внесете f в начале каждой индивидуальной строки, то получите обычную, старую версию строк, без приятных новшеств.
# # Если вы хотите размножить строки по нескольким линиям, у вас также есть возможность избежать возвратов при помощи \:

message = f" Hi {name}. " \
          f"You are a {profession}. " \
          f"You were in {age} ."

print(message)
# # Вывод: 'Hi Eric. You are a comedian. You were in Monty Python.'
#
# message _ _ """
#     Hi n_.
#     You are a p__ .
#     You were in a___ .
# """
#
# print ?
# # Вывод: '\n    Hi Eric.\n    You are a comedian.\n    You were in Monty Python.\n'
#
# # Скорость
# #
# # Буква f в f-strings может также означать и “fast”. Наши f-строки заметно быстрее чем % и str.format() форматирования.
# # Как мы уже видели, f-строки являются выражениями, которые оцениваются по мере выполнения, а не постоянные значения.
# # Вот выдержка из документации:
# #     “F-Строки предоставляют способ встраивания выражений внутри строковых литералов с минимальным синтаксисом.
# #     Стоит обратить внимание на то, что f-строка является выражением, которое оценивается по мере выполнения,
# #     а не постоянным значением. В исходном коде Python f-строки является литеральной строкой с префиксом f,
# #     которая содержит выражения внутри скобок. Выражения заменяются их значением.”
# #
# # Во время выполнения, выражение внутри фигурных скобок оценивается в собственной области видимости Python и затем
# # сопоставляется со строковой литеральной частью f-строки. После этого возвращается итоговая строка. В целом, это все.
# #
# # Рассмотрим сравнение скорости:

#
import timeit
timeit.timeit("""name _ "Eric"
# ... age _ 74
# ... '%s is %s.' % (name, age)""", number _ 10000)
#
# # # 0.003324444866599663
# #
# # timeit.timeit("""name _ "Eric"
# # ... age _ 74
# # ... '{} is {}.'.format(name, age)""", number _ 10000)
# #
# # # 0.004242089427570761
# #
# # timeit.timeit("""name _ "Eric"
# # ... age _ 74
# # ... f'n_ is {age}.'""", number _ 10000)
# #
# # # 0.0024820892040722242
#
# # Однако, суть не всегда в этом. После того, как они реализуются первыми, у них есть определенные проблемы со скоростью
# # и их нужно сделать быстрее, чем str.format(). Для этого был предоставлен специальный опкод BUILD_STRING.
# # Python F-Строки: Детали
# #
# # На данный момент мы узнали почему f-строки так хороши, так что вам уже может быть интересно их попробовать в работе.
# # Рассмотрим несколько деталей, которые нужно учитывать:
# # Кавычки
# #
# # Вы можете использовать несколько типов кавычек внутри выражений. Убедитесь в том, что вы не используете один и тот же
# # тип кавычек внутри и снаружи f-строки.
# #
# # Этот код будет работать:
#
# print _ {'Eric Idle'}")
# # Вывод: 'Eric Idle'
#
# print(f'{"Eric Idle"}')
# # Вывод: 'Eric Idle'
#
# print(f"""Eric Idle""")
# # Вывод: 'Eric Idle'
#
# print(f'''Eric Idle''')
# # Вывод: 'Eric Idle'
#
# print _ The \"comedian\" is n_, aged a__.")
# # Вывод: 'The "comedian" is Eric Idle, aged 74.'
#
# # Словари
# #
# # Говоря о кавычках, будьте внимательны при работе со словарями Python. Вы можете вставить значение словаря
# # по его ключу, но сам ключ нужно вставлять в одиночные кавычки внутри f-строки. Сама же f-строка должна иметь двойные
# # кавычки.
#
# comedian _ 'name' 'Eric Idle' 'age' 74
#
# print _ The comedian is c.. |name , aged c... age ."
# # Вывод: The comedian is Eric Idle, aged 74.
#
# comedian _  'name' 'Eric Idle' 'age' 74
# # f'The comedian is {comedian['name']}, aged {comedian['age']}.'
# #   File "<stdin>", line 1
# #     f'The comedian is {comedian['name']}, aged {comedian['age']}.'
# #                                     ^
# # SyntaxError: invalid syntax
#
# # Если вы используете одиночные кавычки в ключах словаря и снаружи f-строк, тогда кавычка в начале ключа словаря будет
# # интерпретирован как конец строки.
#
# # Скобки
# #
# # Чтобы скобки появились в вашей строке, вам нужно использовать двойные скобки:
#
# print _ {{74}}")
# # Вывод: '{ 74 }'
#
# # Обратите внимание на то, что использование тройных скобок приведет к тому, что в строке будут только одинарные:
#
# print _ {{{74}}}" )
# # Вывод: '{ 74 }'
#
# # Однако, вы можете получить больше отображаемых скобок, если вы используете больше, чем три скобки:
#
# print _ {{{{74}}}}")
# # Вывод: '{{74}}'
#
# # Бэкслеши
# #
# # Как вы видели ранее, вы можете использовать бэкслеши в части строки f-string. Однако, вы не можете использовать
# # бэкслеши в части выражения f-string:
#
# # f"{\"Eric Idle\"}"
# #   File "<stdin>", line 1
# #     f"{\"Eric Idle\"}"
# #                       ^
# # SyntaxError: f-string expression part cannot include a backslash
#
# # Вы можете проработать это, оценивая выражение заранее и используя результат в f-строк:
#
# name _ "Eric Idle"
# print _ n_")
#
# # Вывод: 'Eric Idle'
#
#
