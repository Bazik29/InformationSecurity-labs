def decode(str, k, alph):
    result_str = ""
    for i in range(len(str)):
        res = alph.find(str[i])
        if(res != -1):
            pos = (res - k) % len(alph)
            result_str += alph[pos]
        else:
            result_str += str[i]
    return result_str


def test_bigram(str):
    tests = [
        "ГЪ", "КЩ", "ЩФ", "ЩЗ", "ЭЩ", "ЩК", "ГЩ", "ЩП", "ЩТ", "ЩШ", "ЩГ", "ЩМ", "ФЩ", "ЩЛ", "ЩД",
        "ДЩ", "ЧЦ", "ВЙ", "ЙА", "ШЯ", "ШЫ", "ГЮ", "ХЯ", "ЙЫ", "ЦЯ", "ГЬ", "СЙ", "ХЮ", "ЪЖ", "ЪД",
        "УЬ", "ЩЧ", "ЧЙ", "ШЙ", "ШЗ", "ЫФ", "ЖЩ", "ЖШ", "ЖЦ", "ЫЪ", "ЫЭ", "ЫЮ", "ЫЬ", "ЖЙ", "ЫЫ",
        "ЖЪ", "ЖЫ", "ЪШ", "ПЙ", "ЪЩ", "ЗЩ", "ЪЧ", "ЪЦ", "ЪУ", "ЪФ", "ЪХ", "ЪЪ", "ЪЫ", "ЫО", "ЖЯ",
        "ЗЙ", "ЪЬ", "ЪЭ", "ЫА", "НЙ", "ЕЬ", "ЦЙ", "ЬЙ", "ЬЛ", "ЬР", "ПЪ", "ЕЫ", "ЕЪ", "ЬА", "ШЪ",
        "ЪТ", "ЩС", "ОЬ", "КЪ", "ОЫ", "ЩХ", "ЩЩ", "ЩЪ", "ЩЦ", "КЙ", "ОЪ", "ЦЩ", "ЛЪ", "МЙ", "ШЩ",
        "ЦЬ", "ЦЪ", "ЩЙ", "ЙЬ", "ЪГ", "ИЪ", "ЪБ", "ЪВ", "ЪИ", "ЪЙ", "ЪП", "ЪР", "ЪС", "ЪО", "ЪН",
        "ЪК", "ЪЛ", "ЪМ", "ИЫ", "ИЬ", "ЙУ", "ЩЭ", "ЙЫ", "ЙЪ", "ЩЫ", "ЩЮ", "ЩЯ", "ЪА", "МЪ", "ЙЙ",
        "ЙЖ", "ЬУ", "ГЙ", "ЭЪ", "УЪ", "АЬ", "ЧЪ", "ХЙ", "ТЙ", "ЧЩ", "РЪ", "ЮЪ", "ФЪ", "УЫ", "АЪ",
        "ЮЬ", "АЫ", "ЮЫ", "ЭЬ", "ЭЫ", "БЙ", "ЯЬ", "ЬЫ", "ЬЬ", "ЬЪ", "ЯЪ", "ЯЫ", "ХЩ", "ДЙ", "ФЙ"
    ]
    for test in tests:
        if (str.find(test) != -1):
            return False
    return True


def test_freq(str, freq, k):
    str_freq = {}
    str_len = len(str)

    for i in range(str_len):
        str_freq[str[i]] = str_freq.get(str[i], -1) + 1

    summa = 0
    for ch in str_freq:
        if (str_freq[ch] / str_len > freq.get(ch, 1)):
            summa += 1
    return k > (summa / len(str_freq))


if __name__ == "__main__":
    alph = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    frequency = {
        'О': 0.1097, 	'Е': 0.0845,
        'А': 0.0801, 	'И': 0.0735,
        'Н': 0.067, 	'Т': 0.0626,
        'С': 0.0547, 	'Р': 0.0473,
        'В': 0.0454, 	'Л': 0.044,
        'К': 0.0349, 	'М': 0.0321,
        'Д': 0.0298, 	'П': 0.0281,
        'У': 0.0262, 	'Я': 0.0201,
        'Ы': 0.019, 	'Ь': 0.0174,
        'Г': 0.017, 	'З': 0.0165,
        'Б': 0.0159, 	'Ч': 0.0144,
        'Й': 0.0121, 	'Х': 0.0097,
        'Ж': 0.0094, 	'Ш': 0.0073,	
        'Ю': 0.0064, 	'Ц': 0.0048,
        'Щ': 0.0036, 	'Э': 0.0032,
        'Ф': 0.0026, 	'Ъ': 0.0004,
        'Ё': 0.0004
    }


    source_str = "ШОФТЙЧШЩМЕТУЖЦВЮБУАШЬТ,ЯТУЩОЫЫЙЧЯЭЬЪЬЗКМТЮБСЬСЬ ШЩМЕA"

    for i in range(1, 33):
        res = decode(source_str, i, alph)
        if (test_freq(res, frequency, 0.25)):
            print(i, res)

    print("---")

    for i in range(1, 33):
        res = decode(source_str, i, alph)
        if (test_bigram(res)):
            print(i, res)
