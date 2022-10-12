import random
import time
hangman_stages = ['''
It is just one, I know you can do this
  +---+
  |   |
      |
      |
      |
      |
=========
''', '''
YOU ARE THE BEST - 5 more attempts
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
I BELIEVE IN YOU - 4 more attempts
 +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
YOU CAN DO THIS - 3 more attempts
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
My nerves are going up- 2 MORE attempts
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
You are master of last turn, You can do it- Last Attempt
   +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
BYE BYE Good Friend, Take Care
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''']



WORDS = ['abruptly','absurd','awkward','blizzard','bookworm','buffoon','croquet','daiquiri','galvanize','glowworm','microwave',
    'lengths','keyhole','nightclub','syndrome','twelfth','vaporize','triphthong','zigzagging','whiskey','waltz']

end_of_game = False
lives = 6



def hangman():

    secretWord = random.choice(WORDS)
    secretWordlowerCase = secretWord.lower()
    correctLetter = []
    blanks = len(secretWord) * '_'
    print(f'\nSecret word: {blanks}')
    print(f'{hangman_stages[0]}\n')
    blanks = list(blanks)
    maxLife = len(hangman_stages) - 1
    lifeUsed = maxLife

    while lifeUsed > 0:
        letter = input('\nEnter a letter: ').lower()

        if len(letter) != 1 or not letter.isalpha():
            print('The value entered is invalid.\n')
        elif letter in correctLetter:
            print('This letter has already been entered. Enter another letter.\n')
        elif letter in secretWordlowerCase:
            for i, char in enumerate(secretWordlowerCase):
                if char == letter:
                    blanks[i] = letter
            correctLetter.append(letter)
            print(''.join(blanks))
        else:
            correctLetter.append(letter)
            lifeUsed -= 1
            print(f'You have lost a life. You have {lifeUsed} attempts left.')
            print(f'{hangman_stages[maxLife - lifeUsed]}\n')

        if ''.join(blanks) == secretWordlowerCase:
            print(f'Yaaaayyy..You saved a lige with your guess: {secretWord}.')
            break
    else:
        print(f'You lost. The secret word is: {secretWord}.')

print('''
  #     # ####### #        #####  ####### #     # #######             
       #  #  # #       #       #     # #     # ##   ## #                   
       #  #  # #       #       #       #     # # # # # #                   
       #  #  # #####   #       #       #     # #  #  # #####               
       #  #  # #       #       #       #     # #     # #                   
       #  #  # #       #       #     # #     # #     # #                   
        ## ##  ####### #######  #####  ####### #     # #######             
                                                                           
                                                                           
                         #####  ####                                       
                           #   #    #                                      
                           #   #    #                                      
                           #   #    #                                      
                           #   #    #                                      
                           #    ####                                       
                                                                           
 #     #       #       #     #     #####     #     #       #       #     # 
 #     #      # #      ##    #    #     #    ##   ##      # #      ##    # 
 #     #     #   #     # #   #    #          # # # #     #   #     # #   # 
 #######    #     #    #  #  #    #  ####    #  #  #    #     #    #  #  # 
 #     #    #######    #   # #    #     #    #     #    #######    #   # # 
 #     #    #     #    #    ##    #     #    #     #    #     #    #    ## 
 #     #    #     #    #     #     #####     #     #    #     #    #     #  
''')
name= input('Please Enter Your Name: ')
print('Welcome ' + name + ' !')
print('Try to save the man in 6 attempts!')
time.sleep(1)
hangman()