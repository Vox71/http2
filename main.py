import requests


class YandexDisk:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        file_name = file_path.split('/')[-1]
        headers = {"Authorization": f"OAuth {self.token}"}
        response = requests.get("https://cloud-api.yandex.net/v1/disk/resources/upload", params={"path": file_name},
                                headers=headers
                                )
        href = response.json()["href"]

        with open(file_path, "r") as i:
            upload_response = requests.put(href, files={"file": i})
            upload_response.raise_for_status()
        return 'Загрузка завершена'


if __name__ == '__main__':
    uploader = YandexDisk('')  # токен
    result = uploader.upload('queen/bohemian_rhapsody.txt')
    print(result)
