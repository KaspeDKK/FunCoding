import time
import random

ff = ["fact", "false"]
reward = 0

# Setup console-pleasing motherfucker...
def Break():
    print('')

def roll(inputvalue):
    Break() # console-pleasing motherfuckers!

    rollvalue = random.choice(ff)
    print("the result is: ", rollvalue)

    Break() # console-pleasing motherfuckers!

    return rollvalue

def start():

    user_input = input("Hello User, Welcom to Fact OR False. Choose a bet amount: (2-999)")

    if int(user_input) >= 2 & int(user_input) <= 999:

        # reward user for win
        if roll(user_input) == 'fact':
            print('You got fact chief! congrats on your', reward, "moneyz!")
        # condole user for loss
        else:
            print('You got false dude :( - Better luck next time!')
    else:

        # restart program, since user is an absolute nincompoop
        print("Are you an idiot? you CANT bet than amount! Try again dummy...")
        start()

if __name__ == "__main__":
    Break() # console-pleasing motherfuckers!

    start()

    Break() # console-pleasing motherfuckers!
