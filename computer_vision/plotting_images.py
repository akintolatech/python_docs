from PIL import Image
import matplotlib.pyplot as plot
import array

#read image to array
img_arr = array(Image.open("us campo.jpg"))

# plot the image
img_arr.show(img_arr)

# some points
x = [100, 100, 400, 400]
y = [200, 500, 200, 500]

# plot x and y with red stars
plot(x, y, 'r*')

#add title
plot.title("plotting Images")

plot.show()