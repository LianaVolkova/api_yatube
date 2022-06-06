### Описание проекта:

Проект API для Yatube
Это продолжение проекта Yatube - блога для публикации постов, комментирования и подписок на избранных авторов. 
К Yatube добавили API, чтобы появилась возможность обращаться к нему и делать запросы.
Также для проекта разработана документация. При запуске можно перейти на /redoc, чтобы с ней ознакомиться.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:LianaVolkova/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры запросов:

Пример POST-запроса: добавление нового поста.

```
POST .../api/v1/posts/
```

```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```

Пример ответа:

```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

Пример GET-запроса: получение комментариев.

```
GET .../api/v1/posts/{post_id}/comments/
```

Пример ответа:

```
[
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
  }
]
```
