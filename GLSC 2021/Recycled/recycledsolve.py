def rotr(byte, n):
    """Uses some bit magic to rotate a bit to the right by N rotations. Code is based off of the formula presented
    by Smitha Dinesh Semwal in a bit rotation example. """

    while n > 8:
        n -= 8  # This part of the code is just meant to make sure that the rotations are within the confine
    while n < 0:  # of 0 - 8, since the binary width of this operation is 8.
        n += 8

    return int(byte >> n | byte << (8 - n) & 0xFF)


def rotl(byte, n):
    """Same thing as the right rotation function, but to the left instead."""

    while n > 8:
        n -= 8
    while n < 0:
        n += 8

    return int(byte << n | byte >> (8 - n)) & 0xFF


counter = 0
output = b''
with open("encrypted.jpg", "rb") as f:
    f = f.read()
    with open("out.jpg", "wb") as g:
        for byte in f:
            output += bytes([rotl(byte, counter)])
            print(counter)
            if counter >= 7:
                counter = 0
            else:
                counter += 1

        g.write(output)
