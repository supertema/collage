import os
import math
import shutil
import threading


import cv2
import numpy as np


import vk_pars


s = int(input('Задайте размер стороны ячейки:'))
h_collage = int(input('Задайте количество ячеек коллажа по вертикали:'))
w_collage = int(input('Задайте количество ячеек коллажа по горизонтали:'))
id = int(input('Введите ID пользователя Вконтакте в числовом формате (только цифры):'))
n = int(input('Задайте общее количество картинок для коллажа:'))


# s = 100
# h_collage = 5
# w_collage = 8
# id =
# n = 60


vk_pars.main(id, n)


# проверяем, есть ли папка, если нет - создаем
def create_path(image_dir):
    path = image_dir + '/resize_pic'
    if os.path.isdir(path):
        pass
    else:
        try:
            os.mkdir(path)
        except FileExistsError:
            print('Директория уже существует')
        pass


create_path(os.getcwd() + '/pic')


# делаем картинки квадратными
def get_square(image_dir, size):
    path = image_dir + '/resize_pic'
    image_paths = os.listdir(image_dir)
    for pic in image_paths:
        image = cv2.imread(os.getcwd() + '/pic/' + pic)
        if image is None:
            print('В папке больше нет картинок')
        else:
            h = image.shape[0]
            w = image.shape[1]
            if len(image.shape) < 3:
                c = None
            else:
                c = image.shape[2]
            if h > w:
                dif = h
            else:
                dif = w
            x_pos = int((dif - w)/2.)
            y_pos = int((dif - h)/2.)
            if c is None:
                mask = np.zeros((dif, dif), dtype=image.dtype)
                mask[y_pos:y_pos+h, x_pos:x_pos+w] = image[:h, :w]
            else:
                mask = np.zeros((dif, dif, c), dtype=image.dtype)
                mask[y_pos:y_pos+h, x_pos:x_pos+w, :] = image[:h, :w, :]
                p = cv2.resize(mask, (size, size), cv2.INTER_AREA)
                cv2.imwrite(os.path.join(path , 'resize_' + pic), p)


get_square(os.getcwd() + '/pic', s)


# ресайзим заглушку
def mock_resize(size):
    mock = cv2.imread(os.getcwd() + '/mock.jpg')
    width = height = size
    dim = (width, height)
    image = cv2.resize(mock, dim)
    cv2.imwrite(os.getcwd() + '/pic/resize_mock.jpg', image)
    return image


#создаем коллаж
def create_collages(image_dir, w, h, size_m=s):
    image_paths = os.listdir(image_dir)
    list_img = [] # список в котором будут списки с картинками
    k = 0 # счетчик картинок в директории
    # создаем двуменрый массив c картинками
    for i in range(w): # ширина коллажа
        list_img.append([])
        for j in range(h): # высота коллажа
            if k >= len(image_paths):
                list_img[i].append(mock_resize(size_m))
            else:
                pic = cv2.imread(os.path.join(image_dir, image_paths[k]))
                list_img[i].append(pic)
                k += 1

    row = [] # создаем список для стаконных по вертикали картикок

    for i in list_img:
        # i - это тоже список внутри списка
        # подаем на вход методу vstack массив картинок и кладем в переменную
        a = np.vstack(i) # стакаем список по вертикали
        row.append(a) # добавляем список в новый список

    collage = np.hstack(row) # подаем на вход методу hstack массив картинок
    cv2.imshow("Original image", collage)
    cv2.waitKey(0)
    return collage


create_collages(os.getcwd() + '/pic/resize_pic', w_collage, h_collage)


# чистим директории после показа картинки
def delete_dir(dir):
    shutil.rmtree(dir)

delete_dir(os.getcwd() + '/pic')
