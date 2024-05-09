def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_letter_count(text)
    character_list = get_character_list(num_letters)
    character_list.sort(reverse=True, key=sort_on)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()
    for char in character_list:
        if char["character"].isalpha() == True:
            print(f"The {char["character"]} character was found {char["char_count"]} times")

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
    
def get_character_list(char_dict):
    char_list = []
    for char, count in char_dict.items():
        new_dict = {"character": char, "char_count" :count}
        char_list.append(new_dict)
    return char_list
    
def sort_on(dict):
    return dict["char_count"]

main()