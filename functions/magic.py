import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        print('yes')
    elif answerNumber == 2:
        print ('no')
r = random.randint(1, 2)
fortune = getAnswer(r)
print(fortune)
