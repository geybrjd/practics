import random

massages = ['It is certain', 'It is decidedly', 'Yes', 'Rply hazy try again', \
        'ask again later', 'Concentrate and ask again', 'My reply is no', \
        'Outlook not so good', 'Very doubtful']
print(massages[random.randint(0, len(massages) -1)])    

# Здесь random.randint(0, len(massages) -1) говорит о том, что список индексов от нуля до (-1) самого последнего
# Это позволяет делать список более гибким. Если список будет от 0 до 9 и мы уберем или добавим в списко еще одно значение.
