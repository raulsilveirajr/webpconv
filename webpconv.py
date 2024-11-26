import sys

from PIL import Image

file = sys.argv[1]
print(file)


# convert webp file to jpg
def webp_to_jpg(file):
    im = Image.open(file)
    im.save(file.replace(".webp", ".jpg"), "jpeg")


webp_to_jpg(file)
