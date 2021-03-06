## Оглавление
1. Сборка проекта и локальный запуск
    * Клонируем репозиторий
    * Настройка
    * Запуск
    * Открытие OpenApi(swager)
    * Пример запуска
2. Запуск тестов


___

## Сборка проекта и локальный запуск:
### Клонируем репозиторий
Выполните в консоли

`git clone https://github.com/Madixxx22/quiz_rest_api`

### Настройка
Создайте .env файл в том же каталоге что и docker-compose.yaml, и добавьте следующие параметры
```
DB_USER
DB_HOST
DB_PASSWORD
DB_NAME

POSTGRES_USER
POSTGRES_DB
POSTGRES_PASSWORD

PGADMIN_DEFAULT_EMAIL
PGADMIN_DEFAULT_PASSWORD
PGADMIN_CONFIG_SERVER_MODE=
```
### Запуск
Установите docker desktop с оффициального сайта и запустите(если на windows или macos)
https://eternalhost.net/base/vps-vds/ustanovka-docker-linux (Воспользуйтесь инструкцией для Linux)

В консоле находясь в каталоге с файлом docker-compose.yaml запускаем команду
`docker-compose up` 
Если все было установлено и настроено корректно приложения запустится, кроме back end(http://127.0.0.1:8008) развернется postgresql и pgadmin(http://127.0.0.1:5050)

### Открытие OpenApi(swager)
Перейдя по ссылке http://127.0.0.1:8008/docs мы откроем автоматически сгенерированную документацию openapi swager

### Пример запуска
Если первого запроса нет.
![](https://github.com/Madixxx22/quiz_rest_api/blob/master/img/1.jpg)
![](https://github.com/Madixxx22/quiz_rest_api/blob/master/img/2.jpg)
 ____
 
 Если в базе есть вопросы и он выдает последний.
 ![](https://github.com/Madixxx22/quiz_rest_api/blob/master/img/3.jpg)
 ![](https://github.com/Madixxx22/quiz_rest_api/blob/master/img/4.jpg)

## Запуск тестов
Тесты можно запустить и проверить работоспособность программы при запущенных docker контейнерах. 1 тест на пустой БД завершится с успехом. При непустой Бд мы от 1 теста ожидаем ошибку. обработал xfailed из pytest
`docker-compose exec app python -m pytest app/tests`



Если обновляете БД проведите миграции с помощью *alembic* при запущенном контейнере. Обновление миграции произведите или перезапустив контейнер или вручную `alembic upgrade head` 
