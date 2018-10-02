
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

alph = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

test = "Н	У	Л	Т	Х	С	Ж	У	Г	Ч	Л	В"
print(decode(test, 3, alph))

source_str = "ШОФТЙЧШЩМЕТУЖЦВЮБУАШЬТ,ЯТУЩОЫЫЙЧЯЭЬЪЬЗКМТЮБСЬСЬ ШЩМЕA"

for i in range(1, 33):
	print(i,decode(source_str, i, alph))

# print(decode(source_str, 14, alph))
