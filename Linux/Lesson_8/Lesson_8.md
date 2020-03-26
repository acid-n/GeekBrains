1) Для создания образа копируем все файлы в папку
2) создаем образ
#docker build . -t flaskapp

3) запускаем образ
#docker run -ti --rm --hostname flaskapp -v $(pwd)/socket/:/opt/socket/ --name flaskapp flaskapp

4) запускаем контейнер nginx
#docker run -ti --rm -p 80:80 -v $(pwd)/flaskapp.conf:/etc/nginx/conf.d/default.conf -v $(pwd)/socket:/socket --name nginx nginx:alpine

ДЗ выполнено

есть момент, в Ubuntu Server 18 столкнулся, что при вызове контейнера ругается на сокеты (вообще не очень эту тему понял)

[uWSGI] getting INI configuration from /opt/params.ini
*** Starting uWSGI 2.0.18 (64bit) on [Wed Mar 25 21:14:43 2020] ***
compiled with version: 9.2.0 on 25 March 2020 20:42:19
os: Linux-4.15.0-91-generic #92-Ubuntu SMP Fri Feb 28 11:09:48 UTC 2020
nodename: flaskapp
machine: x86_64
clock source: unix
detected number of CPU cores: 1
current working directory: /opt
detected binary path: /usr/local/bin/uwsgi
!!! no internal routing support, rebuild with pcre support !!!
setuid() to 101
chdir() to /opt
your processes number limit is 7727
your memory page size is 4096 bytes
detected max file descriptor number: 1024
lock engine: pthread robust mutexes
thunder lock: disabled (you can enable it with --thunder-lock)
bind(): Permission denied [core/socket.c line 230]

