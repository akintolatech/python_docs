from PIL import Image
import os

# open image
pil_im = Image.open("us campo.jpg")
print(pil_im)

#convert to gray scale
# gray_scale = pil_im.convert("L")

#print size
# print("JPG[size]: {0}\nPNG[size]: {1}".format(os.path.getsize("us campo.jpg"), os.path.getsize("us campo.png")))

#save in another format
# gray_scale.save("us campo.jpg.jpg")

#creating thumbnails
# gray_scale.thumbnail((150, 150))
# gray_scale.save("thumbnail.jpg")

#resizing images
# resized_img = pil_im.resize((512, 512))
# resized_img.save("resized.jpg")
