**Новогодние поздравления и предсказания**

Краткая инструкция:
На новогодней открытке елка с подарками. Можно выбрать любой подарок
и получить новогодное предсказание.

Можно передать подарок под елкой любым адресатам.
Для этого нужно кликнуть снеговика на елке и в появившейся форме набрать поздравление.
После отправления сообщения в буфер обмена будет сохранен URL адрес, который нужно 
передать адресатам. 

Перейдя по такой ссылке адресат увидит один большой подарок поделкой, 
кликнув по которому сможет прочитать оставленное сообщение.

Предусмотрено воспроизведение музыки, но она не всегда автоматичеси стартует в зависимости от браузера.

Проект на Django. Использует БД sqlite3.
Данные в программе анонимны, поэтому специальные меры безопасности не применяются.


**Установка**


- Скачать репозиторий через GIT:

git clone https://github.com/avdivo/happy_new_year

- Перейти в папку проекта:

cd happy_new_year/

- Для запуска проекта в контейнерах выполнить:

docker-compose up -d --build

В контейнере есть подготовленная база данных.
При необходимости после клонирования ее можно пересоздать.

- Открыть браузер и перейти по адресу:

http://0.0.0.0:8003/hny


-------------------------------------------


- Для установки без докеризации:

- Перейти в папку проекта:

cd happy_new_year/

- Создать виртуальное окружение:

virtualenv venv

- Активировать виртуальное окружение:

source venv/bin/activate

- Установить зависимости:

pip install -r requirements.txt

- - Если нужно создать новую база данных нужно удалить файл db.sqlite3

- Запустить миграции:

python manage.py makemigrations happy_new_year

python manage.py migrate

- Экспортировать файл фикстур (его подготовка описана в папке utils):

python manage.py loaddata fixture_prediction.json

- Запустить сервер:

python3 manage.py runserver

- Открыть браузер и перейти по адресу:

http://127.0.0.1:8000/hny