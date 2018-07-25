#encoding:UTF-8
import cv2 
import numpy as np
#读图片
image = cv2.imread('../PIL/Lenna_(test_image).png',cv2.IMREAD_COLOR)#or cv.LoadImage('../Lenna_(test_image).png')
#cv2.namedWindow('a_window',cv2.WINDOW_AUTOSIZE)#facultative
#cv2.imshow('a_window',image)#show the image
grayImage = cv2.imread('../PIL/Lenna_(test_image).png', cv2.IMREAD_GRAYSCALE)
#cv2.imshow('a_window',grayImage)#show the gray image
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#读取图片信息
print(image.shape)
print(image.size)
print(image.dtype)

#往图片添加文字信息
font = cv2.FONT_HERSHEY_SIMPLEX #Creates a font
y = image.shape[1]/ 2# y position of the text
x = image.shape[0]/ 4# x position of the text
cv2.putText(image,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)
cv2.imshow('Hello World', image) #Show the image
cv2.waitKey(0)

#缩放
#thumb = np.zeros(int(image.shape[0]/2),int(image.shape[1]/2), np.uint8)  
height,width=image.shape[:2]
thumb = cv2.resize(image,((int)(height/2),(int)(width/2)),interpolation=cv2.INTER_CUBIC)
cv2.imwrite("thumb.png", thumb) # save the thumb image

