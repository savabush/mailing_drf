# Mailing DRF

Сервис разработан на django rest framework с celery, flower, redis, pytest, swagger


## Установка и запуск

1. Склонировать репозиторий с Github:

````
git clone git@github.com:savabush/mailing_drf.git
````
2. Перейти в директорию проекта

3. Создать виртуальное окружение:

````
python -m venv venv
````

4. Активировать окружение: 

````
source \venv\bin\activate
````
5. Файл .env.example переименовать в .env и изменить данные в нем на подходящие вам 
6. Установка зависимостей:

```
pip install -r requirements.txt
```

7. Создать и применить миграции в базу данных:
```
python manage.py makemigrations
python manage.py migrate
```
8. Запустить сервер
```
python manage.py runserver
```
9. Запустить celery
```
celery -A mailing worker -l info -P solo
```
10. Запустить flower

```
celery -A mailing flower --port=5555
```
***
### Запуск тестов
``` 
pytest
```
***
## Установка проекта с помощью docker-compose


1. Склонировать репозиторий с Github
```
git clone git@github.com:savabush/mailing_drf.git
```
2. Перейти в директорию проекта
3. Файл .env.example переименовать в .env и изменить данные в нем на подходящие вам 
4. Запустить контейнеры 
``` 
sudo docker-compose up -d
 ```
5. Остановка работы контейнеров 
```
sudo docker-compose stop
```
***
```http://0.0.0.0:8000/api/v1/``` - api проекта

```http://0.0.0.0:8000/api/v1/clients/``` - клиенты

```http://0.0.0.0:8000/api/v1/clients/<pk>/``` - детальная информация о клиенте

```http://0.0.0.0:8000/api/v1/mailinglist/``` - рассылки

```http://0.0.0.0:8000/api/v1/mailinglist/<pk>/``` - детальная статистика по конкретной рассылке

```http://0.0.0.0:8000/docs/``` - docs проекта, оформленный через swagger

```http://0.0.0.0:5555``` - celery flower

***

**Техзадание:** 
[https://www.craft.do/s/n6OVYFVUpq0o6L](https://www.craft.do/s/n6OVYFVUpq0o6L)

## Дополнительные задания, которые я выполнил

<ol>
<li>организовать тестирование написанного кода</li>
<li>подготовить docker-compose для запуска всех сервисов проекта одной командой</li>
<li>сделать так, чтобы по адресу <i> /docs/ </i> открывалась страница со Swagger UI и в нём отображалось описание разработанного API. Пример: <a href="https://petstore.swagger.io" target="_blank">https://petstore.swagger.io</a></li>
<li>реализовать администраторский Web UI для управления рассылками и получения статистики по отправленным сообщениям</li>
<li>удаленный сервис может быть недоступен, долго отвечать на запросы или выдавать некорректные ответы. Необходимо организовать обработку ошибок и откладывание запросов при неуспехе для последующей повторной отправки. Задержки в работе внешнего сервиса никак не должны оказывать влияние на работу сервиса рассылок.</li>
<li>реализовать дополнительную бизнес-логику: добавить в сущность "рассылка" поле "временной интервал", в котором можно задать промежуток времени, в котором клиентам можно отправлять сообщения с учётом их локального времени. Не отправлять клиенту сообщение, если его локальное время не входит в указанный интервал.</li>
</ol>