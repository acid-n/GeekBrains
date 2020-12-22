# Запуск скрипта-дочернего процесса

from subprocess import Popen, PIPE

PROC = Popen(
    'python3 text_ex.py',
    shell=True,
    stdout=PIPE, stderr=PIPE
)

RES = PROC.communicate()
print(PROC.returncode)
if PROC.returncode == 0:
    print(RES)
print(f'result: {RES[0]}')