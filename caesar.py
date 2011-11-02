from general import *

"""pt: string to encrypt, plaintext
   si: shift index"""
def encrypt(pt, si):
	res = ""
	for char in pt:
		if char == " ":
			res += " "
			continue

		res += itoc((ctoi(char)+si)%26)

	return res

"""et: encrypted string
   si: shift index"""
def decrypt(et, si):
	res = ""
	for char in et:
		if char == " ":
			res += " "

		res += itoc((ctoi(char)-si)%26)
	return res

if __name__ == "__main__":
	print "Note: Spaces are just ignored"

	print "Enter something to encrypt: "
	x = raw_input()
	print "Enter shift: "
	s = int(raw_input())
	print "Encrypted: ", encrypt(x, s)

	print "Enter something to decrypt: "
	x = raw_input()
	print "Enter shift: "
	s = int(raw_input())
	print "Decrypted: ", decrypt(x, s)

