import time
import os
import sys


class Random:
    def __init__(self, seed=None):
        if seed is None:
            self.seed = int(time.time() * (10 ** 7))
        else:
            try:
                self.seed = int(seed)
            except ValueError:
                raise ValueError("Please use a valid integer for the seed.")
        self.next_seed = 0

    def __generate_percentage(self):
        a = 5320987168123165987435198746541196719161631970
        c = 981956519787432168745465494985698465191912969
        m = 102136854831294946518746541654987324197497117

        if self.next_seed == 0:
            next_seed = (self.seed * a + c) % m
        else:
            next_seed = (self.next_seed * a + c) % m
        self.next_seed = next_seed
        randomPercentage = float(str(f"0.{str(next_seed)[4:]}"))

        return randomPercentage

    def choice(self, index):
        randomIndex = round((self.__generate_percentage() * (len(index) - 1)))
        randomChoice = index[randomIndex]

        return randomChoice


alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890?!@#$%^&*()"
for i in range(0, 99999):
    rand = Random(i)
    password = ''.join([rand.choice(alphabet) for i in range(32)])
    print(password)