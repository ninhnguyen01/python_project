def replace():
    str = "Hello, I am [name]"
    word_to_replace = input("Enter the word to replace: ")
    word_replacement = input("Enter the word replacement: ")
    print(str.replace(word_to_replace, word_replacement))

replace()