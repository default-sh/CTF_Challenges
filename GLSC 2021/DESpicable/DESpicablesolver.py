from Crypto.Cipher import DES
from datetime import datetime

cipher = DES.new(key=b"\x0d\x0e\x0a\x0d\x42\x42\xfe\xcc", mode=DES.MODE_CBC, iv=b"\x48\xe4\x5f\xaa\xa9\x0f\x12\xb3")

test = cipher.encrypt(b"GLSC{d0nt_5pi11_ur_k3yz}")

with open("desmessage.txt", "wb") as f:
    f.write(test)

with open("desmessage.txt", "rb") as g:
    with open('output.txt', "wb") as gg:
        start_time = datetime.today().timestamp()
        init = b"\x0d\x0e\x0a\x0d"
        ciphertext = g.read()
        for a in range(0, 255):
            for b in range(0, 255):
                for c in range(0, 255):
                    for d in range(0, 255):

                        new_cipher = DES.new(key=init + bytes([a]) + bytes([b]) + bytes([c]) + bytes([d]),
                                             mode=DES.MODE_CBC, iv=b"\x48\xe4\x5f\xaa\xa9\x0f\x12\xb3")
                        plaintext = new_cipher.decrypt(ciphertext)
                        if plaintext.__contains__(b"GLSC"):
                            print(init + bytes([a]) + bytes([b]) + bytes([c]) + bytes([d]))
                            print((datetime.today().timestamp()) - start_time)
                            print(plaintext)
                            exit(1)
