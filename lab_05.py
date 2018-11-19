# # # Шифр «Поворотная решетка»
# # import numpy as np


# # class RotateGrilee(object):
# #     def __init__(self):
# #         self.EMPTY = 0
# #         self.HOLE = 1
# #         self.BLOCK = 2

# #     def encode(self, text, grille):
# #         encode_matrix = np.chararray(grille.shape, unicode=True)
# #         encode_matrix[:] = ''
# #         text_index = 0
# #         # Прямое
# #         for m_index, value in np.ndenumerate(grille):
# #             if value:
# #                 encode_matrix[m_index] = text[text_index]
# #                 text_index += 1
# #         # Переворот на 180
# #         rot180 = np.rot90(grille, 2)
# #         for m_index, value in np.ndenumerate(rot180):
# #             if value:
# #                 encode_matrix[m_index] = text[text_index]
# #                 text_index += 1
# #         # Отзеркаливание с переворотом
# #         flip_rot180 = np.fliplr(rot180)
# #         for m_index, value in np.ndenumerate(flip_rot180):
# #             if value:
# #                 encode_matrix[m_index] = text[text_index]
# #                 text_index += 1
# #         # Поворот на 180 отзеркаливания с переворотом
# #         rot180_flip_rot180 = np.rot90(flip_rot180, 2)
# #         for m_index, value in np.ndenumerate(rot180_flip_rot180):
# #             if value:
# #                 encode_matrix[m_index] = text[text_index]
# #                 text_index += 1
# #         return encode_matrix

# #     def decode(self, matrix, grille):
# #         decode_text = []
# #         # Прямое
# #         for m_index, value in np.ndenumerate(grille):
# #             if value:
# #                 decode_text.append(matrix[m_index])
# #         # Переворот на 180
# #         rot180 = np.rot90(grille, 2)
# #         for m_index, value in np.ndenumerate(rot180):
# #             if value:
# #                 decode_text.append(matrix[m_index])
# #         # Отзеркаливание с переворотом
# #         flip_rot180 = np.fliplr(rot180)
# #         for m_index, value in np.ndenumerate(flip_rot180):
# #             if value:
# #                 decode_text.append(matrix[m_index])
# #         # Поворот на 180 отзеркаливания с переворотом
# #         rot180_flip_rot180 = np.rot90(flip_rot180, 2)
# #         for m_index, value in np.ndenumerate(rot180_flip_rot180):
# #             if value:
# #                 decode_text.append(matrix[m_index])
# #         return ''.join(decode_text)

# #     def prepareText(self, text, aggreg="*"):
# #         text = text.replace(' ', '').replace('\t', '').replace('\n', '')
# #         # ужс...
# #         while(len(text) % 4 != 0):
# #             text = text + aggreg
# #         return text

# #     def getAllDims(self, text):
# #         dims = []
# #         for i in range(len(text)):
# #             for j in range(len(text)):
# #                 if (i % 2 == 0 and j % 2 == 0 and i * j == len(text)):
# #                     dims.append([i, j])
# #         return dims

# #     def genEmptyGrillee(self, dims):
# #         return np.array([self.EMPTY for i in range(dims[0]*dims[1])]).reshape(dims[0], dims[1])

# #     def addHole(self, grille, pos):
# #         shape = grille.shape
# #         h = shape[0] - 1
# #         w = shape[1] - 1
# #         i = pos[0]
# #         j = pos[1]
# #         if grille[i][j] != self.BLOCK:
# #             grille[i][j] = self.HOLE
# #             grille[h-i][j] = self.BLOCK
# #             grille[i][w-j] = self.BLOCK
# #             grille[h-i][w-j] = self.BLOCK

# #     def testGrillee(self, grille):
# #         shape = grille.shape
# #         h = shape[0] - 1
# #         w = shape[1] - 1
# #         for i in range(h):
# #             for j in range(w):
# #                 sum = 0
# #                 if grille[i][j] != grille[h-i][j]:
# #                     sum += 1
# #                 if grille[i][j] != grille[i][w-j]:
# #                     sum += 1
# #                 if grille[i][j] != grille[h-i][w-j]:
# #                     sum += 1
# #                 if grille[i][j] == self.EMPTY or grille[i][j] == self.HOLE and sum != 3 or grille[i][j] == self.BLOCK and sum != 1:
# #                     return [False, [[i, j], [h-i, j], [i, w-j], [h-i, w-j]]]
# #         return [True]


