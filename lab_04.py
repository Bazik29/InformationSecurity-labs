# Шифр вертикальной перестановки


import numpy as np
from itertools import permutations
from analysis import test_bigram


def encryption_VertTranspos(text, key):
    len_key = len(key)
    len_txt = len(text)
    if len_txt % len_key != 0:
        raise Exception("Не возможно сотавить матрицу")

    order = [int(x) - 1 for x in key]
    matrix = np.array(list(text)).reshape(int(len_txt / len_key), len_key)
    temp = []
    for i in range(len_key):
        temp.append(list(matrix[:, order.index(i)]))
    return "".join(np.hstack(temp))


def decryption_VertTranspos(text, key):
    len_key = len(key)
    len_txt = len(text)
    if len_txt % len_key != 0:
        raise Exception("Не возможно сотавить матрицу")
    order = [int(x) - 1 for x in key]
    matrix = np.array(list(text)).reshape(len_key, int(len_txt / len_key))
    matrix = np.transpose(matrix)
    temp = []
    for i in range(len_key):
        temp.append(list(matrix[:, order[i]]))
    temp = np.transpose(temp)
    return "".join(np.hstack(temp))


def brute_VertTranspos(encrypt_text, key, test_func, *args, **kwargs):
    len_key = len(key)
    pos = []
    numbers = [i for i in range(1, len_key + 1)]

    template_key = [0 for i in range(len_key)]
    # Заполнение шаблона, позиции неизвестных и известные позиции
    for i, ch in enumerate(key):
        if ch.isdigit():
            numbers.remove(int(ch))
            template_key[i] = int(ch)
        else:
            pos.append(i)

    all_keys = []
    for set_nums in list(permutations(numbers)):
        for i, p in enumerate(pos):
            template_key[p] = set_nums[i]
        all_keys.append("".join(map(str, template_key)))

    # Перебор
    result_dict = {}
    for key_nums in all_keys:
        test_key = "".join(map(str, key_nums))
        res = decryption_VertTranspos(encrypt_text, test_key)
        if test_func(res, *args, **kwargs):
            result_dict[test_key] = res
    return result_dict


if __name__ == "__main__":
    # test_text = "ПЕРЕСТАНОВКАТЕКСТАПОСТОЛБЦАМ"
    # test_key = "4312567"
    # encrypt_text = encryption_VertTranspos(test_text, test_key)
    # decrypt_text = decryption_VertTranspos(encrypt_text, test_key)

    # print("Test  :", test_text)
    # print("Key   :", test_key)
    # print("Encode:", encrypt_text)
    # print("Decode:", decrypt_text)
    # print("Test decryption:", decrypt_text == test_text)

    source_text = "БСЕАГНМЗЛАЕООЯНПЛТБНАЕЕСЬЬЕА"
    key = "2X41XX7"

    brute_res = brute_VertTranspos(
        source_text, key, lambda x: test_bigram(x))

    for key, test in brute_res.items():
        print(key, test)
