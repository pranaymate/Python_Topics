# # # -*- coding: utf-8 -*-
# # copyf ile ( <Копируемый файл>, <Куда копируем>) - позволяет скопировать содержимое файла в другой файл.
# # Никакие метаданные (например, права доступа) не копируются. Если файл существует, то он будет перезаписан.
# # Если файл не удалось скопировать, возбуждается исключение OSError или одно из исключений, являющихся подклассом
# # этого класса.Исключение1 FileNotFoundError является подклассом класса OSError и возбуждается, если указанный
# # файл не найден.
# # сору ( <Копируемый файл>, <Куда копируем>) - позволяет скопировать файл вместе с правами доступа.
# # Если файл существует, то он будет перезаписан. Если файл не удалось скопировать, возбуждается исключение osError
# # или одно из исключений, являющихся подклассом этого класса.
# # Начиная с Python 3.3, функция сору () в качестве результата возвращает путь скопированного файла;
# # сору2 ( <Копируемый файл>, <Куда копируем>) - позволяет скопировать файл вместе с метаданными. Если файл существует,
# # то он будет перезаписан. Если файл не удалось скопировать, возбуждается исключение osError или одно из исключений,
# # являющихся подклассом этого класса.
# # Начиная с Python 3.3, функция сору2 () в качестве результата возвращает путь скопированного файла
# # rename ( <Старое имя>, <Новое имя>) - переименовывает файл. Если файл не удалось переименовать,
# # возбуждается исключение OSError или одно из исключений, являющихся подклассом этого класса.
# # Пример переименования файла с обработкой исключений:
# # remove (<Путь к файлу>) и unlink (<Путь к файлу>) - позволяют удалить файл. Если
# # файл не удалось удалить, возбуждается исключение OSError или одно из исключений,
# # являющихся подклассом этого класса.
# # e... <<Путь>) - проверяет указанный путь на существование. Значением функции
# # будет True, если путь существует, и False - в противном случае
# # Начиная с Python 3.3, в качестве параметра можно передать целочисленный дескриптор
# # открытого файла, возвращенный функцией open ( ) из того же модуля __;
# # g.s. (<Путь к файлу>) - возвращает размер файла в байтах. Если файл не существует,
# # возбуждается исключение OSError:
# # g.at. ( <Путь к файлу>) - служит для определения времени последнего доступа к файлу.
# # В качестве значения фунюmя возврашает количество секуН!l, прошедmи:х с начала эпохи.
# # Если файл не существует, возбуждается иск..rпочение OSE:rror.
# # getctime (<Путь к файлу>) - позволяет узнать дату создания файла. В качестве значения
# # функция возвращает количество секунд, прошедших с начала эпохи. Если файл HF сушествует,
# # возбуждается искточение OSError.
# # getmtirne (<Путь к файлу>) - возвращает время последнего изменения файла.
# # В качестве значения функция возвращает количество секунд, прошедших с начала эпохи. Если файл
# # не существует, возбуждается искточение OSError .
#
#
# _____ s_____      # Подключаем модуль
# s_____.c....  file.txt   file2.txt
# # Путь не существует:
# s_____.c....  file.txt   C:\book2\file2.txt
# # ... Фрагмент опущен ...
# # FileNotFoundError: [Errno 2] No such file or directory:
# # 'C:\\book2\\file2.txt'
#
# s_____.c.  file.txt   file3.txt
#
# s_____.copy2  file.txt   file4.txt
#
# s_____.move  file4.txt   C:\book\test
#
#
# _____ __  # Подключаем модуль
# t__
#     __.rename  file3.txt   file4.txt
# e__ OSE..
#     print  Файл не удалось переименовать
# e___
#     print  Файл успешно переименован
#
#
# __.re..  file2.txt
# __.un..  file4.txt
#
# _____ __.p___
# __.p___.e...  file.txt   __.p___.e...  file2.txt
# #  True False
# __.p___.e...  C:\book   __.p___.e...  C:\book2
# #  True False
# # ######################################################################################################################
#
# __.p___.g.s.  file.txt    # Файл существует
# # 18
# __.p___.g.s.  file2.txt   # Файл не существует
# # ... Фрагмент опущен ...
# # OSError: [Error 2] Не удается найти указанный файл: 'file2.txt'
# # ######################################################################################################################
#
# _____ ti..    # Подключаем модуль time
# t _ __.p___.g.at.  file.txt
# t
# # 1304111982.96875
# ti__.st..ti..  %d.%m.%Y %H:%M:%S  ti__.l..ti.. t
# # '30.04.2011 01:19:42'
# # ######################################################################################################################
#
# t _ __.p___.g..ct..  file.txt
# t
# # 1304028509.015625
# ti__.st..ti..  %d.%m.%Y %H:%M:%S  ti__.l.t. t
# # '29.04.2011 02:08:29'
# # ######################################################################################################################
#
# t _ __.p___.g..t..  file.txt
# t
# # 1304044731.265625
# t_.s_e  %d.%m.%Y %H:%M:%S  t__.l. t
# # '29.04.2011 06:38:51'
# # ######################################################################################################################