# API социальной сети Yatube

## Описание проекта:

Это продолжение проекта Yatube - блога для публикации постов, комментирования и подписок на избранных авторов. 
К Yatube добавили API, чтобы появилась возможность обращаться к нему и делать запросы.
Также для проекта разработана документация. При запуске можно перейти на /redoc, чтобы с ней ознакомиться.

#### Документация к API доступна по адресу [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/) после запуска проекта

## Стек технологий

- Python 3.7
- Django 2.2.16
- Django REST Framework 3.12.4
- Djangorestframework-simplejwt 4.7.2
- Git

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

``` 
git clone git@github.com:LianaVolkova/api_final_yatube.git
```

``` 
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

``` 
python -m venv env
```

``` 
source venv/Scripts/activate
```

``` 
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

``` 
pip install -r requirements.txt
```

Выполнить миграции:

``` 
python manage.py migrate
```

Запустить проект:

``` 
python manage.py runserver
```

### Примеры запросов:

Получить список всех постов:     
``` 
GET /api/v1/posts/
```  

Добавление нового поста:  
``` 
POST /api/v1/posts/
```   

Получить список всех групп:  
``` 
GET /api/v1/groups/
```  

Добавление нового комментария:  
``` 
POST /api/v1/posts/{post_id}/comments/
```  

Удаление комментария по id:  
``` 
DELETE /api/v1/posts/{post_id}/comments/{id}/
```

Получение списока подписок:  
``` 
GET /api/v1/follow/
```  

Подписка пользователя на пользователя переданного в запросе:  
``` 
POST /api/v1/follow/
```

#### Полный список запросов API находятся в документации

### Автор

Волкова Лиана
