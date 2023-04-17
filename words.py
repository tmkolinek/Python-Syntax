def print_upper_words(words):
    """Prints list of words all in uppercase"""
    for current_word in words:
        print(current_word.upper())

def print_upper_words2(words):
    """Prints words in list in uppercase if it starts with e"""
    for current_word in words:
        if current_word.startswith('e') or current_word.startswith('E'):
            print(current_word.upper())

def print_upper_words3(words, must_start_with):
    """Prints words in uppercase that start with that certain letter"""
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break

