import requests
import json
import os


# на место client_id вставляем ID созданного приложения, вставляем в строку браузера и даем разрешение
# получаем токен который живет 24 часа!
'https://oauth.vk.com/authorize?client_id=7316510&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=photos&response_type=token&v=5.74'


# полученный токен вставляем сюда
token = '5bdba3c73d66bfb2329e0f584e985087f4f727353485c71a5fcc52c018e87d4ef4b848fa68c2f915926e7'


def write_json(data):
    with open('response.json', 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=True)


def get_largetst(size_dict):
    if size_dict['width'] >= size_dict['height']:
        return size_dict['width']
    else:
        return size_dict['height']


def download_photo(url):
    path = os.getcwd() + '/pic'
    if os.path.isdir(path): # проверяем есть ли путь
        r = requests.get(url, stream=True)

        filename = url.split('/')[-1] # получаем имя
        with open(os.path.join(os.getcwd() + '/pic', filename), 'bw') as file:
            for chunk in r.iter_content(4096): #бьем файл на куски по 4кб
                file.write(chunk)
    else:
        try:
            os.mkdir(path)
        except FileExistsError:
            print('Директория уже существует')

def main(id, n_img):
    r = requests.get("https://api.vk.com/method/photos.getAll" ,
                        params = {'owner_id': id,
                                  'access_token': token,
                                  'v': 5.74,
                                  'album_id': 'saved',
                                  'need_system': 1,
                                  'photo_sizes': 1,
                                  'count': n_img,
                                })
    write_json(r.json())

    photos = json.load(open('response.json'))['response']['items']
    for photo in photos:
        sizes = photo['sizes']

        max_size_url = max(sizes, key=get_largetst)['src']
        download_photo(max_size_url)
