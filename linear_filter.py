import cv2
import numpy as np
import scipy.ndimage


# opening the image using cv2
a = cv2.imread('image2/11.jpg')
# converting the image to grayscale
a = cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)
