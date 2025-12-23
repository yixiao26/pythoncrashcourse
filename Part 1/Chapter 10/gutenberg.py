filename = input("Enter the filename: ")
word = input("Enter the word you want to count: ")

def count_word(filename, word):
    try:
        with open(filename) as file_object:
                contents = file_object.read()
                count = contents.lower().count(word.lower())
                print(f"The word '{word}' appears {count} times in the file.")

    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")

count_word(filename, word)