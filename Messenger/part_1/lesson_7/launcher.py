import subprocess
import shlex
import time
import os
import signal


PROCESS = []

while True:

    ANSWER = input('Выберите действие: q - выход, s - запустить сервер и клиенты, x - закрыть все окна: ')

    if ANSWER == 'q':
        break
    elif ANSWER == 's':
        PROCESS.append(subprocess.Popen('gnome-terminal -- python3 server.py', shell=True))
        time.sleep(0.5)
        for i in range(2):
            PROCESS.append(
                subprocess.Popen('gnome-terminal -- python3 client.py -m send', shell=True))
        for i in range(3):
            PROCESS.append(
                subprocess.Popen('gnome-terminal -- python3 client.py -m listen', shell=True))
    elif ANSWER == 'x':
        while PROCESS:
            VICTIM = PROCESS.pop()
            VICTIM.kill()
            VICTIM.terminate()