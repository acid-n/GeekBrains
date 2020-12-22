# Дочерний процесс запуска консольной команды

from subprocess import call, Popen, PIPE
import chardet

# Класс subprocess.Popen - выполняет программу в новом процессе
# Popen не дожидается конца выполения вызванного процесса (он завершается, а запущенное приложение висит)

# stdin и stdout это файлоподобные объекты, предоставляемые os
# stdout=PIPE - стандартный поток вывода
# вывод результатов выполнения команды декодированием
# shell=True выполнение кода через оболочку

PROC = Popen("dir", shell=True, stdout=PIPE)
print(PROC)
OUT = PROC.stdout.read().decode('utf-8')

# Мы знаем в чем нужно декодировать
# но нам помогает модуль chardet
PROC = Popen("dir", shell=True, stdout=PIPE)
DATA = PROC.stdout.read()
RESULT = chardet.detect(DATA)
print(RESULT)
OUT = DATA.decode(RESULT['encoding'])
print(OUT)

# Popen поддерживает менеджеры контекста
with Popen("dir", shell=True, stdout=PIPE) as p:
    out = p.stdout.read().decode('utf-8')
    print(out)