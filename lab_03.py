# Шифр Виженера
import random


def encryption_Vigenere(text, key, alphabet):
    encrypt_text = ""
    for i in range(len(text)):
        a = alphabet.find(text[i])
        if a == -1:
            raise Exception("Алфавит не содержит " + text[i])
        b = alphabet.find(key[i % len(key)])
        if b == -1:
            raise Exception("Алфавит не содержит " + key[i])
        c = (a + b) % len(alphabet)
        encrypt_text += alphabet[c]
    return encrypt_text


def decryption_Vigenere(text, key, alphabet):
    decrypt_text = ""
    for i in range(len(text)):
        c = alphabet.find(text[i])
        if c == -1:
            raise Exception("Алфавит не содержит " + text[i])
        b = alphabet.find(key[i % len(key)])
        if b == -1:
            raise Exception("Алфавит не содержит " + key[i])
        a = (c - b) % len(alphabet)
        decrypt_text += alphabet[a]
    return decrypt_text


def generate_key(length, alphabet):
    result = ""
    for i in range(length):
        result += alphabet[random.randint(0, len(alphabet) - 1)]
    return result


if __name__ == "__main__":
    # удалено: Ё
    alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

    source_text = "ИСПОЛЪЗУЙТЕСРЕДСТВАКРИПТОГРАФИИДЛЯЗАЩИТЫ"

    key_word = generate_key(random.randint(0, len(source_text) - 1), alphabet)
    encrypt_text = encryption_Vigenere(source_text, key_word, alphabet)
    decrypt_text = decryption_Vigenere(encrypt_text, key_word, alphabet)

    print("Text:", source_text)
    print("Key:", key_word)
    print("Encode:", encrypt_text)
    print("Decode:", decrypt_text)
    print("Test decryption:", decrypt_text == source_text)
