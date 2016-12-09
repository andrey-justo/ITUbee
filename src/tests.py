'''
Created on Dec 9, 2016

Tests for hexadecimal implementation

@author: andrey.justo
'''

from itubee.main import ITUbee
import time

start = time.time()
itubee = ITUbee()
 
key = '00000000000000000080'
plain_text = '01000000000000000000'
enc = itubee.encrypt(plain_text, key)
dec = itubee.decrypt(enc, key)
print(enc)
print(dec)
print(dec == plain_text)

end = time.time()
print(end - start)