### Проект Yatube

**Yatube**  это агрегатор всех авторов в мире, которые повествуют о чем угодно, выкладывая свои посты. Вы можете опубликовать пост в какой-нибудь группе по интересам, а так же приложить к посту фото. Можете прокомментировать любую публикацию и подписаться на любимого автора. Благодаря API вы теперь можете автоматически опубликовать пост на Yatube, когда пишете его в социальной сети!

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/Palashnenkoff/api_final_yatube
```
```
cd api_final_yatube
```
Cоздать и активировать виртуальное окружение:
```
python -m venv env
```
###### *на **Winows** часто вместо 'python' просто 'python3'
```
source env/bin/activate или source venv/Scripts/activate (на Windows)
```
Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
```

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
***

* Получить все посты (GET запрос)
```
http://127.0.0.1:8000/api/v1/posts/
```
Ответ
```
[
    {
        "id": 1,
        "author": "string",
        "text": "string",
        "pub_date": "2019-08-24T14:15:22Z",
        "image": "string",
        "group": 0
    }
]
```
При указании параметров limit и offset выдача должна работает с пагинацией!
***
* Получить конкретный пост (GET запрос)
```
http://127.0.0.1:8000/api/v1/posts/{id}/
```
***
* Создать пост (POST запрос)
```
http://127.0.0.1:8000/api/v1/posts/
```
В теле запроса: 
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
###### Поля "image" и "group" необязательные
***
* Подписаться на автора (POST запрос)
```
http://127.0.0.1:8000/api/v1/follow/
```
В теле запроса: 
```
{
  "following": "string(username автора)"
}
```
***
**Для знакомства со всем возможностями проекта запустите локальный сервер и посетите** [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
***

