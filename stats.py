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
	del letter_count[" "]
	return sort_characters(letter_count)
def sort_characters(letter_count):
    char_list = []
    for char, count in letter_count.items():
        char_list.append({"char": char, "num": count})
    char_list.sort(reverse=True, key=lambda item: item["num"])
    return char_list
