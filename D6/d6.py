import operator

codes = open('input.txt', 'r').read().split('\n')

frequent = [{},{},{},{},{},{},{},{}]
col_count = 8

for code in codes:
	for col in range(col_count):
		d = frequent[col]
		if code[col] not in d:
			d[code[col]] = 0
		d[code[col]] += 1

password = ""
for i in range(col_count):
	password += min(frequent[i], key=frequent[i].get)

print(password)
