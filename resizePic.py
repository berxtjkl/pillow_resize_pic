from PIL import Image
originPicName = 'akashi'
img = Image.open('./'+originPicName+'.jpg')  # image extension *.png,*.jpg
tempList = ["100,100", "200,200", "300,300", "400,400", "500,500", "600,600", "700,700",
            "800,800", "900,900", "1000,1000", "1100,1100", "1200,1200", "1300,1300", "1400,1400", "1500,1500"]
tempList1 = "100"
def resize(img):
    for i in tempList:
        temp = i.split(',')
        print(temp[0])
        new_width = temp[0]
        print(temp[1])
        new_height = temp[1]
        img = img.resize((int(new_width), int(new_height)), Image.ANTIALIAS)
        img.save('./sets/originPicName-resize-'+new_width+"-"+new_height +
                ".jpg", quality=95)  # format may what u want ,*.png,*jpg,*.gif

def crop(img):
    img.show()
    # 传入参数分别是左上的坐标和右下的坐标
    img = img.crop((0,0,500,500))
    
    img.save('./sets/originPicName-crop.jpg')


crop(img)

img.close()