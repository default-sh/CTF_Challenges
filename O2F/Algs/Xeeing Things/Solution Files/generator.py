import random
from PIL import Image
import math


def color_alpha_out(byte1, byte2):
    if byte1 == "1":
        r, g, b = 255, 255, 255
    elif byte1 == "0":
        r, g, b = 0, 0, 0

    if byte2 == "1":
        a = 255
    elif byte2 == "0":
        a = 0

    return (r, g, b, a)


def is_square(i: int) -> bool:
    return i == math.isqrt(i) ** 2


with open("maze.png", "rb") as f:
    file = f.read()
    f.close()

binstr = []
for byte in file:
    binstr.append('{0:08b}'.format(byte))

image_binary = ''.join(binstr)

binstr = []
rand = random.Random()
for i in range(len(image_binary)):
    binstr.append(str(rand.randint(0, 1)))

random_binary = ''.join(binstr)

binstr = []
for i, j in zip(image_binary, random_binary):
    binstr.append(str(int(i) ^ int(j)))

encrypted_binary = ''.join(binstr)

temp = len(image_binary)
while not is_square(temp):
    temp += 1
    image_binary += "0"
    random_binary += "0"
    encrypted_binary += "0"

print(temp)

# ALPHA = Random
# COLOR = Encrypted
img = Image.new('RGBA', size=(int(math.sqrt(temp)), int(math.sqrt(temp))), color="black")

counter = 0
for i in range(0, img.height):
    for j in range(0, img.width):
        b1 = random_binary[counter]
        b2 = encrypted_binary[counter]

        img.putpixel((j, i), (color_alpha_out(b1, b2)))
        counter += 1

img.show()
img.save("wow.png")