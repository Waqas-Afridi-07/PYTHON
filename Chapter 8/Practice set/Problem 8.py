def remove_word():

    words = ["apple", "banana", "orange", "grape"]

    print("Here is the list:")
    print(words)

    word = input("Type the word you want to remove: ")
    word = word.strip()
    
    if word in words:
        words.remove(word)
        print("Word removed!")
    else:
        print("Word not found in the list.")

    print("Now the list is:")
    print(words)

remove_word()
