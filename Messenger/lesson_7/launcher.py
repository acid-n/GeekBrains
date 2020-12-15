import subprocess
import shlex

PROCESS = []

while True:

    ANSWER = input('Выберите действие: q - выход, s - запустить сервер и клиенты, x - закрыть все окна: ')

    if ANSWER == 'q':
        break
    elif ANSWER == 's':
        PROCESS.append(subprocess.Popen(
            shlex.split("""x-terminal-emulator -e 'python3 server.py'"""),
            stdout=subprocess.PIPE
            # 'python3 server.py',
            # shell=True
            # creationflags=subprocess.CREATE_NEW_CONSOLE
        ))
        for i in range(2):
            PROCESS.append(subprocess.Popen(
                shlex.split("""x-terminal-emulator -e 'python3 client.py -m send'"""),
                stdout=subprocess.PIPE
                # 'python3 client.py',
                # shell=True
                # creationflags=subprocess.CREATE_NEW_CONSOLE
            ))
        for i in range(3):
            PROCESS.append(subprocess.Popen(
                shlex.split("""x-terminal-emulator -e 'python3 client.py -m listen'"""),
                stdout=subprocess.PIPE
                # 'python3 client.py',
                # shell=True
                # creationflags=subprocess.CREATE_NEW_CONSOLE
            ))
    elif ANSWER == 'x':
        while PROCESS:
            VICTIM = PROCESS.pop()
            VICTIM.kill()
