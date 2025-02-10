PATH_TO_FILE = r"./books/frankenstein.txt"

def count_words() -> int:
    num_of_words = 0
    with open(PATH_TO_FILE, "r") as file:
        file_contents = file.read()
        lines = file_contents.split()
        num_of_words += len(lines)
        print(type(file_contents))
    return num_of_words

def count_letters() -> dict:
    letters = {}
    with open(PATH_TO_FILE, "r") as file:
        file_contents = file.read()
        for letter in file_contents:
            temp = letter.lower()
            if temp in letters.keys():
                letters[temp] += 1
            else:
                letters[temp] = 1

    return letters

def analyze_book() -> None:
    num_of_words = count_words()
    letter_analysis = count_letters()

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_of_words} words found in the document")
    for key, item in letter_analysis.items():
        if key.isalpha():
            print(f"The '{key}' character was found {item} times")
    print("--- End report ---")

def main() -> None:
    analyze_book()
    



if "__main__" == __name__:
    main()

