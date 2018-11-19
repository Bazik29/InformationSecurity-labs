import socket
import random


def protS(*arg):
    return (':'.join(list(map(str, arg)))).encode('utf-8')


class Client():
    def __init__(self):
        # Открытые параметры
        self.p = 0
        self.g = 0
        # Закрытый ключ
        self.privateKey = random.randint(10*10, 10**100)
        # Секретный ключ
        self.secretKey = 0
        # Вычисляемый секретный ключ
        self.secretTemp = 0

    def getPublicKey(self):
        return pow(self.g, self.privateKey, self.p)

    def getSecretTemp(self):
        return self.secretTemp

    def setSecret(self, R, last=False):
        self.secretTemp = pow(R, self.privateKey, self.p)
        if last:
            self.secretKey = self.secretTemp

    def processMsg(self, msg):
        flag = msg.pop(0)

        if flag == '':
            return
        if flag == "pg":
            p = int(msg.pop(0))
            g = int(msg.pop(0))
            self.p = p
            self.g = g
            print(f"p = {p}\ng = {g}")
        elif flag == "getPublic":
            sock.send(str(self.getPublicKey()).encode('utf-8'))
        elif flag == "getSecretTemp":
            sock.send(str(self.getSecretTemp()).encode('utf-8'))
        elif flag == "setLast":
            client.setSecret(int(msg.pop(0)), True)
            print(f"Secret key: {self.secretKey}")
        elif flag == "setTemp":
            client.setSecret(int(msg.pop(0)), False)
        else:
            print("Command \"{msg}\" is invalid")

        if msg:
            print("recurs: ", msg)
            self.processMsg(msg)


if __name__ == "__main__":
    sock = socket.socket()
    sock.connect(('localhost', 9090))

    client = Client()

    while True:
        data = sock.recv(2048).decode('utf-8')
        client.processMsg(data.split(':'))

    sock.close()
