from random import randint

one_time_pad_file = 'secret.txt'
ascii_beg = 65
ascii_end = 122

ascii_space = 32

ascii_jump = 17

def random_ascii_int():
	i = randint(ascii_beg - 1, ascii_end)
	# space is not in our contiguous range of allowed ascii characters 
	# but we want it in our charset
	if i == ascii_beg - 1: i = ascii_space
	return i

def random_ascii():
	return chr(random_ascii_int())

# generate a one time pad ASCII string
def generate(length):
	return ''.join([random_ascii() for _ in range(length)])

# generate a new one time pad from an old ascii string
def generate_from_key(key):
	s = ''
	for c in key:
		i = ord(c)+ascii_jump
		if i >= ascii_end: i -= (ascii_end - ascii_beg)
		s += chr(i)
	return s

# generate and save a one time pad ASCII string
def generate_and_save(length):
	secret_key = generate(length)
	wr = open(one_time_pad_file, 'w')
	wr.write(secret_key)

# read secret key from file
def read_key_from_disk():
	return open(one_time_pad_file).read()

# generate a secret key and encrypt a string 
def strong_encrypt(string):
	secret_key = generate(len(string))
	return crypto(string, secret_key)

# encrypt or decrypt a string with one time pad
def crypto(string, secret_key):
	return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(string, secret_key))

# print an xor key as ascii
def ascii_key(key):
	return ''.join(chr(ord(c) + ascii_beg) for c in key)