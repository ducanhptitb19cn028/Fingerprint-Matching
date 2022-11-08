# load_model_sample.py
from keras.models import load_model
from keras.preprocessing import image
from keras.utils import load_img, img_to_array
import matplotlib.pyplot as plt
import numpy as np
import os


def load_image(img_path, show=False):

    img = load_img(img_path, target_size=(100, 100))
    img_tensor = img_to_array(img)                    # (height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    img_tensor /= 255.                                      # imshow expects values in the range [0, 1]

    if show:
        plt.imshow(img_tensor[0])                           
        plt.axis('off')
        plt.show()

    return img_tensor


if __name__ == "__main__":

    classLabels = []
    path = 'data/train'
    for _, dirnames, filenames in os.walk(path):
        classLabels=dirnames
        break
    
    # load model
    model = load_model("model_cv.h5")

    # image path
    img_path = 'test.png'    # dog
    #img_path = '/media/data/dogscats/test1/19.jpg'      # cat

    # load a single image
    new_image = load_image(img_path)

    # check prediction
    pred = model.predict(new_image)
    pos = np.argmax(pred, axis = 1)
    print(classLabels[int(pos)])