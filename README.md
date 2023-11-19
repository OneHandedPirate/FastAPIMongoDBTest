# FastAPI + MongoDB Test

<details>
  <summary>ТЗ</summary>
  
  Web-приложение для определения заполненных форм.
По поводу сроков выполнения: тестовые задания принимаются до тех пор, пока открыта вакансия.

Результат лучше всего присылать ссылкой на репозиторий Github

В базе данных хранится список шаблонов форм.

Шаблон формы, это структура, которая задается уникальным набором полей, с указанием их типов.

Пример шаблона формы:

```
{
    "name": "Form template name",
    "field_name_1": "email",
    "field_name_2": "phone"
}
```


Всего должно поддерживаться четыре типа данных полей:<br> 
email<br>
телефон<br>
дата<br>
текст<br>

Все типы кроме текста должны поддерживать валидацию. Телефон передается в стандартном формате <b>+7 xxx xxx xx xx</b>, дата передается в формате <b>DD.MM.YYYY</b> или <b>YYYY-MM-DD</b>.

Имя шаблона формы задается в свободной форме, например MyForm или Order Form.
Имена полей также задаются в свободной форме (желательно осмысленно), например user_name, order_date или lead_email.

На вход по урлу <b>/get_form</b> POST запросом передаются данные такого вида:
<b>f_name1=value1&f_name2=value2</b>

В ответ нужно вернуть имя шаблона формы, если она была найдена.
Чтобы найти подходящий шаблон нужно выбрать тот, поля которого совпали с полями в присланной форме. Совпадающими считаются поля, у которых совпали имя и тип значения. Полей в пришедшей форме может быть больше чем в шаблоне, в этом случае шаблон все равно будет считаться подходящим. Самое главное, чтобы все поля шаблона присутствовали в форме.

Если подходящей формы не нашлось, вернуть ответ в следующем формате:

```
{
    f_name1: FIELD_TYPE,
    f_name2: FIELD_TYPE
}
```


где FIELD_TYPE это тип поля, выбранный на основе правил валидации, проверка правил должна производиться в следующем порядке дата, телефон, email, текст.

В качестве базы данных рекомендуем использовать tinyDB, вместе с исходниками задания должен поставляться файл с тестовой базой, содержащей шаблоны форм. Но если сможете поднять и использовать контейнер Docker с MongoDB - это будет отличное решение, однако оно может отнять у вас много времени и не является обязательным.

Также в комплекте должен быть скрипт, который совершает тестовые запросы. Если окружение приложения подразумевает что-то выходящее за рамки virtualenv, то все должно быть упаковано в Docker контейнеры или таким способом, чтобы не приходилось ставить дополнительные пакеты и утилиты на машине. Все необходимые действия для настройки и запуска приложения должны находится в файле README.

Версия Python остается на ваш выбор. Мы рекомендуем использовать версию 3.6 и выше.

<b>Входные данные для веб-приложения:</b><br>
Список полей со значениями в теле POST запроса.

<b>Выходные данные:</b><br>
Имя наиболее подходящей данному списку полей формы, при отсутствии совпадений с известными формами произвести типизацию полей на лету и вернуть список полей с их типами.

  
</details>

<hr>

### Требования:

- установленный `docker`;
- установленный `poetry` (опционально);

### Установка

- стянуть репозиторий:<br>`git clone https://github.com/OneHandedPirate/FastAPIMongoDBTest.git`
- перейти в директорию проекта:<br>`cd FastAPIMongoDBTest`
- создать файл `.env` со следующими переменными:<br>`APP_PORT` - порт, на котором будет висеть FastAPI-приложение;<br>`DB_PORT` - порт, на котором будет висеть MongoDB;<br>Можно просто переименовать `.env-example` в `.env` если ваc устраивают порты по умолчанию; 
- если вы используте `poetry`:
    + создать и войти в окружение:<br>`poetry shell`
    + установить зависимости:<br>`poetry install`
