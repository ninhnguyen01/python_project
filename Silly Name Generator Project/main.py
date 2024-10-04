"""Turn a word into its Pig Latin Equivalent"""

#import package
import sys

VOWELS = 'aeiouy'

while True:
    word = input("Enter a word to get its Pig Latin Equivalent: ").lower()

    if word[0] in VOWELS:
        pig_latin = word + 'way'

    else:
        pig_latin = word[1:] + word[0] + 'ay'
    
    print()
    print("{}".format(pig_latin), file=sys.stderr)

    try_again = input("\n\nTry again? (Press ENTER else 'n' to stop)\n ")
    if try_again.lower() == 'n':
        sys.exit()