from general import *

def equateLen(x, passphr):
	sameLength = False
	pp = ""
	while not sameLength:
		for c in passphr:
			pp = pp+c
			if len(pp) == len(pp):
				sameLength = True
				break

	return pp

def encrypt(x, passphr):
	pp = equateLen(x, passphr)
	
	res = ""
	for i in range(0, len(pp)):
		res += itoc(ctoi(pp[i])+ctoi(x[i]))

	return res

print encrypt("ATTACK", "ABC")

