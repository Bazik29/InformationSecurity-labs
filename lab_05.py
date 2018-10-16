# Шифр «Поворотная решетка»


import numpy as np


def encode_RotateGrille(text, grille):
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


def decode_RotateGrille(matrix, grille):
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


arr = np.array([[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 1, 0, 1, 1, 0, 0],
                [0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
                [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]]
               )
text = "ШИФРРЕШЕТКАЯВЛЯЕТСЯЧАСТНЫМСЛУЧАЕМШИФРАМАРШРУТНОЙПЕРЕСТАНОВКИ"

print(encode_RotateGrille(text, arr))
print(decode_RotateGrille(encode_RotateGrille(text, arr), arr))
