# Copyrigt
from string import ascii_lowercase as az

def cheak(text):
	return set(text.lower()).issuperset(set(az))

print (cheak('abc') == False)
print (cheak('abcdefghijklmnopqrstuvwxyz') == True)
print (cheak('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == True)
print (cheak('Quick brown fox jumps over the lazy dog') == True)