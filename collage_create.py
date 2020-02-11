import os
import math


import cv2
import numpy as np

s = int(input('Задайте размер стороны ячейки:'))
h_collage = int(input('Задайте количество ячеек коллажа по вертикали:'))
w_collage = int(input('Задайте количество ячеек коллажа по диагонали:'))

def get_square(image_dir, size):
    path = image_dir + '/resize_pic'
    try:
        os.mkdir(path)
    except FileExistsError:
        print('Директория уже существует')
    image_paths = os.listdir(image_dir)

    for pic in image_paths:
        image = cv2.imread('/home/supertema/python_project/gallery/pic/' + pic)
        if image is None:
            print('В папке нет картинок')
        else:
            h = image.shape[0]
            w = image.shape[1]
            if len(image.shape) < 3:
                c = None
            else:
                c = image.shape[2]
            if h == w:
                return cv2.resize(image, (size, size), cv2.INTER_AREA)
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
                cv2.waitKey(0)


get_square('/home/supertema/python_project/gallery/pic/', s)





# ресайзим заглушку
def mock_resize(size):
    path = os.getcwd() + 'pic/resize_pic'
    mock = cv2.imread('/home/supertema/python_project/gallery/mock.jpg')
    width = height = size
    dim = (width, height)
    image = cv2.resize(mock, dim)
    cv2.imwrite('/home/supertema/python_project/gallery/m.jpg', image)
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

create_collages('/home/supertema/python_project/gallery/pic/resize_pic', w_collage, h_collage)
