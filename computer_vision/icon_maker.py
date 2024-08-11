"""
Source: Computer Vision
Desc: Basic Image Manipulation
All rights reserved Akintola Technologies  - updt Aug 24
"""

from PIL import Image

# open image
icon = Image.open("shop-icon.jpg")
# print(icon)

#save in another format
icon.save("shop-icon.ico")