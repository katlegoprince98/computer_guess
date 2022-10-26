import random

def guess(num):
    ran_num = random.randint(100,num)
    guess = 0
    while guess != ran_num:
        guess = int(input(f"Guess a number between 100 and {num}"))
          
guess(1000)