# # if __name__ == "__main__":
# #     rg = RotateGrilee()
# #     arr = np.array([[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
# #                     [1, 0, 0, 0, 1, 0, 1, 1, 0, 0],
# #                     [0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
# #                     [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
# #                     [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
# #                     [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]]
# #                    )
# #     text = "ШИФРРЕШЕТКАЯВЛЯЕТСЯЧАСТНЫМ\nСЛУЧАЕМШИФРА МАРШРУТНОЙ\tПЕРЕСТАНОВК"
# #     # text = rg.prepareText(text)
# #     # print(rg.genEmptyGrillee([4, 8]))
# #     # print(len(text))
# #     # print(rg.getAllDims(text))
# #     # print(rg.encode(text, arr))
# #     # print(rg.decode(rg.encode(text, arr), arr))

# #     gr = rg.genEmptyGrillee([6, 10])

# #     # print(gr)

# #     rg.addHole(gr, [0, 1])
# #     rg.addHole(gr, [1, 0])
# #     rg.addHole(gr, [1, 4])
# #     rg.addHole(gr, [1, 6])
# #     rg.addHole(gr, [1, 7])
# #     rg.addHole(gr, [2, 1])
# #     rg.addHole(gr, [2, 5])
# #     rg.addHole(gr, [2, 9])
# #     rg.addHole(gr, [3, 3])
# #     rg.addHole(gr, [3, 7])
# #     rg.addHole(gr, [4, 1])
# #     rg.addHole(gr, [5, 2])
# #     rg.addHole(gr, [5, 5])
# #     rg.addHole(gr, [5, 6])
# #     rg.addHole(gr, [5, 9])
# #     print(gr)
# #     print(rg.testGrillee(gr))




# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow
# from PyQt5.uic import loadUi
# from PyQt5.QtCore import QObject, QUrl, pyqtSignal


# class MyWindow(QMainWindow):
#     def __init__(self):
#         QMainWindow.__init__(self)
#         loadUi('lab_05.ui', self)


# if __name__ == "__main__":
#     app = QApplication(sys.argv)

#     mainWin = MyWindow()
#     mainWin.show()

#     sys.exit(app.exec_())

import math
import random
import itertools
import numpy as np

EMPTY = 2
HOLE = 1
BLOCK = 0


def getAllDims(value):
    dims = []
    for i in range(1, int(math.sqrt(value) + 1)):
        j = value // i
        if value % i == 0 and j % 2 == 0 and i % 2 == 0:
            dims.append([i, j])
    return dims


def testDim(pair):
    return pair[0] % 2 == 0 and pair[1] % 2 == 0


def writeDimsToFile(path, pairs):
    with open(path, 'w') as file:
        for pair in pairs:
            file.write(f"{pair[0]}x{pair[1]}\n")


def readDimsFromFile(path):
    pairs = []
    with open(path, 'r') as file:
        for line in file:
            pairs.append(list(map(int, line.split('x'))))
    return pairs


def writeKeysToFile(path, keys):
    with open(path, 'w') as file:
        for grille in keys:
            grille_str = "".join(map(str, grille.flatten()))
            file.write(f"{grille.shape[0]}x{grille.shape[1]}x{grille_str}\n")


def readKeysFromFile(path):
    keys = []
    with open(path, 'r') as file:
        for line in file:
            items = line.strip().split('x')
            grille = np.array(tuple(items[2]), dtype=int).reshape(
                int(items[0]), int(items[1]))
            keys.append(grille)
    return keys


def genGrilleRandom(dim):
    grille = np.zeros(dim[0] * dim[1], dtype=int).reshape(dim[0], dim[1])
    all_index = list(itertools.product(range(0, dim[0]), range(0, dim[1])))

    while len(all_index) != 0:
        i = random.randint(0, len(all_index) - 1)

        ind_1 = all_index[i]
        ind_2 = dim[0] - 1 - all_index[i][0], all_index[i][1]
        ind_3 = dim[0] - 1 - all_index[i][0], dim[1] - 1 - all_index[i][1]
        ind_4 = all_index[i][0], dim[1] - 1 - all_index[i][1]

        grille[ind_1[0]][ind_1[1]] = HOLE
        grille[ind_2[0]][ind_2[1]] = BLOCK
        grille[ind_3[0]][ind_3[1]] = BLOCK
        grille[ind_4[0]][ind_4[1]] = BLOCK

        all_index.pop(all_index.index(ind_1))
        all_index.pop(all_index.index(ind_2))
        all_index.pop(all_index.index(ind_3))
        all_index.pop(all_index.index(ind_4))
    return grille


