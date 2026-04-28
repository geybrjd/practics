import random, sys

print('Камень, Ножницы, Бумага')

wins = 0
losses = 0
ties = 0

while True:
    print('%s побед, %s поражений %s ничьих' % (wins, losses, ties))
    while True:
        print('Выберите ход: (к)аменьб (н)ожницы, ' '(б)умага или ' + ' (в)ыход')
        playerMove = input()
        if playerMove == 'в':
            sys.exit()
        if playerMove == 'к' or playerMove == 'н' or playerMove == 'б':
            break
        print('Введите "к", "н", "б", или "в".')
    if playerMove == 'к':
        print('Камень и ...')
    elif playerMove == 'н':
        print('Ножницы и ...')
    elif playerMove == 'б':
        print('Бумага и ...')


    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'к'
        print('Камень')
    elif randomNumber == 2:
        computerMove = 'н'
        print('Ножницы')
    elif randomNumber == 3:
        computerMove = 'б'
        print('Бумага')

    if playerMove == computerMove:
       print('Ничья')
       ties = ties + 1
    elif playerMove == 'к' and computerMove == 'н':
        print('Вы выиграли!')
        wins = wins + 1
    elif playerMove == 'н' and computerMove == 'б':
        print('Вы выиграли!')
        wins = wins + 1
    elif playerMove == 'б' and computerMove == 'к':
        print('Вы выиграли!')
        wins = wins + 1
    elif playerMove == 'к' and computerMove == 'б':
        print('Вы проиграли!')
        losses = losses + 1
    elif playerMove == 'б' and computerMove == 'н':
        print('Вы проиграли!')
        losses = losses + 1
    elif playerMove == 'н' and computerMove == 'к':
        print('Вы проиграли!')
        losses = losses + 1



