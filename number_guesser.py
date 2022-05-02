import random
#we import the random library
number = random.randint(1, 10)
#we are generating a random number from 1 to 10 
name = input("Hello welcome, What's your name? ")
#we are asking the user to imput his or her name 
number_of_guesses = 0
#we set the number of guesses to 0 
print('okay! '+ name+ ' I am Guessing a number between 1 and 10:')
#print our welcome statement and starting the game 
while number_of_guesses < 5:
    #a while loop that print wheather the number is too low or to high 
    guess = int(input())
    #user inputs guess number
    number_of_guesses += 1
    # we increment the number_of_guesses
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break
if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' guesses!')
    #printis the user was able to guess tne number 
else:
    print('You did not guess the number, The number was ' + str(number))
    # prints the correct answer if user didn't guess it 
    