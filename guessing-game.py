import random

def computerGuess(lowval, highval, randnum, count=0):
    if highval >= lowval:
        # Set guess as median of lowval and highval.
        guess = lowval + (highval - lowval) // 2
        # If guess is correct, return count.
        if guess == randnum:
            return count
        # If guess is greater than randnum, call computerGuess to look
        # for the number between lowval and the current value of guess.
        elif guess > randnum:
            count = count + 1
            return computerGuess(lowval, guess-1, randnum, count)
        # If guess is lower than randnum, call computerGuess to look
        # for the number between the current value of guess and highval.
        else:
            count = count + 1
            return computerGuess(guess + 1, highval, randnum, count)

    return -1

# Generate a random number between 1 and 100.
randnum = random.randint(1, 101)

count = 0
guess = 0

while guess != randnum:
    # Get the user's guess.
    guess = int(input('Enter your guess between 1 and 100: '))

    if guess < randnum:
        print('Higher')
    elif guess > randnum:
        print('Lower')
    else:
        print('You guess it!')
        break

    count = count + 1

print('You took {} steps to guess the number.'.format(count))
print('The computer took {} steps!'.format(
    computerGuess(0, 100, randnum)))
