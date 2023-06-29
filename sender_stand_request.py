import requests
import configuration
import data


# Функция запроса на создание нового пользователя
def post_new_user(test_body):
    # Составление URL запроса
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, headers=data.headers, json=test_body)


# Функция запроса на получение информации из таблицы БД
def get_users_table():
    # Составление URL запроса
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)
