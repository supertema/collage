import requests
import json
import os


# #токен приложения
# token = '9b7df9c59b7df9c59b7df9c5fb9b12729999b7d9b7df9c5c546008b95315955624a2eb8'
#
# # запрос для получения токена, живет 24 часа!!!
# # https://oauth.vk.com/authorize?client_id=7310172&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=photos&response_type=token&v=5.74
#
# #токен24
# token2 = 'b5a85bf137628b28860c62ba2308c77a0f754d91b50099b98cecf1f925b3a3ba88fbe213239923bc23528'
#
#
# def write_json(data):
#     with open('response.json', 'w') as file:
#         json.dump(data, file, indent=2, ensure_ascii=True)
#
#
# def get_largetst(size_dict):
#     if size_dict['width'] >= size_dict['height']:
#         return size_dict['width']
#     else:
#         return size_dict['height']
#
# def download_photo(url):
#     r = requests.get(url, stream=True)
#
#     filename = url.split('/')[-1] # получаем имя
#     with open(filename, 'bw') as file:
#         for chunk in r.iter_content(4096): #бьем файл на куски по 4кб
#             file.write(chunk)
#
# # def main():
# #     r = requests.get("https://api.vk.com/method/photos.getAll" ,
# #                         params = {'owner_id': 6270495,
# #                                   'access_token': token2,
# #                                   'v': 5.74,
# #                                   'album_id': 'saved',
# #                                   'need_system': 1,
# #                                   'photo_sizes': 1,
# #                                 })
# #
# #     write_json(r.json())
# #     print(r.json())
#
# photos = json.load(open('response.json'))['response']['items']
# for photo in photos:
#     sizes = photo['sizes']
#
#     max_size_url = max(sizes, key=get_largetst)['src']
#     download_photo(max_size_url)
# #
# #     for size in sizes:
# #         print(size['type'])
# #
# #     print('---------------------')
# # print(photos)
#
# # main()
