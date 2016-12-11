import re

ips = open('input.txt', 'r').read().split('\n')

support_tls = 0
support_ssl = 0
total_aba = 0

print(len(ips))

def is_abba(word):
	if (len(word) >= 4):
		for i in range(len(word)-3):
			a = word[i]
			b = word[i+1]
			if a==b:
				continue

			bb = word[i+2]
			if b!=bb:
				continue

			aa = word[i+3]
			if a!=aa:
				continue

			return True
	return False

def check_for_bab(bab, hypernets):
	for hyper_ip in hypernets:
		if bab in hyper_ip:
			#print("Found " + bab + " in " + h)
			return True
	return False

for code in ips:
	hypernet = []
	non_hypernet = []

	for seq in code.split(']'):
		temp = seq.split('[')
		if (len(temp)==2):
			hypernet.append(temp[1])

		non_hypernet.append(temp[0])

	# First we check if any abba in hypernet
	cancel = False
	for h in hypernet:
		if is_abba(h):
			cancel = True
			break

	if not cancel:
		# Then we need at least one abba in the rest
		found = False
		for h in non_hypernet:
			if is_abba(h):
				found = True
				break

		if found:
			support_tls += 1

	# Part 2

	# Find a aba in any non_hypernet
	for h in non_hypernet:
		if (len(h) >= 3):
			found_aba = False
			for i in range(len(h)-2):
				a = h[i]
				b = h[i+1]
				if a==b:
					continue

				aa = h[i+2]
				if a!=aa:
					continue

				total_aba += 1

				# Check if the corresponding bab is present in any hypernet
				aba = a+b+a
				bab = b+a+b
				if check_for_bab(b+a+b, hypernet):
					found_aba = True
					break
				else:
					print(aba + " but no " + bab + " in " + code)

			if found_aba:
				support_ssl += 1
				#print(code)
				break

	

print(support_tls, support_ssl, total_aba)
