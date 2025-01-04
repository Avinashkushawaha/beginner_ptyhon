import PIL
from PIL import Image
import PIL.Image

img = PIL.Image.open("C:/Users/DELL/Downloads/IMG_20200701_113013.jpg")
width, height = img.size

print (width,"x ", height)