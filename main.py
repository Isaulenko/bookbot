def read(contents):
    words = contents.split()
    return len(words)

def count_char(contents):
    low_contents = contents.lower()
    char_counts = {}
    for char in low_contents:
        if char.isalpha():
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    return char_counts
    
def get_list(char_counts):
    char_list = []
    for char, count in char_counts.items():
        char_list.append({'char': char,"count": count})
    def sort_on(dict):
        return dict["count"]


    char_list.sort(reverse=True, key=sort_on)
    return char_list

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    word_count = read(file_contents)
    char_counts = count_char(file_contents)
    char_list = get_list(char_counts)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")

    for char_dict in char_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['count']} times")
    
    print("--- End report ---")
    
main()