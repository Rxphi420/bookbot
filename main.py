def Main():
	with open("./books/frankenstein.txt") as buch:
		print (charakter_count(buch))
from stats import word_count, charakter_count

Main()
