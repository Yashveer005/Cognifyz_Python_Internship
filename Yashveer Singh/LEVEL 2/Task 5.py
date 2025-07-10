import string
import os
os.chdir(os.path.dirname(__file__))
def count_word_occurrences(filename):
    word_counts = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    word = word.strip(string.punctuation)
                    word_counts[word] = word_counts.get(word, 0)+1
    except FileNotFoundError:
        print("File not found. Please make sure the file exists")
        return None
    return word_counts

def display_word_count(word_counts):
    sorted_word_counts = sorted(word_counts.items(), key=lambda x:x[0].lower())
    for word, count in sorted_word_counts:
        print(f"{word} : {count}")

while True:
    filename = input("Enter the filename : ")
    try:
        word_count = count_word_occurrences(filename)
        if word_count:   # Only call display if word_count is valid
            display_word_count(word_count)
            break
    except FileNotFoundError:
        print("File not found")

    choice = input("Do you want to enter another filename?(y/n) : ").lower()
    if choice != 'y' :
        break