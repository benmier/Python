import os, binascii # include this at the top of your file
salt = binascii.b2a_hex(os.urandom(15))
print salt
for i in range(0,1000):
	print binascii.b2a_hex(os.urandom(35)) 