1. Репозиторий https://github.com/acid-n/
2. Установка VirtualBox под Ubuntu:
- открываем терминал
- вводим команду #sudo apt-get install virtualbox, соглашаемся с запросом на установку всех зависимостей
- запускаем virtualbox

- Скачиваем Ubuntu на сайте https://ubuntu.com/download/desktop

- Уставливаем Ubuntu в Virtualbox:
- нажимаем создать
- вводим имя, папку машины, тип Linux, версия Ubuntu
- указываем объем памяти
- создаем новый виртуальный жесткий диск
- указываем тип VDI
- формат хранения динамический
- размер 10Гб
- далее выбираем в настройках Носитель (скачанный образ ubuntu)

3. Устанавливаем утилиты для гостевой ОС вручную:
- запустили в Virtualbox ОС Ubuntu, подключили образ диска и дальше переходим в раздел где примонтирован диск
- далее запускаем команду #sudo ./autorun.sh
- узнаем что необходимо установить зависимости gcc make perl: #sudo apt-get install gcc make perl
- повторно запускаем установку гостевой ОС #sudo ./autorun.sh

4. В конфигурации виртуальной машины включаем "общий буфер" и заменить NAT сетевой интерфейс на Bridged 

5. Настраиваем SSH
- установка ssh сервера: #sudo apt-get install ssh
- открыть справку #man ufw
- включить службу ssh сервера: #sudo systemctl start sshd
- добавить порт 22 в исключение фаервола: #sudo ufw enable, #sudo ufw allow ssh
- подключаемся #ssh user@ip
- генерируем ssh ключи:
	#ssh-keygen -t rsa
	#ssh-copy-id username@ip
	теперь без проблем попадаем на удаленную машину без пароля