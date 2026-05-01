myPets = ['Буся', 'Хрюня', 'Барсик']
print('Укажите имя домашнего питомца: ')
name = input()
if name not in myPets:
    print('У меня нет питомца по имени', name)
else:
    print(name, ' - Мой питомец')
