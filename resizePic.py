from PIL import Image
originPicName = 'akashi'
img = Image.open('./'+originPicName+'.jpg')  # image extension *.png,*.jpg
tempList = ["100,100", "200,200", "300,300", "400,400", "500,500", "600,600", "700,700",
            "800,800", "900,900", "1000,1000", "1100,1100", "1200,1200", "1300,1300", "1400,1400", "1500,1500"]
tempList1 = ["200,100", "300,200", "400,300", "500,400", "600,500", "700,600", "800,700",
            "900,800", "1000,900"]
for i in tempList1:
    temp = i.split(',')
    print(temp[0])
    new_width = temp[0]
    print(temp[1])
    new_height = temp[1]
    img = img.resize((int(new_width), int(new_height)), Image.ANTIALIAS)
    image_fullsize.save('./sets/originPicName-'+new_width+"-"+new_height +
             ".jpg", quality=95)  # format may what u want ,*.png,*jpg,*.gif
img.close()
