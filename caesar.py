"""Encrypts and Decrypts using the Caesar Cipher. License: Tell me if you ever use it, but, if you don't its okay, I don't really care."""
def ctoi(c):
	return (ord(c.upper())-64)

def itoc(v):
	return (chr(v+64))

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
	print encrypt("I am awesome", 15)
	print decrypt("ydc", 15)
