#encoding:UTF-8
#ref:https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_canny/py_canny.html?highlight=canny
import cv2
import numpy as np
from matplotlib import pyplot as plt

#切记路径中斜杠是/
img = cv2.imread('../PIL/Lenna_(test_image).png',0)

#First argument is our input image. Second and third arguments are our minVal and maxVal respectively. Third argument is aperture_size. It is the size of Sobel kernel used for find image gradients. By default it is 3. Last argument is L2gradient which specifies the equation for finding gradient magnitude.
edges = cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap=plt.get_cmap('gray'), vmin=0, vmax=255)
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap=plt.get_cmap('gray'), vmin=0, vmax=255)
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
