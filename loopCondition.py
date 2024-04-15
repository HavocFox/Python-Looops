#Task 1: Loop Condition Exploration Write a while loop with a condition that will never be true (an infinite loop).
#Ask the user a series of questions until their answer triggers a break statement.

#Task 2: Conditional Exit Create a while loop that will terminate after 5 iterations,
#and each iteration you print which iteration it is on. (use a control variable)

while True:
    
    ans = input("Are cats better than dogs? ")
    if ans == 'yes':
        ans = input('Does Sonic the Hedgehog have a friend that is a cat? ')
        if ans == 'yes':
            ans = input('Does this cat friend have fire powers? ')
            if ans == 'yes':
                ans = input('Is this cat friend named after these powers? ')
                if ans == 'yes':
                    ans = input('Is Blaze the Cat from another dimension? ')
                    if ans == 'yes':
                        ans = input('Awesome. You know a non-main Sonic character! Do you think there are more questions? ')
                        if ans == 'yes':
                            print("Sorry, there aren't any more. I'm tired. Go play Sonic Rush.")
                            break

    else:
        print("Wrong.")
        break

