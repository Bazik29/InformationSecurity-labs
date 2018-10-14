# Шифр Плейфейера


import numpy as np


def maxtrix_Playfair(key, alphabet, h=5, w=6):
    # Создание матрицы
    temp = list(key)
    for char in alphabet:
        if key.find(char) == -1:
            temp += char
    matrix = np.array(temp).reshape(h, w)
    return matrix


def encryption_Playfair(text, key, alphabet, h=5, w=6, aggreg="Э"):
    matrix = maxtrix_Playfair(key, alphabet, h, w)

    # Преобразование текста
    pairs = []
    if len(text) % 2 != 0:
        text += aggreg
    for i in range(0, len(text) - 1, 2):
        if text[i] != text[i + 1]:
            pairs.append(text[i] + text[i + 1])
        else:
            pairs.append(text[i] + aggreg)
            pairs.append(aggreg + text[i + 1])

    encrypt_text = ''
    x0, y0, x1, y1 = 0, 0, 0, 0
    for element in pairs:
        # Позиция букв в матрице
        row_0, col_0 = np.where(matrix == element[0])
        row_1, col_1 = np.where(matrix == element[1])
        row_0, col_0 = row_0[0], col_0[0]
        row_1, col_1 = row_1[0], col_1[0]

        # Если в одной строке
        if row_0 == row_1:
            y0 = y1 = row_0
            x0 = (col_0 + 1) % w
            x1 = (col_1 + 1) % w
        # Если в одной колонке
        elif col_0 == col_1:
            x0 = x1 = col_0
            y0 = (row_0 + 1) % h
            y1 = (row_1 + 1) % h
        # Иначе
        else:
            y0 = row_0
            x0 = col_1
            y1 = row_1
            x1 = col_0
        encrypt_text += matrix[y0][x0] + matrix[y1][x1]
    return encrypt_text


def decryption_Playfair(text, key, alphabet, h=5, w=6):
    matrix = maxtrix_Playfair(key, alphabet, h, w)

    # Разбиваем на пары
    temp = [text[i:i + 2] for i in range(0, len(text), 2)]

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
                x1 = w - 1
            else:
                x1 = j - 1
            x2 = m - 1
        # Если в одной колонке
        elif j == m:
            x1 = x2 = j
            if i == 0:
                y1 = h - 1
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


def prepare_key(key):
    res_key = ""
    for char in key.translate(''.maketrans('ЬЙЁ', 'ЪИЕ')):
        if res_key.find(char) == -1:
            res_key += char
    return "".join(res_key)


if __name__ == "__main__":
    # # удалено: Й Ё Ь
    alphabet = 'АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЭЮЯ'

    key = "СОЛНЦЕ"
    encrypt_text = "ЗОИЦОЫИТЗУСОШЖАЦФАВЗЗКЗЧНБЗЖУКПБЕЫТЗЪЗФЩ"

    key_word = prepare_key(key)

    print(maxtrix_Playfair(key_word, alphabet))

    decrypt_text = decryption_Playfair(encrypt_text, key_word, alphabet)
    print(encrypt_text)
    print(decrypt_text)

    test_encrypt = encryption_Playfair(decrypt_text, key_word, alphabet)
    print("Test encryption:", encrypt_text == test_encrypt)
