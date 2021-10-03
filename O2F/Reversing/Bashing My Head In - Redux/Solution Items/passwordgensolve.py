import time
import sys


class Random:
    def __init__(self, seed=None):
        if seed is None:
            self.seed = round(int(time.time() * (10 ** 5)))
            with open("seed", "w") as f:
                f.write(str(self.seed))
        else:
            try:
                self.seed = int(seed)
            except ValueError:
                raise ValueError("Please use a valid integer for the seed.")
        self.next_seed = 0

    def __generatePercentage(self):
        a = 1664525
        c = 1013904223
        m = 2 ** 32

        if self.next_seed == 0:
            next_seed = (self.seed * a + c) % m
        else:
            next_seed = (self.next_seed * a + c) % m
        self.next_seed = next_seed
        randomPercentage = next_seed / m

        return randomPercentage

    def choice(self, index):
        randomIndex = round((self.__generatePercentage() * (len(index) - 1)))
        randomChoice = index[randomIndex]

        return randomChoice


alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890?!@#$%^&*()"

with open("passlist.txt", "w") as f:

    for k in range(163252292000000, 163252292100000):
            rand = Random(seed=k)
            f.write(''.join([rand.choice(alphabet) for i in range(16)]) + "\n")
