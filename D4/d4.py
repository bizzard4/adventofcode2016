from collections import OrderedDict
from operator import itemgetter

rooms = list(map(lambda s: s.split('-'), open('input.txt', 'r').read().split('\n')))

sector_list = []

for i in range(len(rooms)):
	room_def = rooms[i]

	# Build letters dictionary
	letters_hash = {}
	for j in range(len(room_def)-1):
			for c in room_def[j]:
				if c not in letters_hash:
					letters_hash[c] = 0
				letters_hash[c] = letters_hash[c] + 1
	#print(letters_hash)

	# Sort dictionary from letter cound and validate [hash]
	sector, hash_val = room_def[len(room_def)-1].replace(']', '').split('[')
	#print(sector, hash_val)
	letters_hash = OrderedDict(sorted(letters_hash.items(), key=itemgetter(0)))
	letters_hash = sorted(letters_hash.items(), key=itemgetter(1), reverse=True)
	#print(letters_hash)

	# Validate with hash_val
	good = True
	for index in range(len(hash_val)):
		if (hash_val[index] != letters_hash[index][0]):
			good = False
			break

	# If good, we decrypt and show result
	if (good):
		print("Decrypting : ", *room_def)

		# Shift cipher letters
		sentense = ' '.join(room_def[0:len(room_def)-1])
		decrypted_sentense = ""
		for c in sentense:
			if (c == ' '):
				decrypted_sentense += ' '
			else:
				decrypted_sentense += chr((((ord(c)-97)+int(sector))%26)+97)

		if ("north" in decrypted_sentense):
			print("========================== " + decrypted_sentense)


		sector_list.append(int(sector))

print(sum(sector_list))