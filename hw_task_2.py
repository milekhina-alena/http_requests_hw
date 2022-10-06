import requests


class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'0Auth {self.token}'
        }

    def _get_upload_link(self, file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    # def upload(self, file_path: str):
    #     url = 'https://dev.yandex.net/disk-polygon/?lang=ru&tld=ru#!/v147disk47resources/PublishResource'
    #     headers = self.get_headers()
    #     params = {'path': file_path, 'overwrite': 'true'}
    #     pesponse = requests.put()
    #     pass

    def upload_file_to_disk(self, file_path, filename):
        href = self._get_upload_link(file_path=file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")

my_token = 'y0_AgAAAAA8HMbLAADLWwAAAADQWpZPW-W6lf4OTJqmME1qqsxP9UR6UDk'

# Netology/test   test.txt
if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = ...
    token = my_token
    uploader = YaUploader(token)
    result = uploader.upload_file_to_disk('Netology/test', 'test.txt')
    print(result)
