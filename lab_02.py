# Шифр Плейфейера
import numpy as np


def prepare_key(key):
    res_key = ""
    for char in key.translate(''.maketrans('ЬЙЁ', 'ЪИЕ')):
        if res_key.find(char) == -1:
            res_key += char
    return "".join(res_key)


def key_matrix(key, alph):
    temp = list(key)
    for char in alph:
        if key.find(char) == -1:
            temp += char
    array = np.array(temp).reshape(5, 6)
    return array


def decode(string, matrix):
    h, w = matrix.shape
    h -= 1
    w -= 1
    # Разбиваем на пары
    temp = [string[i:i + 2] for i in range(0, len(string), 2)]
    answer = ''
    x1, y1, x2, y2 = 0, 0, 0, 0
    for element in temp:
        # Позиция букв в матрице
        i, j = np.where(matrix == element[0])
        n, m = np.where(matrix == element[1])
        i, j = i[0], j[0]
        n, m = n[0], m[0]
        # Если в одной строке
        if i == n:
            y1 = y2 = i
            if j == 0:
                x1 = w
            else:
                x1 = j - 1
            x2 = m - 1
        # Если в одной колонке
        elif j == m:
            x1 = x2 = j
            if i == 0:
                y1 = h
            else:
                y1 = i - 1
            y2 = n - 1
        # Если в разных
        else:
            x1 = m
            y1 = i
            x2 = j
            y2 = n
        answer += matrix[y1][x1] + matrix[y2][x2]
    return answer


if __name__ == "__main__":
    # удалено: Й Ё Ь
    alph = 'АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЭЮЯ'

    key_word = 'СОЛНЦЕ'
    decode_string = 'ЗОИЦОЫИТЗУСОШЖАЦФАВЗЗКЗЧНБЗЖУКПБЕЫТЗЪЗФЩ'

    new_key = prepare_key(key_word)
    matrix = key_matrix(new_key, alph)
    result = decode(decode_string, matrix)

    print(new_key)
    print(matrix)
    print(decode_string)
    print(result)
