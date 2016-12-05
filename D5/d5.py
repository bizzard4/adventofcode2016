import hashlib

id = 0
base = "uqwqemis"
hit_count = 0
password = ['', '', '', '', '', '', '', '']

while hit_count<8:
		res = hashlib.md5((base+str(id)).encode('utf-8')).hexdigest()
		if (res.startswith('00000')):
			try:
				pos = int(res[5])
				if (pos >= 0) and (pos <= 7):
					print("HIT : " + res)
					if password[pos] == '':
						password[pos] += res[6]
						hit_count+=1
						print(*password)
			except ValueError:
				print("woops bad position")
				
		if (id%1000000==0):
			print("AT = " + str(id))

		id += 1

print(password)