- если вы используте `virtualenv`:
    + создайте новое виртуальное откружение:<br>`virtualenv venv`
    + активируйте его:<br>`source venv/bin/activate`
    + установить зависимости проекта:<br>`pip install -r requirements.txt`

### Запуск:
Последовательно выполнить следующие команды:

- `make up_db` - поднимает docker-compose c одним MongoDB-контейнером.
- `make fill_db` - запускает скрипт, который добавляет шаблоны форм в БД (сами шаблоны см. ниже) и выводит количество добавленных в БД шаблонов в консоль.
- `make start_app` - запускает FastAPI-приложение с единственным эндпоинтом - `get_form`.
- `make tests` - запускает скрипт, который делает "тестовые" асинхронные запросы к приложению. В консоли выводятся тела запросов (`Request data`) и возвращаемые из эндпоинта `get_form` данные (`Response data`).


### Описания эндпоинтов:
`/get_form` - методы: `POST`. Метод принимает форму. Если форма содержит поля, отличные от строковых, такая форма считается невалидной (см. Дополнения).<br>- Если переданная форма соответствует какому-либо шаблону из БД:<br>`{"template_name": <имя шаблона>}`;<br>- Если переданная форма не соответствует ни одному шаблону:<br>
```
{
  <имя_поля1>: <тип_поля1>,
  ...........: ...........,
  <имя_поляN>: <тип_поляN>
}
``` 

### Дополнения:
- Структура проекта:<br>
    ```
    FastAPIMongoDBTest/
    ├── src/
    │   ├── database.py
    │   ├── main.py
    │   └── utils/
    │       ├── db_fill.py
    │       ├── utils.py
    │       └── validators.py
    ├── tests/
    │   └── test.py
    ├── .env
    ├── .env-example
    ├── docker-compose-dev.yaml
    ├── environ.py
    ├── Makefile
    ├── poetry.lock
    ├── pyproject.toml
    ├── README.md
    └── requirements.txt
    ```
    + `database.py` - подключение к MongoDB через Motor.
    + `main.py` - файл FastAPI-приложения с эндпоинтом.
    + `db_fill.py` - скрипт, который заполняет БД шаблонами.
    + `utils.py` - вспомогательные функции.
    + `validators.py` - функции валидации полей и формы в целом.
    + `test.py` - тестовые данные и функция отправки "тестовых" запросов.
    + `.env` - файл с переменными окружения.
    + `.env-example` - пример файла `.env` со значениями по умолчанию.
    + `docker-compose-dev.yaml` - docker-compose для поднятия MongoDB.
    + `environ.py` - файл для передачи переменных окружения другим модулям.
    + `Makefile` - файл с make-командами.
    + `poetry.lock` - конфигурационный файл `poetry`.
    + `pyproject.toml` - конфигурационный файл проекта.
    + `README.md` - этот файл.
    + `requirements.txt` - список зависимостей в тестовом варианте.
  

- Так как все типы полей в приложении являются текстовыми (даже телефонный номер, определяется регулярным выражением `^\+7 [0-9]{3} [0-9]{3} [0-9]{2} [0-9]{2}$`), я сделал дополнительную валидацию всей формы и если какое-то поле в переданной в эндпоинт форме не являются текстовыми - возникает ошибка `400` с сообщением `All fields must be of string type`.<br><br> 

- Шаблоны форм:<br>
    ```
     {
          "name": "Registration Form",
          "user_name": "text",
          "user_email": "email",
          "user_phone": "phone",
          "created_at": "date"
     },
     {
          "name": "Order Form",
          "order_id": "text",
          "customer_email": "email",
          "customer_phone": "phone",
          "created_at": "date"
     },
     {
          "name": "Contact Form",
          "contact_name": "text",
          "contact_email": "email",
          "message": "text",
          "submitted_at": "date"
     },
     {
          "name": "Subscription Form",
          "subscriber_email": "email",
          "subscribed_at": "date"
     }
    ```
  