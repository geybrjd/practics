# При вводе люого значения кроме Vlad continue возвращает цикл в начало
# В случае если name != vlad, то цикл возвращается в начало continue иначе переходим в if
# если условие if истино то цикл прерывается break, иначе в начала цикла while

while True:
    print('Who are you?')
    name = input()
    if name != 'Vlad':
        continue
    print('Hello Vlad. What is the password? (It is a fish.)')
    password  = input()
    if password == 'swordfish':
        break
print('Access granted.')
