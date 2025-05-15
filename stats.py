def word_count(f):
        words = get_book_text(f).split()
        word_count = 0
        for i in words:
                word_count +=1
        return word_count
def get_book_text(f):
        file_contents = f.read()
        return file_contents
def charakter_count(f):
	lowercase = get_book_text(f).lower()
	cha = list(lowercase)
	letter_count = {}
	for i in cha:
		try:
			letter_count[i] += 1
		except Exception:
			letter_count[i] = 1

	return letter_count

