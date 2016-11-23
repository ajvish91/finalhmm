import os
import xml.etree.ElementTree as ET
from PIL import Image, ImageFilter
import numpy as np


def imagePreprocessing(imageFile):
    # Convert to binary image
    im = Image.open(imageFile).convert('1')
    # resize image based on the longest dimension, and then pasting it on a
    # white canvas
    imageval = np.array(im)
    width = float(im.size[0])
    height = float(im.size[1])
    newImage = Image.new('1', (78, 78), (255))
    if width > height:
        nheight = int(round((70.0 / width * height), 0))
        if (nheight == 0):
            nheight = 1
        # sharpen image
        img = im.resize((70, nheight), Image.ANTIALIAS).filter(
            ImageFilter.SHARPEN)
        wtop = int(round(((78 - nheight) / 2), 0))
        newImage.paste(img, (4, wtop))
    else:
        nwidth = int(round((70.0 / height * width), 0))
        if (nwidth == 0):
            nwidth = 1
        img = im.resize((nwidth, 70), Image.ANTIALIAS).filter(
            ImageFilter.SHARPEN)
        wleft = int(round(((78 - nwidth) / 2), 0))
        newImage.paste(img, (wleft, 4))
    tv = list(newImage.getdata())
    tva = [(255 - x) * 1 / 255 for x in tv]
    return tva

# create csv file with sequence (flattened image array) and the
# corresponding label


def imagePreprocessingForAllFiles():
    words_mapping = []
    with open("words.txt") as fp:
        for i, line in enumerate(fp):
            words_mapping.append(line)
    labels = []
    for label in words_mapping:
        label_split = label.rstrip("\n").split(" ")
        if label_split[0] != "a01-117-05-02" and label_split[0] != "r06-022-03-05":
            mylabel = [label_split[0], label_split[-1]]
            labels.append(mylabel)
            print(mylabel)
    directory = "./words"
    directorylist = [x[0] for x in os.walk(directory)]
    directories = []
    for subdir in directorylist:
        directories = directories + [x[0] for x in os.walk(subdir)]
    print(directories)
    target = open('main_sequence.csv', "w")
    for path in directorylist:
        for file in os.listdir(path):
            if file.endswith(".png"):
                word = imagePreprocessing(path + "/" + file)
                for w in word:
                    target.write(str(w) + ",")
                key = str(file)
                for label in labels:
                    print(label)
                    if(label[0] == key):
                        target.write(label[1])
                        break

                target.write(key)
                target.write("\n")
    target.close()


imagePreprocessingForAllFiles()
