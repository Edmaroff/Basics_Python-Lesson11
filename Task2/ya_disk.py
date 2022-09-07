import requests


class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_upload_link(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json().get('href', '')

    def upload_file_to_disk(self, disk_file_path):
        href = self.get_upload_link(disk_file_path)
        response = requests.put(href, data=open(disk_file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print(f'Файл "{disk_file_path}" загружен')

    def upload_list_files_to_disk(self, list_files):
        for file in list_files:
            self.upload_file_to_disk(file)
