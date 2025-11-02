def number_of_words(book):
    return len(book.split())

def sort_on(items):
    return items["num"]

def sort_letter_dict(letter_dict):
    list_of_letters = [{"char": k, "num": v} for k, v in letter_dict.items()]
    return sorted(list_of_letters, key=sort_on, reverse=True)

def letter_counts(book):
    words = book.split()
    letter_dict = {"a": 0} #dict()?
    for word in words:
        letters = list(word)
        for letter in letters:
            letter = letter.lower()
            if letter in letter_dict: #TODO
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
    return sort_letter_dict(letter_dict)




                

