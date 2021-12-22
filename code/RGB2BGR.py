import cv2 as cv
import os

while 1:
    animal = str(input('animals >>>'))

    file_path = 'downloads/pictures/' + animal
    print(file_path)
    file_names = os.listdir(file_path)
    i = 1

    for name in file_names:
        print(name)
        img_color = cv.imread(file_path + '/' + name)

        # cv.imshow("result", img_color)
        cv.waitKey(0)

        img_gray = cv.cvtColor(img_color, cv.COLOR_RGB2GRAY)
        # cv.imshow("result", img_gray)
        src = 'BGR_img/' + animal + '/' + str(i) + '.jpg'
        cv.imwrite(src, img_gray)
        cv.waitKey(0)
        i += 1
