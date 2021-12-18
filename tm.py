from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import random as rd
dict = {0: '강아지', 1: '고양이', 2: '심해어', 3: '개구리', 4: '부엉이', 5: '라쿤', 6: '타조'}
# dict = {0: '강아지', 1: '고양이', 2: '심해어', 3: '타조',
# 4: '다람쥐', 5: '호랑이', 6: '오랑우탄', 7: '나무늘보', 8: '말'}


def predict(src):

    model = load_model('keras_model.h5')

    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    image = Image.open(src)
    size = (224, 224)

    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array

    prediction = model.predict(data)
    prediction = prediction[0]
    index_max = prediction.argmax()
    percentage = prediction.max()

    print(dict[index_max], percentage)

    return (index_max, dict[index_max], percentage)


def return_src(index):
    if index == 0:
        a = rd.randrange(1, 8)

    elif index == 1:
        a = rd.randrange(1, 11)

    elif index == 2:
        a = rd.randrange(1, 3)
    else:
        a = 1
    return f'animal/{index}/{a}.jpg'