def encode(text, grille):
    encode_matrix = np.chararray(grille.shape, unicode=True)
    encode_matrix[:] = ''
    text_index = 0
    # Прямое
    for m_index, value in np.ndenumerate(grille):
        if value == HOLE:
            encode_matrix[m_index] = text[text_index]
            text_index += 1
    # Переворот на 180
    rot180 = np.rot90(grille, 2)
    for m_index, value in np.ndenumerate(rot180):
        if value == HOLE:
            encode_matrix[m_index] = text[text_index]
            text_index += 1
    # Отзеркаливание с переворотом
    flip_rot180 = np.fliplr(rot180)
    for m_index, value in np.ndenumerate(flip_rot180):
        if value == HOLE:
            encode_matrix[m_index] = text[text_index]
            text_index += 1
    # Поворот на 180 отзеркаливания с переворотом
    rot180_flip_rot180 = np.rot90(flip_rot180, 2)
    for m_index, value in np.ndenumerate(rot180_flip_rot180):
        if value == HOLE:
            encode_matrix[m_index] = text[text_index]
            text_index += 1
    return encode_matrix


def decode(matrix, grille):
    decode_text = []
    # Прямое
    for m_index, value in np.ndenumerate(grille):
        if value == HOLE:
            decode_text.append(matrix[m_index])
    # Переворот на 180
    rot180 = np.rot90(grille, 2)
    for m_index, value in np.ndenumerate(rot180):
        if value == HOLE:
            decode_text.append(matrix[m_index])
    # Отзеркаливание с переворотом
    flip_rot180 = np.fliplr(rot180)
    for m_index, value in np.ndenumerate(flip_rot180):
        if value == HOLE:
            decode_text.append(matrix[m_index])
    # Поворот на 180 отзеркаливания с переворотом
    rot180_flip_rot180 = np.rot90(flip_rot180, 2)
    for m_index, value in np.ndenumerate(rot180_flip_rot180):
        if value == HOLE:
            decode_text.append(matrix[m_index])
    return ''.join(decode_text)


def encodeWithOneKey(text, key, aggreg="x"):
    text = text.replace(' ', '').replace('\t', '').replace('\n', '')
    while(key.size > len(text)):
        text += aggreg
    return ''.join(list(encode(text, key).flatten()))


def decodeWithOneKey(text, key):
    matrix = np.array(list(text)).reshape(key.shape)
    return ''.join(decode(matrix, key))


def encodeWithSeveralKeys(text, keys, aggreg="x"):
    text = text.replace(' ', '').replace('\t', '').replace('\n', '')

    encode_result = []
    ptr = 0
    for key in keys:
        while(ptr + key.size > len(text)):
            text += aggreg
        part_text = text[ptr: ptr + key.size]
        temp = encode(part_text, key)
        encode_result += list(temp.flatten())
        ptr += key.size
    return ''.join(encode_result)


def decodeWithSeveralKeys(text, keys):
    decode_result = []
    ptr = 0
    for key in keys:
        part_text = text[ptr: ptr + key.size]
        matrix = np.array(list(part_text)).reshape(key.shape)
        decode_result += decode(matrix, key)
        ptr += key.size
    return ''.join(decode_result)


def prepareTextForOneKey(self, text, aggreg="x"):
    text = text.replace(' ', '').replace('\t', '').replace('\n', '')
    while(len(text) % 4 != 0):
        text = text + aggreg
    return text


def prepareTextForSeveralKey(self, text, aggreg="x"):
    text = text.replace(' ', '').replace('\t', '').replace('\n', '')
    return text


if __name__ == "__main__":

    keys = [genGrilleRandom([2, 6]), genGrilleRandom([4, 4])]

    writeKeysToFile("test.txt", keys)

    keys_ = readKeysFromFile("test.txt")

    text = "1234567890qwertyuiozxcvaf"

    encode_ = encodeWithSeveralKeys(text, keys_)
    decode_ = decodeWithSeveralKeys(encode_, keys_)

    print(text)
    print(decode_)
