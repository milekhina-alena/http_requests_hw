import requests
from pprint import pprint


class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _get_upload_link(self, file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': file_path, 'overwrite': True}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, file_path):
        href = self._get_upload_link(file_path=file_path).get('href', '')
        with open(file_path, 'rb') as file:
            requests.put(href, files={'file': file})

my_token = 'y0_AgAAAAA8HMbLAAh6dQAAAADQrn3L4JugKVPGS1-uQCFLfKLxhqG5JRU'

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'files/practice.txt'
    token = my_token
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
