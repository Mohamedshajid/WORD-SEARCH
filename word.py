def word_counter(text):
    words = text.split()
    word_count = len(words)
    return word_count

text = input("Enter the text: ")
print("Number of words:", word_counter(text))
