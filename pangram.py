alfabet = 'abcdifghijklmnopqrstuvwxyz'

def cheak(text):
	return set(text.lower()).issuperset(set(alfabet))