from PIL import Image

im = Image.open('grid.png')  # Can be many different formats.
pix = im.load()


pixels = ""
for i in range(0, im.size[0]):
    for j in range(0, im.size[1]):
        pixel = pix[j, i]

        if pixel == (0, 0, 0, 255) or pixel == (0, 0, 0):
            pixels += "0"
        elif pixel == (255, 255, 255, 255) or pixel == (255, 255, 255):
            pixels += "1"

print(pixels)

