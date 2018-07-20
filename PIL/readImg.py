#coding:UTF-8
from PIL import ImageColor
from PIL import Image
from PIL import ImageFilter
####################################
#RGBA of red and block color
#RGBA
print(ImageColor.getcolor('red','RGBA'))
#RGB
print(ImageColor.getcolor('black','RGB'))

####################################
#read imgage
path=r'Lenna_(test_image).png'
im = Image.open(path)
width,height = im.size
#宽,高
print(im.size,width,height)
#格式，以及格式的详细描述
print(im.format,im.format_description)
im.save(r'Lenna_(test_image)_copy.png')
im.show()

####################################
#new image
#RGB模式
redIm = Image.new('RGB',(100,100),'red')
redIm.save(r'1.png')
#RGBA模式
redIm = Image.new('RGBA',(100,100),'black')
redIm.save(r'2.png')
#十六进制颜色
redIm = Image.new('RGBA',(100,100),'#FF0000')
redIm.save('3.png')
#元组形式
redIm = Image.new('RGB',(200,100),(255,2555,0,0))
redIm.save(r'4.png')

####################################
#crop imge
im = Image.open(r'Lenna_(test_image)_copy.png')
cropedIm = im.crop((0,0,100,100))
cropedIm.save(r'5.png')

####################################
#复制图片产生新图
im = Image.open(r'Lenna_(test_image)_copy.png')
cropedIm = im.crop((0,0,100,100))
copyIm = im.copy()
copyIm.paste(cropedIm,(0,0))
copyIm.show()
copyIm.save(r'6.png')

####################################
#resize
im = Image.open(r'Lenna_(test_image)_copy.png')
width,height = im.size
resizedIm = im.resize((width,height+(1920-1080)))
resizedIm.save(r'7.png')

####################################
#rotate
im = Image.open(r'Lenna_(test_image)_copy.png')
im.rotate(90).save(r'8.png')
im.rotate(270).save(r'9.png')

####################################
#图像过滤
im = Image.open(r'Lenna_(test_image)_copy.png')
#高斯模糊
im.filter(ImageFilter.GaussianBlur).save(r'GaussianBlur.png')
#普通模糊
im.filter(ImageFilter.BLUR).save(r'BLUR.png')
#边缘增强
im.filter(ImageFilter.EDGE_ENHANCE).save(r'EDGE_ENHANCE.png')
#边缘
im.filter(ImageFilter.FIND_EDGES).save(r'FIND_EDGES.png')
#浮雕
im.filter(ImageFilter.EMBOSS).save(r'EMBOSS.png')
#轮廓
im.filter(ImageFilter.CONTOUR).save(r'CONTOUR.png')
#锐化
im.filter(ImageFilter.SHARPEN).save(r'SHARPEN.png')
#平滑
im.filter(ImageFilter.SMOOTH).save(r'SMOOTH.png')
#细节
im.filter(ImageFilter.DETAIL).save(r'DETAIL.png')






