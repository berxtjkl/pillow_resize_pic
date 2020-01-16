from PIL import Image
originPicName = 'akashi'
img = Image.open('./'+originPicName+'.jpg')  # image extension *.png,*.jpg
tempList = ["100,100", "200,200", "300,300", "400,400", "500,500", "600,600", "700,700",
            "800,800", "900,900", "1000,1000", "1100,1100", "1200,1200", "1300,1300", "1400,1400", "1500,1500"]
tempList1 = ["100,100", "200,200", "300,300", "400,400", "500,500", "600,600", "700,700",
            "800,800", "900,900", "1000,1000", "1100,1100", "1200,1200", "1300,1300", "1400,1400", "1500,1500"]
for i in tempList:
    temp = i.split(',')
    print(temp[0])
    new_width = temp[0]
    print(temp[1])
    new_height = temp[1]
    img = img.resize((int(new_width), int(new_height)), Image.ANTIALIAS)
    img.save('./sets/originPicName-'+new_width+"-"+new_height +
             ".jpg")  # format may what u want ,*.png,*jpg,*.gif
img.close()
