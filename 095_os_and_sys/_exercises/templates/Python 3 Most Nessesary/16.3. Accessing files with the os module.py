# # # -*- coding: utf-8 -*-
#
# # Доступ к файлам с помощью модуля os
# #
# # ореn(<Путь к файлу>, <Режим>[, mode_Oo777])
# #
# # открывает файл и возвращает целочисле1mый
# # дескриmор, с помощью которого производится дальнейшая работа с файлом.
# # Если файл открыть не удалось, возбуждается исключение osError или одно из исключений,
# # являющихся подклассами класса OSError (мы поговорим о них в конце этой главы).
# # В параметре <Режим> в операционной системе Windows могут быть указаны следующие
# # флаги (или их комбинация через символ 1 ):
# # os. O_ ROONLY -чтение;
# # • os. O WRONLY -запись;
# # • os • O_ RDWR -чтение и запись;
# # • os. O_A.. -добавление в конец файла;
# # • os. O_C... -создать файл, если он не существует и если не указан флаг os. O_ EXCL;
# # • os.O_EXCL- при использовании совместно с os.O_CREATE указывает, что создаваемый
# # файл изначально не должен существовать, в противном случае будет сгенерировано
# # исключение FileExistsError;
# # • os. O_TЕМРОRАRУ - при использовании совместно с os. о_ CREAT указывает, что создается
# # временный файл, который будет автоматически удален сразу после закрытия;
# # • os.O_SHORT_LIVED-TO же самое, что os.O_TEMPORARY, но созданный файл по возмож-
# # ности будет храниться лишь в оперативной памяти, а не на диске;
# # • os. о_ TRUNC -очистить содержимое файла;
# # • os. о_ BINARY - файл будет открыт в бинарном режиме;
# # • os .о_ТЕХТ - файл будет открыт в текстовом режиме. В Windows файлы по умолчанию
# # открываются в текстовом режиме.
#
# ______ __
# __.na..               # Значение в ОС Windows 8
# # 'nt'
# ______ __                # Подключаем модуль
#
#
# mode _ __.O_W...  __.O_C...  __.O_T
# f _ __.o... _"file.txt", ?
# __.w... ? _"String1\n")  # Записываем данные
# # 8
# __.cl.. ?              # Закрываем файл
# # ######################################################################################################################
#
# mode _ __.O_W...  __.O_C...  __.O_A..
# f _ __.o... _"file.txt" ?
# __.w... ? _"String2\n") # Записываем данные
# # 8
# __.cl.. ?             # Закрываем файл
# # ######################################################################################################################
#
# f _ __.o... _"file.txt", __.O_R...
# __.r.. ? 50            # Читаем 50 байт
# # b'String1\nString2\n'
# __.cl.. ?               # Закрываем файл
# # ######################################################################################################################
#
# f _ __.o... _"file.txt" __.O_R...  __.O_B..
# __.r.. ? 50            # Читаем 50 байт
# # b'String1\r\nString2\r\n'
# __.cl.. ?               # Закрываем файл
# # ######################################################################################################################
#
# f _ __.o... _"file.txt" __.O_R...
# __.r.. ? 5 __.r.. ? 5 __.r.. ? 5 __.r.. ? 5
# # (b'Strin', b'g1\nS', b'tring', b'2\n')
# # ######################################################################################################################
# __.r... ? 5             # Достигнут конец файла
# # b''
# __.cl.. ?              # Закрываем файл
# # ######################################################################################################################
#
# f _ __.o... _"file.txt" __.O_R...  __.O_B..
# __.ls.. ? 0 __.S._E.  # Перемещение в конец файла
# # 18
# __.ls.. ? 0, __.S._S.  # Перемещение в начало файла
# # 0
# __.ls.. ? 9, __.S._C.  # Относительно указателя
# # 9
# __.ls.. ? 0, __.S._C.  # Текущее положение указателя
# # 9
# __.cl.. ?                 # Закрываем файл
# # ######################################################################################################################
#
# fd _ __.o... _"file.txt", __.O_R...
# ?
# # 3
# f _ __.f o. ? _
# ?.f.n.  # Объект имеет тот же дескриптор
# # 3
# ?.r..
# 'String1\nString2\n'
# ?.cl..
# # ######################################################################################################################