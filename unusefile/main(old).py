import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np

#img_name = input("輸入文件")
#選擇圖片
back_img = cv2.imread("./A3-1.png")
#圖片大小賦值給x,y
x,y = back_img.shape[0:2]

#設置字體路徑
fontpath = "font/setofont.ttf"
img_pil = Image.fromarray(back_img)
draw = ImageDraw.Draw(img_pil)

#上字
#cv2.putText(back_img,"1234",(350,2200),cv2.FONT_HERSHEY_COMPLEX,35,(255,255,255),10,cv2.LINE_AA)
name1 = "阿佩"
#= input("輸入隊員名字1:")
len1 = len(name1)
if (len1 == 1):
    font = ImageFont.truetype(fontpath, 1150)
    draw.text((1150, 2480+1100),  name1, font = font, fill = (255, 255, 255))
else:
    font = ImageFont.truetype(fontpath, int(1150*2/len1))
    draw.text((580, 1100+int(1150*(len1-2)/(2*len1))),  name1, font = font, fill = (255, 255, 255))
# if len(name1) == 2:
#     font = ImageFont.truetype(fontpath, 1150)
#     draw.text((550, 1100),  name1, font = font, fill = (255, 255, 255))
# elif len(name1) == 3:
#     font = ImageFont.truetype(fontpath, int(1150*2/3))
#     draw.text((550, 1100+int(1150*1/6)),  name1, font = font, fill = (255, 255, 255))

name2 = "大笨蛋"
#= input("輸入隊員名字2:")
len2 = len(name2)
if (len2 == 1):
    font = ImageFont.truetype(fontpath, 1150)
    draw.text((1150, 2480+1100),  name2, font = font, fill = (255, 255, 255))
else:
    font = ImageFont.truetype(fontpath, int(1150*2/len2))
    draw.text((550, 2480+1100+int(1150*(len2-2)/(2*len2))),  name2, font = font, fill = (255, 255, 255))


back_img = np.array(img_pil)

preshowimg = cv2.resize(back_img,(int(y/5),int(x/5)))
cv2.imshow("preshowimg",preshowimg)

cv2.waitKey()
cv2.imwrite("add_text.jpg",back_img)