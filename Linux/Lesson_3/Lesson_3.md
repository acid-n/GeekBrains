1. Создать файл file1 и наполнить его произвольным содержимым. Скопировать его в file2. Создать символическую ссылку file3 на file1. Создать жесткую ссылку file4 на file1. Посмотреть, какие айноды у файлов. Удалить file1. Что стало с остальными созданными файлами? Попробовать вывести их на экран.
#echo "Hello world" > file1
#cp file1 file2
#ln -s file1 file3
#ln file1 file4
#ls -li
итого 12
1974591 -rw-r--r-- 2 nikolay nikolay 12 фев 26 12:50 file1
1974695 -rw-r--r-- 1 nikolay nikolay 12 фев 26 12:50 file2
1974696 lrwxrwxrwx 1 nikolay nikolay  5 фев 26 12:52 file3 -> file1
1974591 -rw-r--r-- 2 nikolay nikolay 12 фев 26 12:50 file4
#rm file1
#ls -li
итого 8
1974695 -rw-r--r-- 1 nikolay nikolay 12 фев 26 12:50 file2
1974696 lrwxrwxrwx 1 nikolay nikolay  5 фев 26 12:52 file3 -> file1
1974591 -rw-r--r-- 1 nikolay nikolay 12 фев 26 12:50 file4
#cat file2
Hello World
#cat file3
cat: file3: Нет такого файла или каталога
#cat file4
Hello World


2. Дать созданным файлам другие, произвольные имена. Создать новую символическую ссылку. Переместить ссылки в другую директорию.
#mv file2 new_file
#mv file4 hardlink
#ls -li
итого 8
1974591 -rw-r--r-- 1 nikolay nikolay 12 фев 26 12:50 hardlink
1974695 -rw-r--r-- 1 nikolay nikolay 12 фев 26 12:50 new_file
#ln -s new_file softlink
#mkdir newtemp
#mv new_file newtemp/
#mv hardlink newtemp/
#ls -li newtemp/
итого 8
1974591 -rw-r--r-- 1 nikolay nikolay 12 фев 26 12:50 hardlink
1974695 -rw-r--r-- 1 nikolay nikolay 12 фев 26 12:50 new_file

3. Создать два произвольных файла. Первому присвоить права на чтение, запись для владельца и группы, только на чтение для всех. Второму присвоить права на чтение, запись только для владельца. Сделать это в численном и символьном виде.
#touch file1 file2
#ls -al
итого 8
drwxr-xr-x  2 nikolay nikolay 4096 фев 26 13:32 .
drwxr-xr-x 35 nikolay nikolay 4096 фев 25 21:55 ..
-rw-r--r--  1 nikolay nikolay    0 фев 26 13:32 file1
-rw-r--r--  1 nikolay nikolay    0 фев 26 13:32 file2
#chmod ug+rw file1
#chmod 664 file1
#chmod u+rw file2
#chmod 600 file 2
#ls -al
итого 8
drwxr-xr-x  2 nikolay nikolay 4096 фев 26 13:32 .
drwxr-xr-x 35 nikolay nikolay 4096 фев 25 21:55 ..
-rw-rw-r--  1 nikolay nikolay    0 фев 26 13:32 file1
-rw-------  1 nikolay nikolay    0 фев 26 13:32 file2

4. Создать пользователя, обладающего возможностью выполнять действия от имени суперпользователя.
#sudo useradd -o -u 0 -g 0 -s /bin/bash newroot
#su newroot
Пароль: 
root@nikolay-MS-7918:/home/nikolay#
