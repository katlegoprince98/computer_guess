import random

def guess(num):
    ran_num = random.randint(1,num)
    guess = 0
    while guess != ran_num:
        guess = int(input(f"Guess a number between 1 and {num}: "))
        if guess < ran_num:
             print("Your guess is low, please try again")
        elif guess > ran_num:
            print("You guess was too high please try again")
            
    print(f"CONGRATULATIONS!!, you guessed the number {ran_num} correctly")
       
          
guess(5)
