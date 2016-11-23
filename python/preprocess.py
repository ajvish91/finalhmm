import cv2
import numpy as np
import math


# Binarizes the image
def binarize(img):
    blur = cv2.GaussianBlur(img, (5, 5), 0)
    ret, binarized_img = cv2.threshold(
        blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return binarized_img


# Removes salt and pepper noise
def removeSaltnPepperNoise(img):
    return cv2.medianBlur(img, 5)


# Detects the edge of the structuring element
def detectEdge(img):
    horizontalStructure = cv2.getStructuringElement(
        cv2.MORPH_RECT, (3, 3))

    cv2.erode(img, img, horizontalStructure, (-1, -1))
    cv2.dilate(img, img, horizontalStructure, (-1, -1))
    return img


# Histogram equalizes the image
def equalize(img):
    return cv2.equalizeHist(img)


# Thins the lines of the image
def thinLines(img):
    return cv2.erode(img, np.ones((3, 3), np.uint8), iterations=3)


# Sharpens the image
def sharpen(img):
    frame = cv2.GaussianBlur(img, (5, 5), 3)
    img = cv2.addWeighted(img, 1.5, frame, -0.5, 0, frame)
    return frame


# Resizes the image
def resizeImage(img):
    return cv2.resize(img, (75 * img.shape[1] / img.shape[0], 75))


# Sample the image
def samplePage(img):
    page_width = img.shape[1]
    page_offset = 700
    page_height = img.shape[0] - page_offset
    page = img[page_offset: page_height - 100, 100:]
    print "Image has been sampled at ", page.shape[1], "x", page_width
    return page


# Detect skew
def detectSkew(img):
    not_img = cv2.bitwise_not(img)
    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(not_img, kernel, iterations=1)
    points_row, points_column = np.where(erosion == 255)
    points = zip(points_column, points_row)
    rect = cv2.minAreaRect(np.asarray(points))
    print rect
    box = cv2.cv.BoxPoints(rect)
    box = np.int0(box)
    print box
    cv2.drawContours(erosion, [box], 0, 125, 2)
    cv2.namedWindow("lined out", cv2.WINDOW_NORMAL)
    cv2.imwrite("lined_out.jpg", erosion)
    return img
