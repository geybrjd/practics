# Здесь приведен процесс выполненмя функции с вызовом других функций
def a():                        
    print('a() starts')         # 2 печатается строка
    b()                         # 3 вызывается функция b в которой выполянются инструкции
    d()                         # 5 вызываем функцию d
    print('a() returns')        # 6 печатаем текст

def b():
    print('b() starts')
    c()                         # 4 В функции b мы видим вызов фунции c
    print('b() returns')

def c():
    print('c() starts')
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')

a()                             # 1. вызывается функция a
