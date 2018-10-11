# Шифр Виженера
import random


def code(string, key, alph):
    if len(string) != len(key):
        return "ERROR!!!"
    result = ""
    string_list = list(string)
    key_list = list(key)
    alph_list = list(alph)
    for i in range(0, len(string)):
        a = alph.find(string_list[i])
        b = alph.find(key_list[i])
        c = (a + b) % len(alph)
        result += alph_list[c]
    return result


def decode(string, key, alph):
    if len(string) != len(key):
        return "ERROR!!!"
    result = ""
    string_list = list(string)
    key_list = list(key)
    alph_list = list(alph)
    for i in range(0, len(string)):
        c = alph.find(string_list[i])
        b = alph.find(key_list[i])
        a = (c - b) % len(alph)
        result += alph_list[a]
    return result


def gen_key(string, alph):
    result = ""
    alph_list = list(alph)
    for ch in string:
        result += alph_list[random.randint(0, len(alph) - 1)]
    return result


if __name__ == "__main__":
    # удалено: Ё
    alph = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

    source = "ИСПОЛЪЗУЙТЕСРЕДСТВАКРИПТОГРАФИИДЛЯЗАЩИТЫ"
    key = gen_key(source, alph)

    code_string = code(source, key, alph)
    decode_string = decode(code_string, key, alph)

    print("КЛЮЧ -", key)
    print("ИСХД -", source)
    print("ШИФР -", code_string)
    print("ДЕКД -", decode_string)
