import random
import sys

if len(sys.argv) != 3:
    sys.exit("Invalid Commands. There should only have 3 commands.")
# This will check for error
try:
    if int(sys.argv[1]) > int(sys.argv[2]):
        sys.exit("First integer must be greater than the second integer")
except ValueError:
    sys.exit('Must be valid integer')

random = random.randint(int(sys.argv[1]), int(sys.argv[2]))

while True:
    try: 
        guess = int(input(f'Guess a number between {sys.argv[1]} and {sys.argv[2]}: '))
    
    except ValueError:
        print("Enter a Valid number")

    else:
        if guess == random:
            print('Congradulation')
            break

        elif guess > random:
            print('Too high')

        else: 
            print('Too low')
