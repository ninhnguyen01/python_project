# Import package
import random

# Set up the constants:
OBJECT_PRONOUN = ['Her', 'Him', 'Them']

POSSESIVE_PRONOUN = ['Her', 'His', 'Their']

PERSONAL_PRONOUN = ['She', 'He', 'They']

STATE = ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania',
            'Illinois', 'Ohio', 'Georgia', 'North Carolina', 'Michigan']

NOUN = ['Athlete', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor', 'Parent',
          'Cat', 'Dog', 'Chicken', 'Robot', 'Video Game', 'Avocado',
           'Plastic Straw','Serial Killer', 'Telephone Psychic']

PLACE = ['House', 'Attic', 'Bank Deposit Box', 'School', 'Basement',
            'Workplace', 'Donut Shop', 'Apocalypse Bunker']

WHEN = ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week']

# Main Function
def main():
    print('Clickbait Headline Generator')
    print('\n')
    print('Our website is influencing people into looking at ads!')
    while True:
        response = input('Enter the number of clickbait headlines to generate: ')
        if not response.isdecimal():
             print('Please enter a number.')
        
        else:
            numberOfHeadlines = int(response)
            break  # Exit the loop once a valid number is entered.
    
    for i in range(numberOfHeadlines):
          clickbaitType = random.randint(1, 8)
          
          if clickbaitType == 1:
              headline = generateAreMillenialsKillingHeadline()
          elif clickbaitType == 2:
              headline = generateWhatYouDontKnowHeadline()
          elif clickbaitType == 3:
              headline = generateBigCompaniesHateHerHeadline()
          elif clickbaitType == 4:
              headline = generateYouWontBelieveHeadline()
          elif clickbaitType == 5:
              headline = generateDontWantYouToKnowHeadline()
          elif clickbaitType == 6:
              headline = generateGiftIdeaHeadline()
          elif clickbaitType == 7:
              headline = generateReasonsWhyHeadline()
          elif clickbaitType == 8:
              headline = generateJobAutomatedHeadline()
  
          print(headline)

    print()

# Each of these functions returns a different type of headline:
def generateAreMillenialsKillingHeadline():
      noun = random.choice(NOUN)
      return 'Are Millenials Killing the {} Industry?'.format(noun)

def generateWhatYouDontKnowHeadline():
    noun = random.choice(NOUN)
    pluralNoun = random.choice(NOUN) + 's'
    when = random.choice(WHEN)
    return 'Without This {}, {} Could Kill You {}'.format(noun, pluralNoun, when)
 
def generateBigCompaniesHateHerHeadline():
    pronoun = random.choice(OBJECT_PRONOUN)
    state = random.choice(STATE)
    noun1 = random.choice(NOUN)
    noun2 = random.choice(NOUN)
    return 'Big Companies Hate {}! See How This {} {} Invented a Cheaper {}'.format(pronoun, state, noun1, noun2)
  
def generateYouWontBelieveHeadline():
    state = random.choice(STATE)
    noun = random.choice(NOUN)
    pronoun = random.choice(POSSESIVE_PRONOUN)
    place = random.choice(PLACE)
    return 'You Won\'t Believe What This {} {} Found in {} {}'.format(state, noun, pronoun, place)
  
def generateDontWantYouToKnowHeadline():
    pluralNoun1 = random.choice(NOUN) + 's'
    pluralNoun2 = random.choice(NOUN) + 's'
    return 'What {} Don\'t Want You To Know About {}'.format(pluralNoun1, pluralNoun2)
  
def generateGiftIdeaHeadline():
     number = random.randint(7, 15)
     noun = random.choice(NOUN)
     state = random.choice(STATE)
     return '{} Gift Ideas to Give Your {} From {}'.format(number, noun, state)
 
def generateReasonsWhyHeadline():
     number1 = random.randint(3, 19)
     pluralNoun = random.choice(NOUN) + 's'
     # number2 should be no larger than number1:
     number2 = random.randint(1, number1)
     return '{} Reasons Why {} Are More Interesting Than You Think (Number {} Will Surprise You!)'.format(number1, pluralNoun, number2)
 
def generateJobAutomatedHeadline():
     state = random.choice(STATE)
     noun = random.choice(NOUN)
 
     i = random.randint(0, 2)
     pronoun1 = POSSESIVE_PRONOUN[i]
     pronoun2 = PERSONAL_PRONOUN[i]
     if pronoun1 == 'Their':
         return 'This {} {} Didn\'t Think Robots Would Take {} Job. {} Were Wrong.'.format(state, noun, pronoun1, pronoun2)
     else:
         return 'This {} {} Didn\'t Think Robots Would Take {} Job. {} Was Wrong.'.format(state, noun, pronoun1, pronoun2)
 
# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
     main()