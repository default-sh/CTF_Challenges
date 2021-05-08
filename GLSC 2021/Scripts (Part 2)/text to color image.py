from PIL import Image
from math import sqrt
import random

with open("script.txt", "r") as f:
    f = f.read().replace("\n", " ").replace("- ", "")

    nums = [ord(char) for char in f]

    binary = []
    for num in nums:
        num = bin(num)[2:]
        while len(num) < 8:
            num = "0" + num
        binary.append(num)

        number = ''.join(binary)

    while not int(sqrt(len(number)) + 0.5) ** 2 == len(number):
        number = number + random.choice(["1", "0"])

    img_size = int(sqrt(len(number) / 4))

    img = Image.new(mode="RGBA", size=(img_size, img_size))
    pix = img.load()

    counter = 0
    for height in range(0, img_size):
        for width in range(0, img_size):
            b1 = number[counter]
            b2 = number[counter + 1]
            b3 = number[counter + 2]
            b4 = number[counter + 3]

            pixel = [0, 0, 0, 0]
            for i, b in enumerate([b1, b2, b3, b4]):
                if b == "0":
                    pixel[i] = random.randint(0, 127)
                else:
                    pixel[i] = random.randint(128, 256)
            counter += 4

            pix[width, height] = (pixel[0], pixel[1], pixel[2], pixel[3])

    img.save("colorgrid.png")