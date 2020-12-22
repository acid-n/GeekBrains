# Получение кода завершения подпроцесса

from subprocess import Popen

# Создаем переменную program и назначаем ей значение gnome-terminal
# После этого передаем ее классу Popen. После запуска увидим, что он мгновенно вернет объект subprocess.Popen
# а вызванное приложение будет выполняться

PROGRAM = 'gnome-terminal'
PROCESS = Popen(PROGRAM)

print(PROCESS)

CODE = PROCESS.wait()

print(PROCESS)
print(CODE)