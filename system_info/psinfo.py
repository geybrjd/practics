#!/usr/bin/env python

# Сценарий сбора информации о системе
import subprocess

# Команда 1
uname = 'uname'
uname_arg = '-a'
print('Getting system information with %s command:\n' % uname)
subprocess.run([uname, uname_arg])

# Команда 2
diskspace = 'df'
diskspace_arg = '-h'
print('Getting diskspace information %s command:\n' % diskspace)
subprocess.run([diskspace, diskspace_arg])
