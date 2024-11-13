while True:
    word = input(str("Please type in a word: "))
    length = int(len(word))
    #print(length)
    if length > 1:
        print(f'There are {length} letters in the word {word}')
    print("Thank you!")