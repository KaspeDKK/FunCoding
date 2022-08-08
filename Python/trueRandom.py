"""

A python script that checks whether python random REALLY is random or not. Well check your yourself

Best test(Most random test):

    One occured  68  times

    Two occured  66  times

    Three occured  67  times

    Error Entries occured  134  times

"""


import random
import time

def randomizer(one, two, three, iteration, errorEntrySum):

    if iteration > MaxIterations:
        print('')
        print('One occured ', one, ' times')
        print('')
        print('Two occured ', two, ' times')
        print('')
        print('Three occured ', three, ' times')
        print('')
        print('Error Entries occured ', errorEntrySum, ' times')
        time.sleep(60)
        exit()
    else:
        iteration += 1

    choice = random.choice(list)
    if choice == 1:
        print(choice)
        one += 1
    if choice == 2:
        print(choice)
        two += 1
    if choice == 3:
        print(choice)
        three += 1
    else:
        print(choice, " - ERROR: Extra entry ingored")
        errorEntrySum += 1
    
    print('')
    randomizer(one, two, three, iteration, errorEntrySum)

one = 0
two = 0
three = 0
list = [1,2,3]
choice = 0
iteration = 0
errorEntrySum = 0
MaxIterations = 200 # Keep in mind that its this number +1. Adjust manually if it is an issue

randomizer(one, two, three, iteration, errorEntrySum)