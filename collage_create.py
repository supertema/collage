import os
import math


import cv2
import numpy as np





# просто ресайзим все картинки по заданным размерам и отправляем в новую директорию
def resizes_pic(image_dir, width, height):
    path = image_dir + '/resize_pic'
    try:
        os.mkdir(path, mode=0o777, dir_fd=None)
    except FileExistsError:
        print('Директория уже существует')
    image_paths = os.listdir(image_dir)
    dim = (width, height)
    try:
        for pic in image_paths:
            image1 = cv2.imread(pic)
            image2 = cv2.resize(image1, dim)
            cv2.imshow("Original image", image2)
            cv2.imwrite(os.path.join(path , 'resize_' + pic), image2)
    except:
        print('Случилась ошибка, но это не беда - все работает)', )


# resizes_pic('/home/supertema/python_project/gallery/pic', 150, 150)


# width = 300
# height = 300
# dim = (width, height)
#
# image1 = cv2.imread("4vqqsNB7Urs.jpg")
# image2 = cv2.imread("7fN6TmXp5jM.jpg")
# image1 = cv2.resize(image1, dim)
# image2 = cv2.resize(image2, dim)
# col1 = np.vstack([image1, image2])
#
# cv2.imshow("Original image", col1)
# cv2.waitKey(0)


#создаем коллаж
def create_collages(image_dir, w, h):
    image_paths = os.listdir(image_dir)
    list_img = [] # список в котором будут списки с картинками
    k = 0 # счетчик картинок в директории
    # создаем двуменрый массив c картинками
    for i in range(w): # ширина коллажа
        list_img.append([])
        for j in range(h): # высота коллажа
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



create_collages('/home/supertema/python_project/gallery/pic/resize_pic', 4, 6)


# def create_collages(image_dir):
#     image_paths = os.listdir(image_dir)
#     n = len(image_paths) # 16
#     # find nearest square
#     collage_size = int(math.floor(math.sqrt(len(image_paths)))) # 4
#
#     # horizontally stacking images to create rows
#     rows = []
#     k = 0 # counter for number of rows
#     for i in range(collage_size**2): # 0,16
#         if i % collage_size == 0: # finished with row, start new one
#             if k > 0:
#                 rows.append(cur_row)
#             cur_row = cv2.imread(os.path.join(image_dir, image_paths[i]))
#             k += 1
#         else:             # continue stacking images to current row
#             cur_img = cv2.imread(os.path.join(image_dir, image_paths[i]))
#             cur_row = np.hstack([cur_row, cur_img])
#
#         # vertically stacking rows to create final collage.
#         collage = rows[0]
#
#         for i in range(1, len(rows)):
#             collage = np.vstack([collage, rows[i]])
#
#     return collage
#
# create_collages('/home/supertema/python_project/gallery/pic/resize_pic')
