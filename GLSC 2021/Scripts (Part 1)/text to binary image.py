from PIL import Image
from math import sqrt
import random

with open("script.txt", "r") as f:
    f = f.read().replace("\n", " ")

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

    img_size = int(sqrt(len(number)))

    img = Image.new(mode="RGB", size=(img_size, img_size))
    pix = img.load()

    counter = 0
    black = (0, 0, 0)
    white = (255, 255, 255)
    for height in range(0, img_size):
        for width in range(0, img_size):
            if number[counter] == "0":
                pix[width, height] = black
            else:
                pix[width, height] = white
            counter += 1

    img.save("grid.png")

