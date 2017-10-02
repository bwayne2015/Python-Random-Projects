import random

def generate_secret_num(digit):
    #This function returns a number which is passed paramerter digit number long
    sec_str = "" 
    str_list = list(range(10))
    #str_list = str(str_list)
    print(str_list)
    random.shuffle(str_list)
    print(str_list)
    #item = 0
    for item in range(digit):
        sec_str = sec_str + str(str_list[item])
    print(sec_str)
    return sec_str    

def play_again():
    response = input("DO you want to play again : ? (Yes or NO)")
    response = response.lower()
    if(response == "y" or response == "yes"):
        return True

def verify_guess(guess_number,secret_number):
    if(guess_number == secret_number):
        print("Congratulations you got the Number Right !!!!")
        play_again()
    clue = []
    for i in range(len(guess_number)):
        #print(guess_number[i])
        #print(secret_number[i])
        if guess_number[i] == secret_number[i]:
            #print("inside")
            clue.append('Fermi')
        elif guess_number[i] in secret_number:
            clue.append('Pico')
    if(len(clue)) == 0:
        print("Bagels")

    clue.sort()
    #print(clue)
    return " ".join(clue)            
def isdigit(num):
    #print(type(num))
#This function returns True only if it has a digit in String format
    #print("asedfg ",num)
    if num == "":
        return False
    #print("something1")
    for i in num:
        if i not in "0 1 2 3 4 5 6 7 8 9".split():
            return False
    return True





max_guess = 10
digit_number = 3

print('I am thinking of a %s-digit number. Try to guess what it is.' % (digit_number))
print('Here are some clues:')
print('When I say:    That means:')
print('  Pico         One digit is correct but in the wrong position.')
print('  Fermi        One digit is correct and in the right position.')
print('  Bagels       No digit is correct.')

while True:

    secret_number = generate_secret_num(digit_number)
    guess = 1
    while guess <= max_guess:
        guess_number = ""
        #print(type(guess_number))
        #is_digit = isdigit(guess)
        #print(is_digit)
        while len(guess_number) != digit_number or not  isdigit(guess_number):
            #print("Something")
            #print(type(guess_number))
            guess_number = input("Guess the number  : ")
        response = verify_guess(guess_number,secret_number)
        print(response)
        guess  = guess + 1
    if (guess > max_guess):
        print(" You Lost!!!! The correct number number is: %s" %(secret_number)) 

    if play_again():
        break   
