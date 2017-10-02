import random
pics=[' ',
    '''
=========||
    |    ||
         ||
         ||
         ||
         ||
         || ''',
'''
=========||
    |    ||
    0    ||
         ||
         ||
         ||
         || ''',
'''
=========||
    |    ||
    0    ||
    |    ||
         ||
         ||
         || ''',
'''
=========||
    |    ||
    0    ||
   /|    ||
         ||
         ||
         || ''',
'''
=========||
    |    ||
    0    ||
   /|\   ||
         ||
         ||
         || ''',
'''
=========||
    |    ||
    0    ||
   /|\   ||
   /     ||
         ||
         || ''',
'''
=========||
    |    ||
    0    ||
   /|\   ||
   / \   ||
         ||
         || ''',
]

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote\
 crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole\
 monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat\
 raven rhino salmon seal shark sheep skunk sloth \
 snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()
print(words)
def getrandom(word):
        wordindex = random.randint(0,len(words)-1)
        #print(word[wordindex])
        return word[wordindex]
def displayboard(missed_letter,correct_letter,secret_letter,pics):
    
    print (pics[len(missed_letter)])
    print()
    
    print('Missed letters : ' , end= '')
    for letter in missed_letter:
        print (letter, end='')
    print()
    blanks = '_' * len(secret_letter)
   # print("Clue : Its a " +str(len(secret_letter))+ " Letter word")
    for i in range(len(secret_letter)):
        if secret_letter[i] in correct_letter:
            blanks = blanks[:i] + secret_letter[i] + blanks[i+1:]
    for letter in blanks :
        print (letter, end="")
    print()
    print("Clue : Its a " +str(len(secret_letter))+ " Letter word")
    
def get_guess(guessed_already):
    response =  False
    while response != True:
        guess  = input("Guess a letter")
        guess = guess.lower()
        if(len(guess) !=1):
                print("1 letter required: ")
        elif(guess in guessed_already):
                print("You already Guessed the letter : ")
        elif(guess not in "abcdefghijklmnopqrstuvwxyz"):
                print("Not a letter")
        else:
                response = True
                return guess
    
def play_again():
    wish = input("Do you want to Play Again: ?")
    wish = wish.lower()
    if(wish == 'yes' or wish== 'y'):
        return True
    else:
        return False
 
missed_letter= ""
correct_letter=""
secret_letter=getrandom(words)
gamesdone= False
 #gamestatus = False
while True: 
    displayboard(missed_letter,correct_letter,secret_letter,pics)
    guess  = get_guess(missed_letter + correct_letter)
    if guess in secret_letter:
            correct_letter = correct_letter + guess
            print(correct_letter)
            found_All=True
            for i in range(len(secret_letter)):
        #print("Length of Secret_le"len(secret_letter))
                #print("value of i : ",i)  
            
                if secret_letter[i] not in correct_letter:
                    found_All=False
                    break
            if found_All:
                    
                    print("Congratulation! You have won the game : ")
                    print("The Secret Letter is : ",secret_letter)
                    gamesdone=True
                    
            #gamestatus = True
    else : 
        missed_letter = missed_letter + guess
        print("Wrong Choice !!!")
        if(len(missed_letter)) == len(pics)-1:
            displayboard(missed_letter,correct_letter,secret_letter,pics)
            print('You have run out of guesses!\nAfter ' + str(len(missed_letter)) + ' missed guesses and \
             '             + str(len(correct_letter)) + ' correct guesses, the word was "' + secret_letter + '"')
            gamesdone=True
             #gamestatus=False 
    if gamesdone:
        #print("Inside gamesdone")                    
        if play_again():
            missed_letter= ""
            correct_letter=""
            secret_letter=getrandom(words)
            gamesdone= False
        else:
            break
            
