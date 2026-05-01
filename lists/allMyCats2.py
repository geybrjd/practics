catNames = []
while True:
    # Задался вопросом зачем здесь нужна str, если len без проблем считает список? Так ведь текст и int нелья склеить
    print('Укажите имя кота или кошки ' + str(len(catNames) +1) + ' (<ENTER> для  завершениея):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]
print('Имена котов и кошек:')
for name in catNames:
    print('   ' + name )
