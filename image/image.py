#!/usr/bin/python3
from PIL import Image as im
image = im.open('image/hath.jpeg')
image = image.convert('L') # convert the image into black-and-white mode
image.show()
