from PIL import Image, ImageDraw, ImageFont
import random

def waterprint(infile,text,quality=100):
    img = Image.open(infile)
    # 字体
    font = ImageFont.truetype("/Library/Fonts/Arial Unicode.ttf", 40)
    # 将图片转为图层
    layer = img.convert("RGBA")
    # 生成对应图片
    text_layer = Image.new("RGBA", (img.size[0]*2,img.size[1]*2), (255, 255, 255, 0))
    Image_draw = ImageDraw.Draw(text_layer) #画图
    # 获取文本大小
    textsize_x, textsize_y = Image_draw.textsize(text, font=font)
    nums = max(layer.size[0] // textsize_x, layer.size[1] // textsize_y)
    for i in range (1,nums):
        for j in range(1,nums):
            # 设置文本文字位置
            text_xy = (textsize_x*(i-1)*1.5+random.random()*200,textsize_y*(j-1)*2.5+random.random()*30)
            # 设置文本颜色和透明度位置
            Image_draw.text(text_xy, text, font=font, fill=(25, 25, 25, 80))
    # 将新图层旋转45度后裁剪和图片一样大，新图层必须和图片一样大，否则无法合并
    text_layer = text_layer.rotate(45)
    text_layer = text_layer.crop((text_layer.size[0]/2 - img.size[0]/2, 
                                text_layer.size[1]/2 - img.size[1]/2, 
                                text_layer.size[0]/2 + img.size[0]/2, 
                                text_layer.size[1]/2 + img.size[1]/2))
    # 合并图层
    after = Image.alpha_composite(layer, text_layer)
    x, y = after.size
    after = after.resize((x//3, y//3), Image.ANTIALIAS)
    outfile = infile.split('.')[0] + '_wp.png'
    after.save(outfile,quality=quality)


infile = "/Users/apple/Downloads/IMG.jpg"
text = "xxxxoooo使用"
waterprint(infile,text,50)
