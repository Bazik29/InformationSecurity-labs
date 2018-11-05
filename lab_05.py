# Шифр «Поворотная решетка»
import numpy as np


class RotateGrilee(object):
    def __init__(self):
        self.EMPTY = 0
        self.HOLE = 1
        self.BLOCK = 2

    def encode(self, text, grille):
        encode_matrix = np.chararray(grille.shape, unicode=True)
        encode_matrix[:] = ''
        text_index = 0
        # Прямое
        for m_index, value in np.ndenumerate(grille):
            if value:
                encode_matrix[m_index] = text[text_index]
                text_index += 1
        # Переворот на 180
        rot180 = np.rot90(grille, 2)
        for m_index, value in np.ndenumerate(rot180):
            if value:
                encode_matrix[m_index] = text[text_index]
                text_index += 1
        # Отзеркаливание с переворотом
        flip_rot180 = np.fliplr(rot180)
        for m_index, value in np.ndenumerate(flip_rot180):
            if value:
                encode_matrix[m_index] = text[text_index]
                text_index += 1
        # Поворот на 180 отзеркаливания с переворотом
        rot180_flip_rot180 = np.rot90(flip_rot180, 2)
        for m_index, value in np.ndenumerate(rot180_flip_rot180):
            if value:
                encode_matrix[m_index] = text[text_index]
                text_index += 1
        return encode_matrix

    def decode(self, matrix, grille):
        decode_text = []
        # Прямое
        for m_index, value in np.ndenumerate(grille):
            if value:
                decode_text.append(matrix[m_index])
        # Переворот на 180
        rot180 = np.rot90(grille, 2)
        for m_index, value in np.ndenumerate(rot180):
            if value:
                decode_text.append(matrix[m_index])
        # Отзеркаливание с переворотом
        flip_rot180 = np.fliplr(rot180)
        for m_index, value in np.ndenumerate(flip_rot180):
            if value:
                decode_text.append(matrix[m_index])
        # Поворот на 180 отзеркаливания с переворотом
        rot180_flip_rot180 = np.rot90(flip_rot180, 2)
        for m_index, value in np.ndenumerate(rot180_flip_rot180):
            if value:
                decode_text.append(matrix[m_index])
        return ''.join(decode_text)

    def prepareText(self, text, aggreg="*"):
        text = text.replace(' ', '').replace('\t', '').replace('\n', '')
        # ужс...
        while(len(text) % 4 != 0):
            text = text + aggreg
        return text

    def getAllDims(self, text):
        dims = []
        for i in range(len(text)):
            for j in range(len(text)):
                if (i % 2 == 0 and j % 2 == 0 and i * j == len(text)):
                    dims.append([i, j])
        return dims

    def genEmptyGrillee(self, dims):
        return np.array([self.EMPTY for i in range(dims[0]*dims[1])]).reshape(dims[0], dims[1])

    def addHole(self, grille, pos):
        shape = grille.shape
        h = shape[0] - 1
        w = shape[1] - 1
        i = pos[0]
        j = pos[1]
        if grille[i][j] != self.BLOCK:
            grille[i][j] = self.HOLE
            grille[h-i][j] = self.BLOCK
            grille[i][w-j] = self.BLOCK
            grille[h-i][w-j] = self.BLOCK

    def testGrillee(self, grille):
        shape = grille.shape
        h = shape[0] - 1
        w = shape[1] - 1
        for i in range(h):
            for j in range(w):
                sum = 0
                if grille[i][j] != grille[h-i][j]:
                    sum += 1
                if grille[i][j] != grille[i][w-j]:
                    sum += 1
                if grille[i][j] != grille[h-i][w-j]:
                    sum += 1
                if grille[i][j] == self.EMPTY or grille[i][j] == self.HOLE and sum != 3 or grille[i][j] == self.BLOCK and sum != 1:
                    return [False, [[i, j], [h-i, j], [i, w-j], [h-i, w-j]]]
        return [True]


if __name__ == "__main__":
    rg = RotateGrilee()
    arr = np.array([[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 1, 0, 1, 1, 0, 0],
                    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
                    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]]
                   )
    text = "ШИФРРЕШЕТКАЯВЛЯЕТСЯЧАСТНЫМ\nСЛУЧАЕМШИФРА МАРШРУТНОЙ\tПЕРЕСТАНОВК"
    # text = rg.prepareText(text)
    # print(rg.genEmptyGrillee([4, 8]))
    # print(len(text))
    # print(rg.getAllDims(text))
    # print(rg.encode(text, arr))
    # print(rg.decode(rg.encode(text, arr), arr))

    gr = rg.genEmptyGrillee([6, 10])

    # print(gr)

    rg.addHole(gr, [0, 1])
    rg.addHole(gr, [1, 0])
    rg.addHole(gr, [1, 4])
    rg.addHole(gr, [1, 6])
    rg.addHole(gr, [1, 7])
    rg.addHole(gr, [2, 1])
    rg.addHole(gr, [2, 5])
    rg.addHole(gr, [2, 9])
    rg.addHole(gr, [3, 3])
    rg.addHole(gr, [3, 7])
    rg.addHole(gr, [4, 1])
    rg.addHole(gr, [5, 2])
    rg.addHole(gr, [5, 5])
    rg.addHole(gr, [5, 6])
    rg.addHole(gr, [5, 9])
    print(gr)
    print(rg.testGrillee(gr))
