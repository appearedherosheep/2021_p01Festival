from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import random as rd
# dict = {0: '강아지', 1: '고양이', 2: '심해어', 3: '개구리', 4: '부엉이', 5: '라쿤', 6: '타조'}
# dict = {0: '강아지', 1: '고양이', 2: '심해어', 3: '타조', 4: '다람쥐', 5: '호랑이', 6: '오랑우탄', 7: '나무늘보', 8: '말'}
# dict = {0: '고양이', 1: '강아지', 2: '개구리', 3: '원숭이', 4: '오랑우탄', 5: '부엉이', 6: '라쿤', 7: '타조'}
# dict = {0: '고양이', 1: '강아지', 2: '오랑우탄', 3: '심해어', 4: '말', 5: '다람쥐', 6: '라쿤', 7: '타조'}
# dict = {0: '고양이', 1: '강아지', 2: '오랑우탄', 3: '심해어', 4: '말', 5: '다람쥐', 6: '호랑이', 7: '원숭이',}
# dict = {0:'심해어',1:'강아지',2:'고양이',3:'곰',4:'공룡',5:'토끼'}
# dict = {0: '심해어', 1: '강아지', 2: '고양이', 3: '곰',
#         4: '공룡', 5: '토끼', 6: '여우', 7: '배경'}
dict = {0: '심해어', 1: '강아지', 2: '고양이', 3: '곰',
        4: '공룡', 5: '토끼', 6: '여우', 7: '배경', 8: '다람쥐'}


def predict(src):

    model = load_model('keras_model_final_2.h5')

    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    image = Image.open(src)
    size = (224, 224)

    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array

    prediction = model.predict(data)[0]
    print(prediction)

    index_max = prediction.argmax()
    percentage = prediction.max()

    print(dict[index_max], percentage)

    return (index_max, dict[index_max], percentage)

# for i in range(22) :
#     print(i)
#     predict(f'picture/{i}.jpg')


def return_src(index):
    if index == 0:
        a = rd.randrange(1, 4)

    elif index == 1:
        a = rd.randrange(1, 9)

    elif index == 2:
        a = rd.randrange(1, 11)

    elif index == 3:
        a = rd.randrange(1, 7)

    elif index == 4:
        a = rd.randrange(1, 4)

    elif index == 5:
        a = rd.randrange(1, 5)

    elif index == 6:
        a = rd.randrange(1, 4)

    elif index == 7:
        a = 1

    elif index == 8:
        a = rd.randrange(1, 6)

    return f'src/{index}/{a}.jpg'
