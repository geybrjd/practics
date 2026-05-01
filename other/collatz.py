RED = '\033[91m'
RESET = '\033[0m'

def collaz(number):
    if  number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1
try:
    i = int(input("Введите число:"))
    result = collaz(i)
    print(result)
except ValueError:
    print(f"{RED}Ошибка: нужно ввести целое число{RESET}")
