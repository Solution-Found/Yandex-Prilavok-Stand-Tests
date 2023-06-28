import requests
import configuration
import data


# Эндпоинт создания нового пользователя
def post_new_user(test_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставляем полный url
                         headers=data.headers,  # здесь заголовки
                         json=test_body)  # здесь тело


# Эндпоинт получения информации из таблицы БД
def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)  # подставляем полный url
