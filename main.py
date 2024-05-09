def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_letter_count(text)
    print(f"{num_words} words found in the document")
    print(f"{num_letters} letters found in the document")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_letter_count(text):
    book_string =  text
    lowered_book_string = book_string.lower()
    character_dict = {}
    for char in lowered_book_string:
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    return character_dict
    
    


main()