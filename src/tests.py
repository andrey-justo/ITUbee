'''
Created on Dec 9, 2016

Tests for hexadecimal implementation

@author: andrey.justo
'''

from itubee.main import ITUbee
import time

itubee = ITUbee()

# First test
plain_text = '01000000000000000000'
key = '00000000000000000080'

start = time.time()
enc = itubee.encrypt(plain_text, key)
print(enc)

dec = itubee.decrypt(enc, key)
print(dec)

end = time.time()
print(end - start)

# 2 test
plain_text = '00000000000000000000'
key = '00000000000000000000'

start = time.time()
enc = itubee.encrypt(plain_text, key)
print(enc)

dec = itubee.decrypt(enc, key)
print(dec)

end = time.time()
print(end - start)

# 3 test
plain_text = 'c538bd9289822be43363'
key = '6925278951fbf3b25ccc'

start = time.time()
enc = itubee.encrypt(plain_text, key)
print(enc)

dec = itubee.decrypt(enc, key)
print(dec)

end = time.time()
print(end - start)

# 4 test
plain_text = '6925288A51fCf3b25ccc'
key = '6925288A51fCf3b25ccc'

start = time.time()
enc = itubee.encrypt(plain_text, key)
print(enc)

dec = itubee.decrypt(enc, key)
print(dec)

end = time.time()
print(end - start)