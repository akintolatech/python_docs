# %matplotlib inline
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread("us campo.jpg")
print(img)

#plotting images
# img_plot = plt.imshow(img)

#applying pseudo colors
lum_img = img[:, :, 0]
# plt.imshow(img)

# plt.imshow(lum_img, cmap="hot")
plt.imshow(lum_img, cmap="nipy_spectral")


plt.show()