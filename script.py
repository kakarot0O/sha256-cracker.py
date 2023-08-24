from pwn import *
import sys

if len(sys.argv)!= 2:
	print("Invalid arguments !")
	print(">> {} <sha256sum>".format(sys.argv[0]))
	exit()

hash = sys.argv[1]
password_file = "" # Enter full path to the password file , I have used latin encoding and decoding in this specifically for rockyou.txt file, if you use something else, change those options accordingly
attempts = 0

with log.progress("Attempting to back: {}!\n".format(hash)) as p:
	with open(password_file,"r",encoding='latin-1') as password_list:
		for password in password_list:
			password = password.strip("\n").encode("latin-1")
			password_hash = sha256sumhex(password)
			p.status("[{}] {} == {}".format(attempts,password.decode('latin-1'),password_hash))
			if password_hash == hash:
				p.success("Password hash found after {} attempts ! {} hashes to {}!".format(attempts,password.decode('latin-1'),password_hash))
				exit()
			attempts+=1
		p.failure("Password hash not found!")
