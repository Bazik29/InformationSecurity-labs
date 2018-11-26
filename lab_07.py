# Цифровая подпись Эль Гамаля

import random


def lucaslemer(prime):
    S, k, M = 4, 1, 2**prime-1
    while k != (prime-1):
        S = ((S*S)-2) % M
        k += 1
    if S == 0:
        return True
    else:
        return False


def randomprime():
    while True:
        prime = random.randint(32, 64)
        if (2 in [prime, 2**prime % prime]):
            if lucaslemer(prime):
                break
    return 2**prime-1, random.randint(4,13)


# def gcd(a, b):
#     while a != b:
#         if a > b:
#             a = a - b
#         else:
#             b = b - a
#     return a


# def primitive_root(modulo):
#     required_set = set(num for num in range(
#         1, modulo) if gcd(num, modulo) == 1)
#     for g in range(1, modulo):
#         actual_set = set(pow(g, powers) %
#                          modulo for powers in range(1, modulo))
#         if required_set == actual_set:
#             return g


class User():
    def __init__(self, g, p):
        self.g = g
        self.p = p
        self.__secret_key = random.randint(2, p - 1)
        self.public_key = pow(g, self.__secret_key, p)

    def __hash(self, message):
        return sum([ord(i) for i in message]) % (p - 1)

    def gen_new_key(self):
        self.__secret_key = random.randint(2, p - 1)
        self.public_key = pow(g, self.__secret_key, p)

    def make_sing(self, message):
        k = random.randint(2, p - 2)
        r = pow(g, k, p)
        m = self.__hash(message)
        print("h_1", m)
        s = (m - self.__secret_key*r)/k % (p - 1)
        k = None
        return r, s

    def check_sign(self, public_key, message, sign):
        r, s = sign
        m = self.__hash(message)
        print("h_2", m)
        left = pow(public_key, r)*pow(r, s)
        right = pow(self.g, m, self.p)
        return left == right

if __name__ == "__main__":
    # g = randomprime()
    # p = primitive_root(g)
    g, p = randomprime() #991, 6
    print(g, p)

    Alice = User(g, p)
    Bob = User(g, p)

    mesg_A = "Hello World!!!!!!!!!!!!!!!!!!!!!!!!!"

    sign_A = Alice.make_sing(mesg_A)
    res_check = Bob.check_sign(Alice.public_key, mesg_A, sign_A)

    if res_check: 
        print("Это сообщение от Alice")
    else: 
        print("Это сообщение НЕ от Alice")

    mesg_B = "Hello World?"
    res_check = Bob.check_sign(Alice.public_key, mesg_B, sign_A)

    if res_check: 
        print("Это сообщение от Alice")
    else: 
        print("Это сообщение НЕ от Alice")
