import sys
print (sys.argv)
def Main():	
	if len(sys.argv) == 2:
		with open(sys.argv[1]) as buch:
			print (f"Found {word_count(buch)} total words")
			buch.seek(0)
			for char_data in charakter_count(buch):
       				 print(f"{char_data['char']}: {char_data['num']}")
	else:
		print ("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
from stats import word_count, charakter_count
Main()
