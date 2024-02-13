import random
num = random.randint(1, 100)

user = 0
upbound = 100
lowbound = 1

guesses = 1

response = 0

user = input("Enter your guess: ")
user = int(user)

while user != num:
    if user > num:
        print("Too high")
        upbound = user
    elif user < num:
        print("Too low")
        lowbound = user
    else:
        print("You got it!")
    user = input(f"Guess again from numbers {lowbound} to {upbound}: ")
    user = int(user)
    guesses += 1
print(f"It took you {guesses} amount of guesses.")


        # if user == num:
            #break also skips the rest of the code

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