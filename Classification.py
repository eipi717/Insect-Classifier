# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import keras
from PIL import Image

model = keras.models.load_model("../Model/Xception.h5")

labels = [
          'Ant',
          'Bee',
          'Butterfly',
          'Cockroaches',
          'Dragonfly',
          'Fly',
          'Grasshopper',
          'Ladybird',
          'Mosquito',
          'Scorpions',
          'Spiders',
          'Wasp'
          ]

def Classifier(imgpath):
    fileImage = Image.open(imgpath).convert("RGB").resize([224, 224],Image.ANTIALIAS)
    image = np.array(fileImage)
    my_image = image.reshape(1, 224, 224, 3)
    my_image = my_image/255.

    pred_label = np.argmax(model.predict(my_image), axis=1)
    output = ["It is a " + str(labels[int(pred_label)]), int(pred_label)]
    plt.imshow(image)
    return output
