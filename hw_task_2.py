import os
import requests
import json

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _create_folder(self, folder_name):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        requests.put(f'{url}?path={folder_name}', headers=headers)
        

    def upload(self, file_path):
        headers = self.get_headers()
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        self._create_folder('Downloads')
        file_name = os.path.basename(file_path)
        result = requests.get(f'{url}/upload?path=Downloads/{file_name}&overwrite={False}', headers=headers).json()
        with open(file_path, 'rb') as file:
            try:
                requests.put(result['href'], files={'file': file})
            except KeyError:
                print(result)


if __name__ == '__main__':
    file_path = 'files/practice.txt'
    token = ''
    uploader = YaUploader(token)
    uploader.upload(file_path)