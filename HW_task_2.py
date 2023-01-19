import requests
from pprint import pprint
import copy
import time

# Проверим правильность работы Яндекс.Диск REST API. Написать тесты, проверяющий создание папки на Диске.
# Используя библиотеку requests напишите unit-test на верный ответ и возможные отрицательные тесты на ответы с ошибкой
#
# Пример положительных тестов:
# Код ответа соответствует 200.
# Результат создания папки - папка появилась в списке файлов.

def get_token_ya_ru():
    with open('ya_ru_token.txt', 'r') as file_obj:
        token = file_obj.read().strip()
    return token

class ya_disk():
    def __init__(self, token):
        self.token = token

    def create_folder(self, path = 'temp_folder'):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {'Authorization': f'OAuth {self.token}'}
        params = {'path': path, 'overwrite': 'true'}
        response = requests.put(url, headers=headers, params=params)
        if response.status_code == 201:
            print(f'folder "{path}" created successfully')
        else:
            print(f'folder "{path}" not created')
        return response.status_code

    def del_folder(self, path):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {'Authorization': f'OAuth {self.token}'}
        params = {'path': path, 'overwrite': 'true'}
        response = requests.delete(url, headers=headers, params=params)
        status = response.status_code
        if status == 204:
            print(f'folder "{path}" deleted successfully')
        else:
            print(f'folder "{path}" not deleted')
        return status

    def getInfo(self, path):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {'Authorization': f'OAuth {self.token}'}
        params = {'path': path}
        response = requests.get(url, headers=headers, params=params)
        return response.status_code

if __name__ == '__main__':
    token = get_token_ya_ru()
    creater = ya_disk(token)
    creater.del_folder('new_folder')
    # creater.create_folder('new_folder')
    creater.getInfo('new_folder')

