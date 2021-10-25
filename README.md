### Проект Yatube (REST API)

**Yatube**  это агрегатор всех авторов в мире, которые повествуют о чем угодно, выкладывая свои посты. Вы можете опубликовать пост в какой-нибудь группе по интересам, а так же приложить к посту фото. Можете прокомментировать любую публикацию и подписаться на любимого автора. Благодаря API вы теперь можете автоматически опубликовать пост на Yatube, когда пишете его в социальной сети!

## Используемые технологии

![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/Palashnenkoff/Yatube_REST_API.git
```
```
cd Yatube_REST_API
```
Cоздать и активировать виртуальное окружение (для Windows):
###### * для Mac или Linux 'python3 -m venv venv'  
```
python -m venv venv
```
###### * для Mac или Linux 'source venv/bin/activate' 
```
source venv/Scripts/activate 
```
Обновить pip и установить зависимости:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Зайти в директорию приложения и выполнить миграции:
```
cd yatube_api
```
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
При указании параметров limit и offset выдача работает с пагинацией!
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

