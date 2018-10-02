
def decode(str, k, alph):
	result_str = ""
	for i in range(len(str)):
		res  = alph.find(str[i])
		if(res != -1):
			pos = (res - k) % len(alph)
			result_str += alph[pos]
		else:
			result_str += str[i]
	return result_str


def filtr(str):
	tests = ["ЦЦ", "ОЪ", "АЪ"]
	for test in tests:
		if (str.find(test) != -1): return False
	return True

if __name__ == "__main__":
	alph = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
	source_str = "ШОФТЙЧШЩМЕТУЖЦВЮБУАШЬТ,ЯТУЩОЫЫЙЧЯЭЬЪЬЗКМТЮБСЬСЬ ШЩМЕA"

	for i in range(1, 33):
		res = decode(source_str, i, alph)
		if (filtr(res)):
			print(i, decode(source_str, i, alph))
