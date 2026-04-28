# Очень короткий сценарий использующий програмный код из pysysinfo_func
from pysysinfo_func import disk_func
import subprocess
def tmp_space():
    tmp_usage = 'du'
    tmp_arg = '-h'
    path = '/tmp'
    print ('Space used in /tmp directory')
    subprocess.run([tmp_usage, tmp_arg, path])

def main():
    disk_func()
    tmp_space()

if __name__ == '__main__':
    main()
