from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

dict = {0: '고양이', 1: '강아지', 2: '심해어'}


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
