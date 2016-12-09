'''
Created on Dec 9, 2016

Tests for texts implementation

@author: andrey.justo
'''

from itubee.main import ITUbeeTexts

itubee = ITUbeeTexts()

key2 = '00000000000000000080'
plain_text2 = 'Andrey Rocks'

enc2 = itubee.encrypt_text(plain_text2, key2)
dec2 = itubee.decrypt_text(enc2, key2)
print(enc2)
print(dec2)
print(dec2 == plain_text2)