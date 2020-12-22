import logging
import sys

# Создаем регистратор верхнего уровня с именем 'app'
app_log = logging.getLogger('app')
app_log.setLevel(logging.INFO)
app_log.propagate = False

# Добавляем несколько обработчиков в регистратор 'app'
app_log.addHandler(logging.FileHandler('app.log'))
app_log.addHandler(logging.StreamHandler(sys.stderr))

# Отправить несколько сообщений. Они попадут в файл и будут выведены в поток
app_log.critical('Creeping death detected!')
app_log.info('FYI')