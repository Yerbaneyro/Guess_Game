import random
from colorama import Fore
import time

# random number from 1 to 1000
random_number = random.randrange(1, 1000)
attempt = 0



print("""
        Welcome to Guess a number game!
        
        - Made by: Marcin Bednarz in 2022
        - v1.0.0  
""")

print(Fore.BLUE + """ 
        Rules:
            Computer choose a number from range 1 to 1000.
            Your task is to quess this numbers with as lowest
            attempts as possible. Ready? Let's go!
            
""")
time.sleep(1)

player_number = -1

while player_number != random_number:
    try:
        player_number = int(input(Fore.YELLOW + 'Type your number: '))

        if player_number > 1000 or player_number < 1:
            print(Fore.RED + "You are out of range! Computer choose number from 1 to 1000 range.")
    except:
        print(Fore.LIGHTRED_EX + "Only numbers are allowed! Try again!")
    else:
        if player_number > random_number:
            attempt += 1
            print(Fore.GREEN + 'Your number is to high. Try again!')
        elif player_number < random_number:
            attempt += 1
            print(Fore.CYAN + 'Your number is too low. Try again!')

print(Fore.BLUE + f'''
            CONGRATULATION!!!
        Random Number is { random_number }
        and you found in { attempt } attempts.
            
                Thanks for 
                playing! 
                
            www.mbednarz.website
''')