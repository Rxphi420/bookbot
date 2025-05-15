def Main():
	with open("./books/frankenstein.txt") as buch:
		print (f" {word_count(buch)} words found in the document")
def word_count(f):
	words = get_book_text(f).split()
	word_count = 0
	for i in words:
		word_count +=1
	return word_count

def get_book_text(f):
	file_contents = f.read()
	return file_contents
	
Main()
