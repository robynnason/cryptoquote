from collections import Counter
import string, random
import hashlib

# TODO--make a webscraper of famous/good quotes
quote = "Robyn Samantha Nason"
quote = quote.upper()

quote_counter = Counter(quote)

alphabet = string.uppercase
crypt = dict()
count = 0

for letter in list(quote_counter):
	if letter.isalpha():
		rand = int(random.uniform(0,25))
		while alphabet[rand] in crypt.values() and alphabet[rand] != letter:
			rand = int(random.uniform(0,25))
		crypt[letter] = alphabet[rand]

# Going through each letter one by one to avoid issues using replace
new_quote = []
count = 0
for original in quote:
	if original.isalpha():
		new_quote.append(crypt[original])
	else:
		new_quote.append(original)
print ''.join(new_quote)
print crypt.values()
print crypt.keys()



