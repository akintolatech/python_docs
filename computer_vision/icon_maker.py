from PIL import Image

# open image
icon = Image.open("shop-icon.jpg")
# print(icon)

#save in another format
icon.save("shop-icon.ico")