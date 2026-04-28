#!/usr/bin/env python
# Сценарий сбора информации о системе
import subprocess

# Команда 1
def uname_func():

    uname = 'uname'
    uname_arg = '-a'
    print('Gathering system information with %s command: \n' % uname)
    subprocess.run([uname, uname_arg])

# Команда 2
def disk_func():

    diskspace = 'df'
    diskspace_arg = '-h'
    print('Gathering diskspace information %s command: \n' % diskspace)
    subprocess.run([diskspace, diskspace_arg])

def list_func():
    lists_cmd = 'ls'
    lists_arg = '-lah'
    print(' Lists files with size in directory %s command: \n' % lists_cmd)
    subprocess.run([lists_cmd, lists_arg])

# Главная функция, которая вызывает остальные функции
def main():
    uname_func()
    disk_func()
    list_func()

if __name__ == '__main__':
    main()
