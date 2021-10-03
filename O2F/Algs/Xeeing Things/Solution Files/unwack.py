from PIL import Image


# ALPHA = Random
# COLOR = Encrypted
img = Image.open("wow.png")

def unxor(pixel):
    r, g, b, a = pixel
    if r == 255 & g == 255 & b == 255:
        b1 = 1
    elif r == 0 & g == 0 & b == 0:
        b1 = 0

    if a == 255:
        b2 = 1
    elif a == 0:
        b2 = 0

    return b1 ^ b2

binstr = []
counter = 0
for i in range(0, img.height):
    for j in range(0, img.width):
        pxl = img.getpixel((j, i))
        binstr.append(str(unxor(pxl)))

binstr = ''.join(binstr)

test = [binstr[i: i+8] for i in (range(0, len(binstr), 8))]

test2 = b""
for bins in test:
    test2 += int(bins, 2).to_bytes(length=1, byteorder="big")

with open("orig.png", "wb") as f:
    f.write(test2)
