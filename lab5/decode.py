import os
import socket


def xor(message, key):

    message = bytes.fromhex(message)
    key = key.encode()

    xor_key = (key * (len(message) // len(key) + 1))[:len(message)]

    result = bytes([a ^ b for a, b in zip(message, xor_key)])

    return result.decode()


def main():
    m1 = "1a117a"
    m2 = "10140445152d4355175c110c2b61"
    m3 = "1616180a527d150902151e176f05020b1201033a43392c1c53073a196b0f562642012f1143331f3a0b41174700080d4d1e050d47522353120b1d04193661"
    KEY = "super_secret_key"
    payload1 = xor(m1, KEY)
    p2 = xor(m2, KEY)
    p3 = xor(m3, KEY)
    print(payload1)
    print(p2)
    print(p3)



if __name__ == "__main__":
    main()