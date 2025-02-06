def read(contents):
    words = contents.split()
    count = 0
    for word in words:
        count += 1
    return count

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    print(read(file_contents))


    
main()