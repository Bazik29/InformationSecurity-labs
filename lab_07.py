# Цифровая подпись Эль Гамаля

import random
from math import gcd


def lucas_lemer(prime):
    S, k, M = 4, 1, 2**prime-1
    while k != (prime-1):
        S = ((S*S)-2) % M
        k += 1
    if S == 0:
        return True
    else:
        return False


def random_prime():
    while True:
        prime = random.randint(64, 256)
        if 2 in [prime, 2**prime % prime]:
            if lucas_lemer(prime):
                break
    return 2**prime-1


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        raise Exception("Error")
    else:
        return x % m


def random_k_invk(p):
    k = random.randint(2, p-2)
    if gcd(k, p-1) != 1:
        return random_k_invk(p)
    else:
        return k, modinv(k, p-1)


class User():
    def __init__(self, g, p):
        self.g = g
        self.p = p
        self.__secret_key = random.randint(2, p - 1)
        self.public_key = pow(g, self.__secret_key, p)

    def __hash(self, message):
        h = sum([ord(i) for i in message]) % (p - 2)
        if h == 1:
            h += 1
        return h

    def gen_new_key(self):
        self.__secret_key = random.randint(2, p - 1)
        self.public_key = pow(g, self.__secret_key, p)

    def make_sing(self, message):
        k, k_inv = random_k_invk(self.p)
        # k_inv = modinv(k, p-1)
        r = pow(g, k, p)
        m = self.__hash(message)
        s = (m - self.__secret_key*r) * k_inv % (p - 1)
        # print(f"K: {k} iK: {k_inv} m: {m} r: {r} s: {s} sign({r},{s})\n")
        k = None
        return r, s

    def check_sign(self, publicKey, message, sign):
        r, s = sign
        m = self.__hash(message)
        print("hash", m)
        # print("yrp", publicKey, r, self.p)
        # print("rsp", r, s, self.p)
        left = pow(publicKey, r, self.p)*pow(r, s, self.p) % self.p
        right = pow(self.g, m, self.p)
        # print("left:", left, "right:",  right)
        return left == right


if __name__ == "__main__":
    # g = random_prime()
    # p = random.randint(4, 13)
    g, p = 618970019642690137449562111, 11
    # print(g, p)

    Alice = User(g, p)
    Bob = User(g, p)

    mesg_A = "Hello World!!!"

    sign_A = Alice.make_sing(mesg_A)
    res_check = Bob.check_sign(Alice.public_key, mesg_A, sign_A)

    if res_check:
        print("Это сообщение от Alice")
    else:
        print("Это сообщение НЕ от Alice")

    mesg_B = "Hello World!!?qw"
    res_check = Bob.check_sign(Alice.public_key, mesg_B, sign_A)

    if res_check:
        print("Это сообщение от Alice")
    else:
        print("Это сообщение НЕ от Alice")
