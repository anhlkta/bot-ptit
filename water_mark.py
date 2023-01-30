from PIL import Image

anh = Image.open("/Users/shone/Desktop/anh_test.jpeg")
water_mark = Image.open("/Users/shone/Desktop/logo.png")

size = (250, 250) #(x,y) logo
water_mark.thumbnail(size)
print(anh.size)
#size ảnh (e, f)
# vị trí (a, b)
# b để nguyên
# a = e - x - 10
anh.paste(water_mark, (2048-250-10,10), water_mark) 
anh.save("/Users/shone/Desktop/new_image.jpg")
