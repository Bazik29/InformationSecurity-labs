import socket
import random
import sys


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
        prime = random.randint(32, 1024)
        if (2 in [prime, 2**prime % prime]):
            if lucaslemer(prime):
                break
    return (2**prime-1, random.randint(3, 13))


def protS(*arg):
    return (':'.join(list(map(str, arg))) + ':').encode('utf-8')


if __name__ == "__main__":

    n_cl = 2
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        n_cl = int(sys.argv[1])

    sock = socket.socket()
    sock.bind(('', 9090))
    sock.listen(n_cl)

    Clients = []

    p, g = randomprime()
    # p, g = 23, 5

    # Ожидание подключения всех клиентов
    while len(Clients) < n_cl:
        conn, addr = sock.accept()
        Clients.append(conn)
        print(f"Connected: {addr}, {len(Clients)}/{n_cl}")

    # Отправка всем клиентам p и g
    for client in Clients:
        pg_str = str(p), str(g)
        pg = ':'.join(pg_str)
        client.send(protS("pg", p, g))

    # Вычисление секретного ключа
    def syncSecretKey(clienst):
        def setSecret(client, secret, last=False):
            flag = "setLast" if last else "setTemp"
            client.send(protS(flag, secret))

        def getSecretTemp(client):
            client.send(protS("getSecretTemp"))
            return int(client.recv(2048).decode('utf-8'))

        def getPublic(client):
            client.send(protS("getPublic"))
            return int(client.recv(2048).decode('utf-8'))

        for i in range(n_cl):
            if n_cl == 2:
                setSecret(clienst[(i+1) % n_cl],
                          getPublic(clienst[i % n_cl]), last=True)
            else:
                setSecret(clienst[(i+1) % n_cl],
                          getPublic(clienst[i % n_cl]))
                j = i+2
                for _ in range(n_cl-3):
                    setSecret(clienst[j % n_cl], getSecretTemp(
                        clienst[(j-1) % n_cl]))
                    j += 1
                setSecret(clienst[(i+n_cl-1) % n_cl],
                          getSecretTemp(clienst[(i+n_cl-2) % n_cl]), last=True)

    syncSecretKey(Clients)

    conn.close()
