# Шифр Цезаря

# from analysis import test_bigram
from analysis import test_freq


def encryption_Caesar(text, key, alphabet):
    result = ""
    len_alp = len(alphabet)
    for i in range(0, len(text)):
        char_index = alphabet.find(text[i])
        if char_index != -1:
            pos = (char_index + key) % len_alp
            result += alphabet[pos]
        else:
            result += text[i]
    return result


def decryption_Caesar(text, key, alphabet):
    result = ""
    len_alp = len(alphabet)
    for i in range(len(text)):
        char_index = alphabet.find(text[i])
        if char_index != -1:
            pos = (char_index - key) % len_alp
            result += alphabet[pos]
        else:
            result += text[i]
    return result


def broot_Caesar(text, alphabet, test_func, *args, **kwargs):
    result_dict = {}
    for i in range(1, len(alphabet) + 1):
        res = decryption_Caesar(encrypt_text, i, alphabet)
        if test_func(res, *args, **kwargs):
            result_dict[i] = res
    return result_dict


if __name__ == "__main__":
    alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

    encrypt_text = "ШОФТЙЧШЩМЕТУЖЦВЮБУАШЬТ,ЯТУЩОЫЫЙЧЯЭЬЪЬЗКМТЮБСЬСЬ ШЩМЕA"

    broot_res = broot_Caesar(encrypt_text, alphabet, test_freq, k=0.25)

    for key, test in broot_res.items():
        print(key, test)

    test_encrypt = encryption_Caesar(decryption_Caesar(
        encrypt_text, 14, alphabet), 14, alphabet)
    print("Test encryption:", encrypt_text == test_encrypt)
