from PIL import Image

img = Image.open()
img.show()

print(img.size)

cropped_img = img.crop((0,0,640,640))
cropped_img.show()