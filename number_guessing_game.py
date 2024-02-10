import random
num = random.randint(1, 100)

user = 0

computerwins = 0
userwins = 0

computerwins = int(computerwins)
userwins = int(userwins)

user = input("Enter your guess: ")
user = int(user)

while user != num:
    if user > num:
        print("Too high, it was", num)
        input("Guess again: ")
    elif user < num:
        print("Too low, it was", num)
        input("Guess again: ")
    else:
        print("You got it!")
        if user == num:
            break

#QUICK NOTE TO PROFESSOR REES:
        #My apologies for how incomplete this lab is. Since I missed class on the Wednesday that while loops were introduced and I had to do this on my own, I had a lot
        #more difficulty than usual. I was incredibly busy in the past few days and wasn't able to reach out for help. I intend to come to office hours next week to get
        #this code ironed out, just for my general knowledge. :)


#the original code, untouched:

#import random
#num = random.randint(1, 100)

#user = input("Enter your guess: ")
#user = int(user)

#if user > num:
#    print("Too high, it was", num)
#elif user < num:
#    print("Too low, it was", num)
#else:
#    print("You got it!")
