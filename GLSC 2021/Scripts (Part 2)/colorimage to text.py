from PIL import Image

im = Image.open('colorgrid.png')
pix = im.load()

pixels = ""
for i in range(0, im.size[0]):
    for j in range(0, im.size[1]):
        rgba = pix[j, i]

        for pixel in rgba:
            if pixel < 128:
                pixels += "0"
            else:
                pixels += "1"

print(pixels)
