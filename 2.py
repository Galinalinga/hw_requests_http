import requests
import json

import yadisk

token = 'TOKEN'

  # y = yadisk.YaDisk(token='TOKEN')
  # print(y.check_token())  # Проверим токен (вывод True)


class YaUploader:
    def __init__(self, _token: str):
        self.token = _token

    def upload(self, file_path):
 
        # запрос для получения ссылки
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        # имя загружаемого файла
        filename = file_path.split('/', )[-1]
        #  формат заголовков запроса
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}
        #  параметры запроса 
        params = {"path": f"Загрузки/{filename}", "overwrite": "true"}
        # запрос на получение ссылки для загрузки
        _response = requests.get(upload_url, headers=headers, params=params).json()
        #  ссылка для загрузки
        href = _response.get("href", "")
        # запрос на загрузку файла 
        responce = requests.put(href, data=open(file_path, 'rb'))
        #статус отправки файла
        responce.raise_for_status()
   
        if responce.status_code == 201:
            return 'Успешно'
        else:
            return f"Ошибка загрузки! Код ошибки: {responce.status_code}"

#
if __name__ == '__main__':
    # Получаем путь к загружаемому файлу и токен от пользователя
    path_to_file = 'Новый документ.txt'  
    token = 'TOKEN'  
    # экземпляр класса для токена 
    uploader = YaUploader(token)
    # Загружаем файл на диск
    print(f"Загружаем файл {path_to_file.split('/', )[-1]} на Яндекс.Диск")
    result = uploader.upload(path_to_file)
    print(result)