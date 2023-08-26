import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np

#選擇圖片
back_img = cv2.imread("./A3-1.png")

#設置字體路徑
fontpath = "font/setofont.ttf"

#設置名字文件路徑
namefilepath = "input.txt"


def TextOnOneImg(name1, name2, num):

    img_pil = Image.fromarray(back_img)
    draw = ImageDraw.Draw(img_pil)
    #cv2.putText(back_img,"1234",(350,2200),cv2.FONT_HERSHEY_COMPLEX,35,(255,255,255),10,cv2.LINE_AA)
    # name1 = "阿佩"
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

    # name2 = "大笨蛋"
    #= input("輸入隊員名字2:")
    len2 = len(name2)
    if (len2 == 1):
        font = ImageFont.truetype(fontpath, 1150)
        draw.text((1150, 2480+1100),  name2, font = font, fill = (255, 255, 255))
    else:
        font = ImageFont.truetype(fontpath, int(1150*2/len2))
        draw.text((550, 2480+1100+int(1150*(len2-2)/(2*len2))),  name2, font = font, fill = (255, 255, 255))

    
    result_img = np.array(img_pil)
    # x,y = back_img.shape[0:2]
    # preshowimg = cv2.resize(result_img,(int(y/5),int(x/5)))
    # cv2.imshow("preshowimg",preshowimg)
    # cv2.waitKey()
    cv2.imwrite("output/{}.jpg".format(str(num)),result_img)

def TextOnAllImg(all_lines):
    length = len(all_lines)
    if(length/2.0 != 0):
        length = length + 1
        all_lines.append(" ")
    
    for i in range( int(length / 2)):
        TextOnOneImg(all_lines[i*2].rstrip('\n') , all_lines[i*2+1].rstrip('\n') , i)

    print("成功!請查看output資料夾")

def ReadNameFormTxt():
    with open(namefilepath,'r', encoding="utf-8") as fp:
        all_lines = fp.readlines()
    return all_lines

if __name__ == '__main__':
    TextOnAllImg(ReadNameFormTxt())