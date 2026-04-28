import time, sys
indent = 0                                  # количество пробелов для отступа
indentIncreasing = True                     # увеличивает или уменьшает оступ

try:
    while True:                             # главный цикл
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1)                     # пауза длительностью 1/10 секунды

        if indentIncreasing:
            # Увеличение количества проблов
            indent = indent + 1
            if indent == 20:
                # изменение направления
                indentIncreasing = False
        else:
            # уменьшение количества проблеов
            indent = indent - 1
            if indent == 0:
                # изменение направления
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
