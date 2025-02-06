def read(contents):
    words = contents.split()
    return len(words)

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    print(read(file_contents))


    
main()