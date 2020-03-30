# Employee search from csv file

Это веб приложение для поиска сотрудников по имени и фамилии

## Запуск программы 

Есть 2 способа запуска программы :

### Способ 1 Запуск скрипта

У вас должен быть установлен python3 , его можно скачать по этой ссылке  https://www.python.org/downloads/

Дальше установить зависимости командой `pip install -r requirements.txt`

И запустить скрипт с помощью `python3 manage.py runserver`

### Способ 2 Запуск через Docker 

У вас должен быть установлен Docker 
https://docs.docker.com/install/
и docker-compose 
https://docs.docker.com/compose/install/

Дальше нужно собрать docker-compose :

`docker-compose build`

Запуск производится с помощью :

`docker-compose up`

Чтобы открыть проект необходимо перейти по адресу:

http://0.0.0.0:8000/

*Все команды запускать из корневой папки проекта (где находится dockerfile и manage.py)




