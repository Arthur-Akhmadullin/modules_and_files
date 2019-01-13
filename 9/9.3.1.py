import os
from PIL import Image, ImageDraw, ImageColor, ImageFont

def convert_image(path, type1, type2, txt1, txt2, fsize):
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == type1:
            try:
                im = Image.open(os.path.basename(file))
                im = im.convert("RGB")

                draw = ImageDraw.Draw(im)

                #Координаты прямоугольника и отрисовка
                x1 = im.size[0]/2 - im.size[0]/4
                x2 = im.size[0]/2 + im.size[0]/4
                y1 = im.size[1]/2 + im.size[1]/4
                y2 = im.size[1]/2 - im.size[1]/4
                draw.rectangle([x1,y1,x2,y2], fill=(255,255,255))

                #Координаты двух строк и размещение по центру
                font = ImageFont.truetype("times.ttf", fsize)

                #Не работает проверка размера шрифта
                '''
                if font.getsize(text1)[0] > im.size[0]:
                    while font.getsize(text1)[0] > im.size[0]:
                        fsize -= 1
                        font = ImageFont.truetype("times.ttf", fsize)                        
                else:
                    continue
                '''



                x_text1 = im.size[0]/2 - font.getsize(text1)[0]/2
                y_text1 = im.size[1]/2 - font.getsize(text1)[1]
                x_text2 = im.size[0]/2 - font.getsize(text2)[0]/2
                y_text2 = im.size[1]/2 + font.getsize(text2)[1]
                draw.multiline_text((x_text1, y_text1), txt1, (0,0,0), font=font)
                draw.multiline_text((x_text2, y_text2), txt2, (0,0,0), font=font)

                del draw

                im.save(os.path.splitext(file)[0] + type2)

            except Exception:
                print("По каким-то причинам конвертация невозможна")

path = "\Python2018\Модули, пакеты\9"
type1 = ".png"
type2 = ".jpg"
text1 = "Hello,"
text2 = "World!"
font_size = 240

convert_image(path, type1, type2, text1, text2, font_size)